import pandas as pd
import numpy as np
import torch
import pickle
import pyro
import copy
from scipy.stats import sem

from .cvae_model import DiseaseCondVAE
from .basic_g2p import BasicG2PModel,BasicG2PMapLoss_Categorical
from .data import GeneToPhenotypeDataset
from .optim import AutoEncoderOptimizer

__version__ = "0.1.0"


class VAE_G2P:

	def _readModelFromFile(self,fName):
		with open(fName,'rb') as f:
			model_dict = torch.load(f,map_location='cpu')
		return model_dict


	def __init__(self,diseaseGeneDataset,nLatentDim,isLinear=True,**kwargs):
		self.diseaseGeneDataset = diseaseGeneDataset
		self.nLatentDim=nLatentDim
		self.isLinear=isLinear
		self.numSymptoms=self.diseaseGeneDataset.num_symptoms
		self.numFreqCats=self.diseaseGeneDataset.num_ordinal_freqs

		self.all_model_kwargs = kwargs

		if 'encoder_hyperparameters' not in self.all_model_kwargs.keys():
			self.all_model_kwargs['encoder_hyperparameters']={'n_layers' : 2, 'n_hidden' : 64, 'dropout_rate': 0.1, 'use_batch_norm':True}
		if 'decoder_hyperparameters' not in self.all_model_kwargs.keys():
			self.all_model_kwargs['decoder_hyperparameters']={'n_layers' : 2, 'n_hidden' : 64, 'dropout_rate': 0.1, 'use_batch_norm':True}

		if 'missing_freq_priors' not in self.all_model_kwargs.keys():
			self.all_model_kwargs['missing_freq_priors']=[0.0,3.0]

		if self.diseaseGeneDataset.aux_gene_info_table['return_dim'].sum()==0:
			self.basic_g2p=None
			self.isConditional=False
		else:
			self.basic_g2p=BasicG2PModel(self.diseaseGeneDataset,network_hyperparameters=self.all_model_kwargs['decoder_hyperparameters'],cut_points=self.diseaseGeneDataset.ordinal_cut_points[:-1])
			self.isConditional=True

		self.vae_g2p_model=DiseaseCondVAE(self.numSymptoms,self.numFreqCats,self.nLatentDim,baseline_g2p_model=self.basic_g2p,isLinear=self.isLinear,encoder_hyperparameters=self.all_model_kwargs['encoder_hyperparameters'],decoder_hyperparameters=self.all_model_kwargs['decoder_hyperparameters'],missing_freq_prior_mean=self.all_model_kwargs['missing_freq_priors'][0],missing_freq_prior_scale=self.all_model_kwargs['missing_freq_priors'][1],cut_points=self.diseaseGeneDataset.ordinal_cut_points[:-1])


	def Fit(self,batch_size,logFile=None,verbose=True,monitor_validation=True,prior_model_state=None,**kwargs):
		"""


		Parameters
		----------


		batch_size : int,
		    Size of dataset batches for inference. 

		verbose : bool, optional
		    Indicates whether or not to print (to std out) the loss function values and error after every epoch. The default is True.

		logFile: str, optional

		    File to log model fitting process.

		Keyword Parameters
		----------
		initLearningRate: float, optional
		    Specifies the maximum learning rate used during inference. Default is 0.01

		finalLearningRate: float, optional
		    Specifies the final learning rate used during inference. Default is 0.001		 

		errorTol: float, optional
		    Error tolerance in ELBO (computed on held out validation data) to determine convergence. Default is 1e-4.

		numParticles: int, optional
		    Number of particles (ie random samples) used to approximate gradient. Default is 1. Computational cost increases linearly with value.

		maxEpochs: int, optional
		    Maximum number of epochs (passes through training data) for inference. Note, because annealing and learning rate updates depend on maxEpochs, this offers a simple way to adjust the speed at which these values change. Default is 200.

		computeDevice: str or None, optional
		    Specifies compute device for inference. Default is None, which instructs algorithm to use cpu. Two other options are supported: 'cuda' and 'mps'. Note, if device number is not included (ex: 'cuda:0'), then it is automatically assumed to be '0'

		numDataLoaders: int
		    Specifies the number of threads used to process data and prepare for upload into the gpu. Note, due to the speed of gpu, inference can become limited by data transfer speed, hence the use of multiple DataLoaders to improve this bottleneck. Default is 0, meaning just the dedicated cpu performs data transfer.

		KLAnnealingParams: dict with keys 'initialTemp','maxTemp','fractionalDuration','schedule'
		    Parameters that define KL-Annealing strategy used during inference, important for avoiding local optima. Note, annealing is only used for computation of ELBO and gradients on training data. Validation data ELBO evaluation, used to monitor convergence, is performed at the maximum desired temperature (typically 1.0, equivalent to standard variational inference). Therefore, it is possible for the model to converge even when the temperature hasn't reached it's final value. It's also possible that further cooling would find a better optimum, but this is highly unlikely in practice.
		    initialTemp--initial temperature during inference. Default: 1.0 (no annealing)
		    maxTemp--final temperature obtained during inference. Default: 1.0 (standard variational inference)
		    fractionalDuration--fraction of inference epochs used for annealing. Default is 0.25
		    schedule--function used to change temperature during inference. Defualt is 'cosine'. Options: 'cosine','linear'



		Returns
		-------
		output : list
		    List containing the following information: [loss function value of best model (computed on validation data),sequence of training loss values, sequence of validation loss values, error estimates across iterations (computed on validation data)].



		"""


		######### Parse Keyword Arguments #########
		allKeywordArgs = list(kwargs.keys())


		if 'initLearningRate' in allKeywordArgs:
		    initLearningRate=kwargs['initLearningRate']
		else:
		    initLearningRate=0.01

		if 'finalLearningRate' in allKeywordArgs:
		    finalLearningRate=kwargs['finalLearningRate']
		else:
		    finalLearningRate=0.001


		if 'errorTol' in allKeywordArgs:
		    errorTol=kwargs['errorTol']
		else:
		    errorTol=1e-4

		if 'numParticles' in allKeywordArgs:
		    numParticles=kwargs['numParticles']
		else:
		    numParticles=1


		if 'maxEpochs' in allKeywordArgs:
		    maxEpochs=kwargs['maxEpochs']
		else:
		    maxEpochs=500


		if 'computeDevice' in allKeywordArgs:
		    computeDevice=kwargs['computeDevice']
		else:
		    computeDevice=None

		if 'numDataLoaders' in allKeywordArgs:
		    numDataLoaders=kwargs['numDataLoaders']
		    if computeDevice in [None,'cpu']:
		        assert numDataLoaders==0,"Specifying number of dataloaders other than 0 only relevant when using GPU computing"
		else:
		    numDataLoaders=0

		if 'KLAnnealingParams' in allKeywordArgs:
		    KLAnnealingParams=kwargs['KLAnnealingParams']
		    assert set(KLAnnealingParams.keys())==set(['initialTemp','maxTemp','fractionalDuration','schedule']),"KL Annealing Parameters must be dictionary with the following keys: 'initialTemp','maxTemp','fractionalDuration','schedule'"
		else:
		    KLAnnealingParams={'initialTemp':1.0,'maxTemp':1.0,'fractionalDuration':1.0,'schedule': 'cosine'}

		if 'EarlyStopPatience' in allKeywordArgs:
			EarlyStopPatience=kwargs['EarlyStopPatience']
		else:
			EarlyStopPatience=10


		pyro.clear_param_store()
		if self.isConditional==True:
			if prior_model_state is None:
				self.basic_g2p.Fit(batch_size,initLearningRate,maxEpochs,errorTol,compute_device=computeDevice,numDataLoaders=numDataLoaders,early_stop_patience=EarlyStopPatience,monitor_validation=False)
			else:
				self.basic_g2p.LoadModel(prior_model_state)

		optimizer=AutoEncoderOptimizer(self.vae_g2p_model,self.diseaseGeneDataset,optimizationParameters={'initLearningRate': initLearningRate,'maxEpochs': maxEpochs,'numParticles':numParticles,'finalLearningRate':finalLearningRate},computeConfiguration={'device':computeDevice,'numDataLoaders':numDataLoaders},KLAnnealingParams=KLAnnealingParams)
		output=optimizer.BatchTrain(batch_size,errorTol=errorTol,verbose=verbose,logFile=logFile,monitor_validation=monitor_validation,early_stop_patience=EarlyStopPatience)
		return output

	def PredictEmbedFromGeneOnly(self,gene_list,returnStdErrors=False):
		if self.isConditional==False:
			raise ValueError("Predictions from genes are only possible for a conditional model that is fed gene-specific information.")
		assert len(set(gene_list).difference(self.diseaseGeneDataset.gene_map.keys()))==0,"The following genes are not in the embedding table: {0:s}".format(','.join(list(set(gene_vec).difference(self.diseaseGeneDataset.gene_map.keys()))))

		gene_data=self.diseaseGeneDataset.ReturnGeneDataArrays(gene_list)
		modes_for_prior = torch.cat(self.vae_g2p_model.baseline_g2p_model.basic_net(gene_data),axis=1)
		p_m,p_std = self.vae_g2p_model.prior_model(torch.cat((modes_for_prior,gene_data),axis=1))

		output_table={'Genes':gene_list,'Embeddings':[x for x in p_m.detach().numpy()]}

		if returnStdErrors:
			output_table['Std Errors']=[x for x in p_std.detach().numpy()]
		output_table=pd.DataFrame(output_table)
		output_table.set_index('Genes',inplace=True)
		return output_table


	def PredictSymptomsFromGeneOnly(self,gene_list,num_particles=0):
		embeds=self.PredictEmbedFromGeneOnly(gene_list,returnStdErrors=True)
		z_loc=np.vstack(embeds.loc[gene_list]['Embeddings'].values)
		z_scale=np.vstack(embeds.loc[gene_list]['Std Errors'].values)
		if num_particles==0:
			symptom_probs=torch.sigmoid(self.vae_g2p_model.symptom_annotation_decoder.forward(torch.tensor(z_loc))).detach().numpy()

			symptom_freqs=torch.exp(pyro.distributions.OrderedLogistic(self.vae_g2p_model.symptom_frequency_decoder(torch.tensor(z_loc)),self.vae_g2p_model.cut_points).logits).detach().numpy()
		else:
			samples_from_priors = torch.normal(torch.tensor(z_loc)*torch.ones((num_particles,z_loc.shape[0],z_loc.shape[1])),torch.tensor(z_scale)*torch.ones((num_particles,z_loc.shape[0],z_loc.shape[1])))

			symptom_probs=np.zeros((len(gene_list),self.numSymptoms))
			symptom_freqs=np.zeros((len(gene_list),self.numSymptoms,self.numFreqCats))

			for i in range(num_particles):
				symptom_probs+=torch.sigmoid(self.vae_g2p_model.symptom_annotation_decoder.forward(samples_from_priors[i])).detach().numpy()/num_particles
				symptom_freqs+=torch.exp(pyro.distributions.OrderedLogistic(self.vae_g2p_model.symptom_frequency_decoder(samples_from_priors[i]),self.vae_g2p_model.cut_points).logits).detach().numpy()/num_particles

		output_table=pd.DataFrame([],index=self.diseaseGeneDataset.symptom_map.keys(),columns=gene_list)
		for i,gene in enumerate(gene_list):
			output_table[gene]=list(zip(symptom_probs[i],symptom_freqs[i]))
		return output_table

	

	def _per_datum_elbo(self,hpo_freq_pairs,gene_list,num_particles=10):
		assert isinstance(hpo_freq_pairs,list),"The provided HPO-frequncy pairs must be an interable of ('HPO Symptom','Frequency') nested within a list."
		if self.isConditional==True:
			assert isinstance(gene_list,list),"Conditional VAE model expects a list of genes in order to compute ELBO"
			assert len(hpo_freq_pairs)==len(gene_list) or (len(hpo_freq_pairs)==1 or len(gene_list)==1),"Number of provided symptom-frequency pair datasets must equal number of genes, unless number of genes or the number of symptom-frequency pair datasets is equal to 1, at which point the data type with length 1 is broadcasted to the same size as the other dataset."
			annot_array=torch.zeros((max(len(hpo_freq_pairs),len(gene_list)),self.numSymptoms),dtype=torch.float32)
			freq_array=torch.zeros((max(len(hpo_freq_pairs),len(gene_list)),self.numSymptoms),dtype=torch.float32)
			if len(gene_list)<len(hpo_freq_pairs):
				gene_list=gene_list*len(hpo_freq_pairs)
			elif len(gene_list)>len(hpo_freq_pairs):
				hpo_freq_pairs=hpo_freq_pairs*len(gene_list)
		else:
			gene_list=[]
			annot_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)
			freq_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)

		for t,hpo_freq_vec in enumerate(hpo_freq_pairs):
			idx_vec=[self.diseaseGeneDataset.symptom_map[x[0]] for x in hpo_freq_vec]
			freq_vec=[self.diseaseGeneDataset._ProcessSymptomCounts(x[1],self.diseaseGeneDataset.symptom_count_prior) for x in hpo_freq_vec]
			annot_array[t,idx_vec]=1.0
			freq_array[t,idx_vec]=torch.tensor(freq_vec,dtype=torch.float32)
		if self.isConditional==True:
			data=(annot_array,freq_array,self.diseaseGeneDataset.ReturnGeneDataArrays(gene_list))
		else:
			data=(annot_array,freq_array,None)

		elbo=self.vae_g2p_model.per_datum_ELBO(*data,num_particles=num_particles)
		return elbo.detach().numpy().ravel()

	def PerplexCompare(self,hpo_freq_pairs,gene_list=None,index=None,num_particles=10):

		perplex_vec = -1.0*self._per_datum_elbo(hpo_freq_pairs,gene_list=gene_list,num_particles=num_particles)
		if self.isConditional==True:
			model_compare_results=self.basic_g2p.PerplexCompareNull(hpo_freq_pairs,gene_list)
			model_compare_results['VAE_G2P Perplex.']=perplex_vec
			model_compare_results['VAE_G2P-BasicG2PModel']=model_compare_results['VAE_G2P Perplex.']-model_compare_results['BasicG2PModel Perplex.']
			model_compare_results['VAE_G2P-Null']=model_compare_results['VAE_G2P Perplex.']-model_compare_results['Null Perplex.']
			model_compare_results['Genes']=gene_list
			model_compare_results=pd.DataFrame(model_compare_results)
		else:

			annot_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)
			freq_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)
			for t,hpo_freq_vec in enumerate(hpo_freq_pairs):
			    idx_vec=[self.diseaseGeneDataset.symptom_map[x[0]] for x in hpo_freq_vec]
			    freq_vec=[self.diseaseGeneDataset._ProcessSymptomCounts(x[1],self.diseaseGeneDataset.symptom_count_prior) for x in hpo_freq_vec]
			    annot_array[t,idx_vec]=1
			    freq_array[t,idx_vec]=torch.tensor(freq_vec,dtype=torch.float32)

			null_model_log_odds=tuple(torch.logit(self.diseaseGeneDataset._torchWrapper(x)).unsqueeze(dim=0) for x in self.diseaseGeneDataset.InferNullModel().values())
			output=np.zeros((perplex_vec.shape[0],3))
			perplex_function_null=BasicG2PMapLoss_Categorical()
			for i in range(output.shape[0]):
				output[i,0]=perplex_vec[i]
				output[i,1]=perplex_function_null(null_model_log_odds[0],null_model_log_odds[1],null_model_log_odds[2], annot_array[i:i+1],freq_array[i:i+1]).detach().item()
				output[i,2]=output[i,0]-output[i,1]

			model_compare_results={}
			model_compare_results['VAE_G2P Perplex.']=output[:,0]
			model_compare_results['Null Perplex.']=output[:,1]
			model_compare_results['VAE_G2P-Null']=output[:,2]
			model_compare_results=pd.DataFrame(model_compare_results)

		if index is not None:
			model_compare_results['Index']=index
		else:
			model_compare_results['Index']=['IDX_{0:d}'.format(x) for x in range(len(hpo_freq_pairs))]
		model_compare_results.set_index('Index',inplace=True)
		return model_compare_results




	def _embedDisease(self,hpo_freq_pairs,gene_list=None):
		assert isinstance(hpo_freq_pairs,list),"The provided HPO-frequncy pairs must be an interable of ('HPO Symptom','Frequency') nested within a list."
		if self.isConditional==True:
			assert isinstance(gene_list,list),"Conditional VAE model expects a list of genes in order to compute ELBO"
			assert len(hpo_freq_pairs)==len(gene_list) or (len(hpo_freq_pairs)==1 or len(gene_list)==1),"Number of provided symptom-frequency pair datasets must equal number of genes, unless number of genes or the number of symptom-frequency pair datasets is equal to 1, at which point the data type with length 1 is broadcasted to the same size as the other dataset."
			annot_array=torch.zeros((max(len(hpo_freq_pairs),len(gene_list)),self.numSymptoms),dtype=torch.float32)
			freq_array=torch.zeros((max(len(hpo_freq_pairs),len(gene_list)),self.numSymptoms),dtype=torch.float32)
			if len(gene_list)<len(hpo_freq_pairs):
				gene_list=gene_list*len(hpo_freq_pairs)
			elif len(gene_list)>len(hpo_freq_pairs):
				hpo_freq_pairs=hpo_freq_pairs*len(gene_list)
		else:
			assert gene_list is None,"Passing gene list to a vanilla VAE model is not allowed."
			gene_list=[]
			annot_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)
			freq_array=torch.zeros((len(hpo_freq_pairs),self.numSymptoms),dtype=torch.float32)

		for t,hpo_freq_vec in enumerate(hpo_freq_pairs):
			idx_vec=[self.diseaseGeneDataset.symptom_map[x[0]] for x in hpo_freq_vec]
			freq_vec=[self.diseaseGeneDataset._ProcessSymptomCounts(x[1],self.diseaseGeneDataset.symptom_count_prior) for x in hpo_freq_vec]
			annot_array[t,idx_vec]=1.0
			freq_array[t,idx_vec]=torch.tensor(freq_vec,dtype=torch.float32)

		if self.isConditional==True:
			data=(annot_array,freq_array,self.diseaseGeneDataset.ReturnGeneDataArrays(gene_list))
		else:
			data=(annot_array,freq_array,None)

		p_m,p_std=self.vae_g2p_model.posterior_latent_state(*data)

		return p_m.detach().numpy(),p_std.detach().numpy()


	def EmbedDisease(self,hpo_freq_pairs,gene_list=None,index=None,returnStdErrors=False):

		pm,pstd=self._embedDisease(hpo_freq_pairs,gene_list)

		if index is None:
			index=['IDX_{0:d}'.format(x) for x in range(len(hpo_freq_pairs))]
		if gene_list is None:
			gene_list=['NA']*len(hpo_freq_pairs)
		output_table={'Index':index,'Gene':gene_list,'Embeddings':[x for x in pm]}
		if returnStdErrors:
			output_table['Std Errors']=[x for x in pstd]

		output_table=pd.DataFrame(output_table)
		output_table.set_index('Index',inplace=True)
		return output_table

	def EstimateAnnotationRates(self,hpo_freq_pairs,gene_list=None,index=None,estimateStdError=False,num_particles=100):
		if estimateStdError==False:
			output_table=self.EmbedDisease(hpo_freq_pairs,gene_list=gene_list,index=index,returnStdErrors=False)
		else:
			output_table=self.EmbedDisease(hpo_freq_pairs,gene_list=gene_list,index=index,returnStdErrors=True)

		annot_table=output_table[['Gene']].copy()
		annot_table['Annot. Rates']=[pd.NA for i in range(output_table.shape[0])]

		for idx in output_table.index:
			embed_tensor=torch.tensor(output_table.loc[idx]['Embeddings'],dtype=torch.float32).unsqueeze(0)
			if estimateStdError==False:
				pred_annots=torch.sigmoid(self.vae_g2p_model.symptom_annotation_decoder(embed_tensor)).detach().numpy().squeeze(0)
				annot_table.loc[idx]['Annot. Rates']=dict(zip([self.diseaseGeneDataset.inverse_symptom_map[x] for x in range(pred_annots.shape[0])],pred_annots))

			else:
				embed_scale=torch.tensor(output_table.loc[idx]['Std Errors'],dtype=torch.float32).unsqueeze(0)
				samples=torch.normal(torch.ones(num_particles,embed_tensor.shape[0])*embed_tensor,torch.ones(num_particles,embed_tensor.shape[0])*embed_scale)
				pred_annots_all=torch.sigmoid(self.vae_g2p_model.symptom_annotation_decoder(samples)).detach().numpy()
				pred_annots=list(zip(list(pred_annots_all.mean(axis=0)),list(sem(pred_annots_all,axis=0))))

				annot_table.loc[idx]['Annot. Rates']=dict(zip([self.diseaseGeneDataset.inverse_symptom_map[x] for x in range(len(pred_annots))],pred_annots))
			
		return annot_table


	def EstimateSymptomFrequencies(self,hpo_freq_pairs,gene_list=None,index=None,estimateStdError=False,num_particles=100):
		if estimateStdError==False:
			output_table=self.EmbedDisease(hpo_freq_pairs,gene_list=gene_list,index=index,returnStdErrors=False)
		else:
			output_table=self.EmbedDisease(hpo_freq_pairs,gene_list=gene_list,index=index,returnStdErrors=True)


		symptom_table=output_table[['Gene']].copy()
		symptom_table['Symptom Freq.']=[pd.NA for i in range(output_table.shape[0])]
		for idx in output_table.index:
			embed_tensor=torch.tensor(output_table.loc[idx]['Embeddings'],dtype=torch.float32).unsqueeze(0)
			if estimateStdError==False:
				pred_class_full=pyro.distributions.OrderedLogistic(self.vae_g2p_model.symptom_frequency_decoder(embed_tensor),self.vae_g2p_model.cut_points).logits.squeeze(dim=0)
				pred_annots=torch.exp(pred_class_full).detach().numpy()
			else:
				embed_scale=torch.tensor(output_table.loc[idx]['Std Errors'],dtype=torch.float32).unsqueeze(0)
				samples=torch.normal(torch.ones(num_particles,embed_tensor.shape[0])*embed_tensor,torch.ones(num_particles,embed_tensor.shape[0])*embed_scale)
				pred_class_full=pyro.distributions.OrderedLogistic(self.vae_g2p_model.symptom_frequency_decoder(samples),self.vae_g2p_model.cut_points).logits.squeeze(dim=0)

				pred_annots_all=torch.exp(pred_class_full).detach().numpy()
				pred_annots=list(zip(pred_annots_all.mean(axis=0),sem(pred_annots_all,axis=0)))
			
			symptom_table.loc[idx]['Symptom Freq.']=dict(zip([self.diseaseGeneDataset.inverse_symptom_map[x] for x in range(len(pred_annots))],pred_annots))
		return symptom_table





	def LoadModel(self,stored_model):
		"""
		Loads previously fit model either from a dictionary (generated using PackageModel) or from a file path (with file constructed using PackageModel)

		Parameters
		----------
		stored_model : either dict or str (file path)

		Returns
		-------
		None.

		"""
		if not isinstance(stored_model,dict):
			assert isinstance(stored_model,str),"Expects file name if not provided with dictionary."
			stored_model = self._readModelFromFile(stored_model)

		assert set(stored_model.keys())==set(['model_state','meta_data','variational_post_params','baseline_g2p_model']),"Model dictionary must contain the following elements: 'model_state','meta_data','baseline_g2p_model'"
		if self.diseaseGeneDataset.aux_gene_info_table['return_dim'].sum()>0:
			self.basic_g2p=BasicG2PModel(self.diseaseGeneDataset,network_hyperparameters=stored_model['meta_data']['all_model_kwargs']['decoder_hyperparameters'],cut_points=self.diseaseGeneDataset.ordinal_cut_points[:-1])
		else:
			self.basic_g2p=None
		self.vae_g2p_model=DiseaseCondVAE(
			stored_model['meta_data']['numSymptoms'],
			stored_model['meta_data']['numFreqCats'],
			stored_model['meta_data']['nLatentDim'],
			self.basic_g2p,
			isLinear=stored_model['meta_data']['isLinear'],
			encoder_hyperparameters=stored_model['meta_data']['all_model_kwargs']['encoder_hyperparameters'],
			decoder_hyperparameters=stored_model['meta_data']['all_model_kwargs']['decoder_hyperparameters'],
			missing_freq_prior_mean=stored_model['meta_data']['all_model_kwargs']['missing_freq_priors'][0],
			missing_freq_prior_scale=stored_model['meta_data']['all_model_kwargs']['missing_freq_priors'][1],
			cut_points=self.diseaseGeneDataset.ordinal_cut_points[:-1]
			)
		self.vae_g2p_model.load_state(stored_model)
	


	def SaveModel(self,fName=None):
		"""
		Packages the current model and returns it as a python dictionary. Will optionally write this dictionary to disk using PyTorch.

		Parameters
		----------
		fName : str, default None
		    File path to save model to disk. The default is None, which means that only a model dictionary will be returned.

		Returns
		-------
		model_dict : dict
		    Dictionary containing fitted model parameters in addition to general meta data.

		"""
		model_dict = self.vae_g2p_model.package_state()
		model_dict['meta_data']={}
		model_dict['meta_data']['numSymptoms']=self.numSymptoms
		model_dict['meta_data']['numFreqCats']=self.numFreqCats
		model_dict['meta_data']['nLatentDim']=self.nLatentDim
		model_dict['meta_data']['isLinear']=self.isLinear
		model_dict['meta_data']['all_model_kwargs']=self.all_model_kwargs
		if fName is not None:
		    with open(fName,'wb') as f:
		        torch.save(model_dict,f)
		return model_dict


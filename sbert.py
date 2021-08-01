
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
import time 
import streamlit as st
import pickle

def sentence_embeddings(sentence):
  embedder = SentenceTransformer('paraphrase-distilroberta-base-v2')
  # return embedder.encode(sentence, convert_to_tensor=True)
  return embedder.encode(sentence)


# def similarity(query_embeddings,docs_embeddings,max_n=10, top_k=5):

# 	cos_scores = util.pytorch_cos_sim(query_embeddings, docs_embeddings)[0]
# 	# cos_scores = cos_scores.cpu()
# 	# try:

# 	pickle.dump(cos_scores, open("cos_scores1", 'wb'))
# 	top_results = torch.topk(cos_scores, k=max_n) 

# 	return zip(top_results[0], top_results[1])
# 	# except:
# 	# 	pass
# def get_query_top_k(query, query_embeddings, docs, docs_embeddings, max_n=10, top_k=5, min_p=0.7, exact_match=True):

# 	count=0
# 	top_k_list = []

# 	for score, idx in similarity(query_embeddings, docs_embeddings, max_n=max_n):
# 		# st.write(score)
# 		score = score.item() #score is tensor
# 		if count<top_k and ((score>min_p and exact_match) or (score<=0.99 and score>min_p)): 
# 			count=count+1 
# 			top_k_list.append({"query":query,"sentence":docs[idx],"score":score}) 
# 		return top_k_list

	# comparison_dict_08_cleaned_all = {}
	# #sentence_embeddings_dict
	# key_list = list(sentence_embeddings_dict_updated.keys())

	# for i in range(len(key_list)-1):
	# 	key1 = key_list[i]
	# 	try:
	# 	# if key1 != 'Umbrella.docx': 

	# 		for key2 in key_list[i+1:]:
	# 			output = main(key1, whitepaper_dict_cleaned[key1], key2, whitepaper_dict_cleaned[key2], threshold=0.8, exact_match=True)
	# 			comparison_dict_08_cleaned_all[key1+'@'+key2] = output

	# 	except:
	# 		pass

def compare(sentence_embeddings_dict, sentences_file_name, sentences_file, queries_file_name, queries_file, document_cleaned_embeddings, threshold=0.8, exact_match=True):

	min_p = 0.8
	top_k_list = []
	for i in range(len(document_cleaned_embeddings)):

		cos_scores = util.pytorch_cos_sim(document_cleaned_embeddings[i], sentence_embeddings_dict[sentences_file_name])[0]

		top_results = torch.topk(cos_scores, k=10) 

		top_k = 5
		count = 0

		for score, idx in zip(top_results[0], top_results[1]):

			score = score.item() #score is tensor
			if count<top_k and ((score>min_p and True) or (score<=0.99 and score>min_p)): 
				count=count+1 
				top_k_list.append({"query":i,"sentence":sentences_file[idx],"score":score, "document":sentences_file_name}) 

	return top_k_list


	# start = time.time()

	# corpus = sentences_file #repository
	# queries = queries_file #new whitepaper

	# corpus_embeddings = sentence_embeddings_dict[sentences_file_name]
	# # query_embeddings = sentence_embeddings_dict[queries_file_name]
	# query_embeddings = document_cleaned_embeddings
	# # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
	# n = 10 
	# top_k = 5

	# data = []
	# counter = 0

	# # similarity(query_embeddings, docs_embeddings, max_n=max_n)

	# for query in queries:
	# 	a = query
	# 	b = query_embeddings[counter]
	# 	c = corpus
	# 	d = corpus_embeddings # same as docs embeddings

	# 	# top_k_list = get_query_top_k(query,query_embeddings[counter], corpus, corpus_embeddings, max_n = n, top_k = top_k, min_p=threshold)
	# 	top_k_list = get_query_top_k(a,b, c, d , max_n = n, top_k = top_k, min_p=threshold)
	# 	data.extend(top_k_list)
	# 	counter += 1

	# df = pd.DataFrame(data)
	# end = time.time()
	# e = int(end - start)
	# st.write(e)
	
	# return df





# df1 = pd.DataFrame(columns = ['key', 'query', 'source', 'score'])
# counter = 0
# for key, value in comparison_dict_08_cleaned_all.items(): 
# if len(value) > 0:
# for i in value.values:
#   score = i[2]
#   query = i[1]
#   source = i[0]

#   # some_list.append([key, ])
#   df1.loc[counter, :] = [key, query, source, score]

# #       counter += 1   

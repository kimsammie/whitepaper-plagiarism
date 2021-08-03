import streamlit as st
import pandas as pd
import numpy as np
import time
import pandas as pd
from clean_doc import *
import pickle 
from sbert import *
import time 


def write():
	new_whitepaper = st.sidebar.file_uploader("Upload A Whitepaper", type=("docx"))
	
	if new_whitepaper is not None:

		try:
			st.write("Cleaning the new whitepaper")
			start = time.time()
			document_cleaned = clean_doc(new_whitepaper)
			st.write(document_cleaned)
			end = time.time()
			e = int(end - start)
			st.write("Time took for cleanup:", e, "second(s)")
		except Exception as e:
			st.write(e)

		try:	
			st.write("Creating sentence embeddings")
			start = time.time()
			document_cleaned_embeddings = [sentence_embeddings(i) for i in document_cleaned]
			# document_cleaned_embeddings = pickle.load(open("document_cleaned_embeddings", "rb"))
			end = time.time()
			e = int(end - start)
			st.write("Time took for creating sentence embeddings:", e, "second(s)")
		except Exception as e:
			st.write(e)
		

		# pickle.dump(document_cleaned_embeddings, open("document_cleaned_embeddings", "wb")) -- save a sample for troubleshooting

		# upload the existing sentence embeddings and cleaned sentences from the whitepaper database
		sentence_embeddings_dict = pickle.load(open('/Users/kimsa/OneDrive/Documents/Plagiarism/sentence_embeddings_dict_updated.pkl', 'rb'))
		whitepaper_dict_cleaned = pickle.load(open('/Users/kimsa/OneDrive/Documents/Plagiarism/whitepaper_dict_cleaned.pkl', 'rb'))

		if st.button("Get Similarity Score"):

			key_list = list(sentence_embeddings_dict.keys())

			# key1 = "New Whitepaper"

			st.write("Comparing against the existing whitepaper database")  

			data = []

			for key2 in key_list:

				try:
					output = compare(sentence_embeddings_dict, key2, whitepaper_dict_cleaned[key2], document_cleaned_embeddings)
					data.extend(output)
				
				except:
					pass
				
			df = pd.DataFrame(data)
			df['New Whitepaper Sentence'] = df['query'].apply(lambda x: document_cleaned[int(x)]) # x is the query column value
			# df['New Whitepaper Name'] = key1
			df = df[["Score", "Existing Whitepaper Name in Database", "Existing Whitepaper Sentence", "New Whitepaper Sentence"]]
			st.table(df)
			
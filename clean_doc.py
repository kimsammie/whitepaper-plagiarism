
import nltk 
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# pip install python-docx - needs to be done in a terminal
import docx
import time 
import streamlit as st

def readtxt(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def clean_doc(new_whitepaper):
	# whitepaper_dict = {}
# folder = '/content/drive/MyDrive/Plagiarism/Whitepapers_word'
# for file in os.listdir(folder):
#   filepath = os.path.join(folder, file)
  	# tokenized_text_raw = sent_tokenize(readtxt(new_whitepaper)) #need to do lower later
	# start = time.time()
	tokenized_text_lower = sent_tokenize(readtxt(new_whitepaper).lower())
	document_cleaned = []
	for sentence in tokenized_text_lower:
		sentence = sentence.replace("::", "")
		sentence = sentence.replace("--", "")
		sentence = sentence.replace("- ", "")
		sentence = sentence.replace("  ", "")

		if len(word_tokenize(sentence)) > 20:
			document_cleaned.append(sentence)

  	# whitepaper_dict[new_whitepaper] = document_cleaned

	# end = time.time()
	# e = int(end - start)
	# st.write("time took for cleanup:", e, "second(s)")
	return document_cleaned

# st.write
# whitepaper_dict = pickle.load(open('/content/drive/MyDrive/Plagiarism/Whitepapers_txt/whitepaper_dict.pkl', 'rb'))

# whitepaper_dict_cleaned = {}
# counter = 0
# for key, value in whitepaper_dict.items():

#     document_cleaned = []
#     for sentence in value[1]:
#         sentence = sentence.replace("::", "")
#         sentence = sentence.replace("--", "")
#         sentence = sentence.replace("- ", "")
#         sentence = sentence.replace("  ", "")
        
#         if len(word_tokenize(sentence)) > 5:
#           document_cleaned.append(sentence)

#     whitepaper_dict_cleaned[key] = document_cleaned

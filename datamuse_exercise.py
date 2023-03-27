import json,requests
import streamlit as st

st.header("Welcome to the app which searchs rhymes, synonyms, antonyms, and related words to a given input!")

keyword = st.text_input('Please provide a keyword to search:', '')
url_rhy= 'https://api.datamuse.com/words?rel_rhy=' + keyword
url_ml= 'https://api.datamuse.com/words?ml=' + keyword
url_sl= 'https://api.datamuse.com/words?sl=' + keyword
url_syn= 'https://api.datamuse.com/words?rel_syn=' + keyword
url_ant= 'https://api.datamuse.com/words?rel_ant=' + keyword

response_syn = requests.get(url_syn)
response_ant = requests.get(url_ant)    
response_rhy = requests.get(url_rhy)
response_ml = requests.get(url_ml)
response_sl = requests.get(url_sl)  

dataFromDatamuse_syn = json.loads(response_syn.text)
dataFromDatamuse_ant = json.loads(response_ant.text)
dataFromDatamuse_rhy = json.loads(response_rhy.text)
dataFromDatamuse_ml = json.loads(response_ml.text)
dataFromDatamuse_sl = json.loads(response_sl.text)

st.text('Synonym\'s of', keyword, 'are:', dataFromDatamuse_syn)
st.text('Antonym\'s of', keyword, 'are:', dataFromDatamuse_ant)
st.text('Words that rhyme with', keyword, 'are:', dataFromDatamuse_rhy)
st.text('Words that have similar meanings with', keyword, 'are:', dataFromDatamuse_ml)
st.text('Words that sound like', keyword, 'are:', dataFromDatamuse_sl)

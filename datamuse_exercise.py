import json,requests
import streamlit as st

st.header("Welcome to the app which searchs rhymes, synonyms, antonyms, and related words to a given input!")

criterion = st.multiselect("What would you like to search?", ("Rhymes", "Synonyms", "Antonyms", "Sounds Similar", "Means Like", "All"), default=None)
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

st.write(criterion)

if criterion == "Rhymes":
  st.write('Words that rhyme with', keyword, 'are:', dataFromDatamuse_rhy)

if criterion == "Synonyms":
  st.write('Synonym\'s of', keyword, 'are:', dataFromDatamuse_syn)

if criterion == "Antonyms":
  st.write('Antonym\'s of', keyword, 'are:', dataFromDatamuse_ant)

if criterion == "Sounds Similar":
  st.write('Words that sound like', keyword, 'are:', dataFromDatamuse_sl)
  
if criterion == "Means Like":
  st.write('Words that have similar meanings with', keyword, 'are:', dataFromDatamuse_ml)

if criterion == "All":
  st.write('Synonym\'s of', keyword, 'are:', dataFromDatamuse_syn)
  st.write('Antonym\'s of', keyword, 'are:', dataFromDatamuse_ant)
  st.write('Words that rhyme with', keyword, 'are:', dataFromDatamuse_rhy)
  st.write('Words that have similar meanings with', keyword, 'are:', dataFromDatamuse_ml)
  st.write('Words that sound like', keyword, 'are:', dataFromDatamuse_sl)

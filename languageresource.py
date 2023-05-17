import streamlit as st
import json, requests
from googletrans import Translator
from gtts import gTTS
from wiktionaryparser import WiktionaryParser

#tools:
translator = Translator()
parser = WiktionaryParser()
lang_options = {
  'de' : 'German / Deutsch / Tedesco',
  'en' : 'English / Englisch / Inglese',
  'it' : 'Italian / Italienisch / Italiano'
}

trans_options = {
  'de' : 'German / Deutsch / Tedesco',
  'en' : 'English / Englisch / Inglese',
  'it' : 'Italian / Italienisch / Italiano'
}

#Nonce Variables
trans_option = None
working_lang2 = None
lang_option = None
working_lang = None
user_input = None
trans_lang2 = None
trans_lang = None

#starter material
st.title("Multilingual Speed Reference")

criterion = st.multiselect("Let's get started! Which resources do you need?", ("Translation", "Pronunciation", "Same-Language Definition", "Grammatical Information (Conjugations/Declensions)", "Etymology", "Example, i.e. Word in Context", "All"), default=None)

if criterion:
  lang_option = st.selectbox("Please enter your Working Language?:", lang_options.values())
  st.caption("TIP: your Working Language is the language of the words you will be inserting into the program. For example, if I want to translate the word 'Hund', then the Working Language is 'German'.")

if lang_option:
  st.header('PLEASE ENTER A WORD:')
  user_input = st.text_input('')

#Setting Languages:
if lang_option:
  key = [k for k, v in lang_options.items() if v == lang_option]
  working_lang = key[0]

for y in criterion:
  if y == "Translation":
    trans_option = st.selectbox("Please, select the language to translate into:", trans_options.values())
  elif y == "All":
    trans_option = st.selectbox("Please, select the language to translate into:", trans_options.values())
  else:
    pass
    
if trans_option:
  key = [j for j, w in trans_options.items() if w == trans_option]
  trans_lang = key[0]
 
if working_lang == 'de':
  working_lang2 = 'german'
elif working_lang == 'en':
  working_lang2 = 'english'
elif working_lang == 'it':
  working_lang2 = 'italian'
else:
  pass

if trans_lang == 'de':
  trans_lang2 = 'german'
elif trans_lang == 'en':
  trans_lang2 = 'english'
elif trans_lang == 'it':
  trans_lang2 = 'italian'
else:
  pass

#url_lang_info = 'https://api.dictionaryapi.dev/api/v2/entries/' + dest_lang + '/' + user_input
#lang_info_resp = requests.get(url_lang_info)
#json.loads(lang_info_resp.text)

#TO ADD SPEECH TO TEXT 

if (user_input):
  for x in criterion:
    if x == "Translation":
      input_trans = translator.translate(user_input, src = working_lang, dest = trans_lang)
      st.subheader('Translation:')
      st.write(input_trans.text)
    else:
      pass

    if x == "Pronunciation":
      tts = gTTS(text = user_input, lang = working_lang)
      tts.save('user_audio.mp3')

      st.subheader("Pronunciation:")
      gramm_info = parser.fetch(user_input, working_lang2)
      st.write(gramm_info[0]['pronunciations']['text'][0])
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)
    else:
      pass

    #if x == "Same-Language Definition":
    if x == "Grammatical Information (Conjugations/Declensions)":
      gramm_info = parser.fetch(user_input, working_lang2)
      st.subheader('Grammatical Information:')
      st.write(gramm_info[0]['definitions'][0]['text'][0])
    else:
      pass

    if x == "Etymology":
      ety_info = parser.fetch(user_input, working_lang2)
      st.subheader('Etymology:')
      st.write(ety_info[0]['etymology'])
    else:
      pass
    
    if x == "Example, i.e. Word in Context":
      ex_info = parser.fetch(user_input, working_lang2)
      st.subheader('Example:')
      st.write(ex_info[0]['definitions'][0]['examples'][0])
    else:
      pass

    if x == "All":
      #Translator
      input_trans = translator.translate(user_input, src = working_lang, dest = trans_lang)
      st.subheader('Translation:')
      st.write('Translation:', input_trans.text)

      #Pronunciation
      tts = gTTS(text = input_trans.text, lang = trans_lang2)
      tts.save('user_audio.mp3')

      st.subheader("Pronunciation:")
      gramm_info = parser.fetch(input_trans.text, trans_lang2)
      st.write(gramm_info[0]['pronunciations']['text'][0])
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

      #Same-Language Definition:

      #Grammatical Information:
      gramm_info = parser.fetch(user_input, working_lang2)
      st.subheader('Grammatical Information:')
      st.write(gramm_info[0]['definitions'][0]['text'][0])

      #Etymology:
      ety_info = parser.fetch(user_input, working_lang2)
      st.subheader('Etymology:')
      st.write(ety_info[0]['etymology'])
      
      #Example, i.e. Word in Context:
      ex_info = parser.fetch(user_input, working_lang2)
      st.subheader('Example:')
      st.write(ex_info[0]['definitions'][0]['examples'][0])
      
    else:
      pass
   

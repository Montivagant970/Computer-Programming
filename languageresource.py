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
st.title("Multilingual Learning Reference")

criterion = st.multiselect("Let's get started! Which resources do you need?", ("Translation", "Pronunciation", "Definition", "Etymology", "Grammatical Information, i.e. Conjugations/Declensions/Gender", "Example, i.e. Word in Context", "All"), default=None)
if criterion:
  for x in criterion:
    if x == "All":
      st.caption("TIP: if you selected 'All,' please deselect all other options, as they are superfluous.")
else:
  pass

if criterion:
  lang_option = st.selectbox("Please enter your Working Language?:", lang_options.values())
  st.caption("TIP: your Working Language is the language of the words you will be inserting into the program. For example, if I want to translate the word 'Hund,' then the Working Language is 'German.'")

if lang_option:
  st.header('PLEASE ENTER A WORD:')
  user_input = st.text_input('TIP: only German nouns should be capitalized; all other words and languages should be written in lower case.')

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

#Program:
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
      try:
        st.write(gramm_info[0]['pronunciations']['text'][0])
      except:
        st.write('No IPA transcription is available for this word.')
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)
    else:
      pass

    if x == "Definition":
      def_info = parser.fetch(user_input, working_lang2)
      st.subheader('Definition:')
      try:
        st.write(def_info[0]['definitions'][0]['text'][1:])
      except:
        st.write('No definition is available for this word.')
    else:
      pass
    
    if x == "Grammatical Information, i.e. Conjugations/Declensions/Gender":
      gramm_info = parser.fetch(user_input, working_lang2)
      st.subheader('Grammatical Information:')
      try:
        st.write(gramm_info[0]['definitions'][0]['text'][0])
      except:
        st.write('No grammatical information is available for this word.')
    else:
      pass

    if x == "Etymology":
      ety_info = parser.fetch(user_input, working_lang2)
      st.subheader('Etymology:')
      try:
        st.write(ety_info[0]['etymology'])
      except:
        st.write('No etymological information is available for this word.')
    else:
      pass
    
    if x == "Example, i.e. Word in Context":
      ex_info = parser.fetch(user_input, working_lang2)
      st.subheader('Example:')
      try:
        st.write(ex_info[0]['definitions'][0]['examples'][0])
      except:
        st.write('No example is available for this word.')
    else:
      pass

    if x == "All":
      #Translator:
      input_trans = translator.translate(user_input, src = working_lang, dest = trans_lang)
      st.subheader('Translation:')
      st.write('Translation:', input_trans.text)
      
      #Pronunciation:
      tts = gTTS(text = user_input, lang = working_lang)
      tts.save('user_audio.mp3')

      st.subheader("Pronunciation:")
      all_info = parser.fetch(user_input, working_lang2)
      try:
        st.write(all_info[0]['pronunciations']['text'][0])
      except:
        st.write('No IPA transcription is available for this word.')
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

      #Definition:
      st.subheader('Definition:')
      try:
        st.write(all_info[0]['definitions'][0]['text'][1:])
      except:
        st.write('No definition is available for this word.')
      
      #Grammatical Information:
      st.subheader('Grammatical Information:')
      try:
        st.write(all_info[0]['definitions'][0]['text'][0])
      except:
        st.write('No grammatical information is available for this word.')
                 
      #Etymology:
      st.subheader('Etymology:')
      try:
        st.write(all_info[0]['etymology'])
      except:
        st.write('No etymological information is available for this word.')
      
      #Example, i.e. Word in Context:
      st.subheader('Example:')
      try:
        st.write(all_info[0]['definitions'][0]['examples'][0])
      except:
        st.write('No examples are available for this word.')
      
    else:
      pass
   

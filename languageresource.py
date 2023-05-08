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

#starter material
st.title("Speed Reference")

criterion = st.multiselect("Which resources do you need?", ("Translation", "Pronunciation", "Same-Language Definition", "Grammatical Information (Conjugations/Declensions)", "Etymology", "All"), default=None)
option = st.selectbox("Please, select a your working language:", lang_options.values())
st.caption("Your working language is the language of the words you will be writing into the program. For example, if I want to translate the word 'Hund', then the working language is 'German'.")

st.header('PLEASE ENTER A WORD:')
user_input = st.text_input('')

#Setting Languages:
if option:
  key = [k for k, v in lang_options.items() if v == option]
  choosen_option = key[0]
st.write(working_lang)

if (criterion):
  if criterion == "Translation" or "All":
    dest_lang = st.text_input('Into which language would you like to translate?:')
    dest_lang = dest_lang.lower()
    if dest_lang == 'german' or 'deutsch':
      dest_lang_trans = 'de'
    elif y == 'italian' or 'italiano':
      dest_lang_trans = 'it'
    elif y == 'english':
      dest_lang_trans = 'en'
    else:
      pass

#url_lang_info = 'https://api.dictionaryapi.dev/api/v2/entries/' + dest_lang + '/' + user_input
#lang_info_resp = requests.get(url_lang_info)
#json.loads(lang_info_resp.text)

#TO ADD SPEECH TO TEXT 

if (user_input):
  for x in criterion:
    if x == "Translation":
      input_trans = translator.translate(user_input, src = source_lang_trans, dest = dest_lang_trans)
      st.subheader('Translation:')
      st.write(input_trans.text)

    if x == "Pronunciation":
      tts = gTTS(text = user_input, lang = working_lang)
      tts.save('user_audio.mp3')

      st.subheader("Pronunciation:")
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

    #if x == "Same-Language Definition":
    if x == "Grammatical Information (Conjugations/Declensions)":
      gramm_info = parser.fetch(user_input, source_lang)
      st.subheader('Grammatical Information:')
      st.write(gramm_info[0]['definitions'][0]['text'][0])

    if x == "Etymology":
      ety_info = parser.fetch(user_input, source_lang)
      st.subheader('Etymology:')
      st.write(ety_info[0]['etymology'])

    if x == "All":
      #Translator
      input_trans = translator.translate(user_input, src = source_lang_trans, dest = dest_lang_trans)
      st.subheader('Translation:')
      st.write('Translation:', input_trans.text)

      #Pronunciation
      tts = gTTS(text = input_trans.text, lang = source_lang_trans)
      tts.save('user_audio.mp3')

      st.subheader("Pronunciation:")
      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

      #Same-Language Definition:

      #Grammatical Information:
      gramm_info = parser.fetch(user_input, source_lang)
      st.subheader('Grammatical Information:')
      st.write(gramm_info[0]['definitions'][0]['text'][0])

      #Etymology:
      ety_info = parser.fetch(user_input, source_lang)
      st.subheader('Etymology:')
      st.write(ety_info[0]['etymology'])

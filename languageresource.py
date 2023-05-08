import streamlit as st
import json, requests
from googletrans import Translator
from gtts import gTTS
from wiktionaryparser import WiktionaryParser

#tools:
translator = Translator()
parser = WiktionaryParser()

#starter material
st.title("Speed Reference")

criterion = st.multiselect("Which resources do you need?", ("Translation", "Pronunciation", "Same-Language Definition", "Grammatical Information (Conjugations/Declensions)", "Etymology", "All"), default=None)

st.header('PLEASE ENTER A WORD:')
user_input = st.text_input('')

#Setting Languages:
if (user_input):
  source_lang = st.text_input('What language is the source material?:')
  source_lang = source_lang.lower()
  if (source_lang):
    if source_lang == 'german' or 'deutsch' or 'tedesco':
      source_lang_trans = 'de'
    elif source_lang == 'italian' or 'italiano' or 'italienisch':
      source_lang_trans = 'it'
    elif source_lang == 'english' or 'englisch' or 'inglese':
      source_lang_trans = 'en'
    else:
      st.write("Your language is not available at this time.")
  else:
    pass
else:
  pass

if (criterion):
  if criterion == "Translation" or "All":
    dest_lang = st.text_input('Into which language would you like to translate?:')
    dest_lang = dest_lang.lower()
    if (dest_lang):
      for y in dest_lang:
        if y == 'german' or 'deutsch':
          dest_lang_trans = 'de'
        elif y == 'italian' or 'italiano':
          dest_lang_trans = 'it'
        elif y == 'english':
          dest_lang_trans = 'en'

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
      tts = gTTS(text = user_input, lang = source_lang_trans)
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

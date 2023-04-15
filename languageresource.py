import streamlit as st
from googletrans import Translator
from gtts import gTTS 
translator = Translator()

st.header("Speed Reference")

criterion = st.multiselect("Which resources do you need?", ("Translation", "Pronunciation", "Same-Language Definition", "Conjugations/Declensions", "Etymology", "All"), default=None)

source_lang = st.text_input('Translate from: (de - German, it - Italian, en - English')
dest_lang = st.text_input('Translate into: (de - German, it - Italian, en - English')

st.text('PLEASE ENTER A WORD:')
user_input = st.text_input('')
#TO ADD SPEECH TO TEXT 

if (user_input):
  for x in criterion:
    if x == "Translation":
      input_trans = translator.translate(user_input, src = source_lang, dest = dest_lang)
      st.write('Translation:', input_trans.text)

    if x == "Pronunciation":
      input_trans = translator.translate(user_input, src = source_lang, dest = dest_lang)

      tts = gTTS(text = input_trans.text, lang = dest_lang)
      tts.save('user_audio.mp3')

      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

    if x == "Same-Language Definition":
    if x == "Conjugations/Declensions":
    if x == "Etymology":
    if x == "All":
      #Translator
      input_trans = translator.translate(user_input, src = source_lang, dest = dest_lang)
      st.write('Translation:', input_trans.text)

      #Pronunciation
      tts = gTTS(text = input_trans.text, lang = dest_lang)
      tts.save('user_audio.mp3')

      st.audio(data = 'user_audio.mp3', format = 'audio/mp3', start_time=0)

      #Cont. here

from gtts import gTTS 
from googletrans import Translator
import streamlit as st
translator = Translator()

st.header("Here's a translator and text-to-speech all in one app!")

text_input = st.text_input('Write some text to be translated and made into an audio:')
lang_code = st.text_input('Enter a two letter language code for translation (en - English, de - Deutsch, it - italiano):')

if (text_input and lang_code):
  text_trans = translator.translate(text_input, dest=lang_code)

  tts1=gTTS(text=text_trans.text, lang=lang_code)
  tts1.save('user_audio.mp3')

  st.audio(data='user_audio.mp3', format='audio/mp3', start_time=0)

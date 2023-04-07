import streamlit as st
from googletrans import Translator
translator = Translator()

st.header("Welcome to an awful online translator!")
word = st.text_input('Please enter a word:')
targ_lang = st.text_input('Enter a language or a two letter language code for translation:')
if (word and targ_lang):
  lang_detect = translator.translate(word, dest=targ_lang)
  st.write('The translation is:', lang_detect.text)

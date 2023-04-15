import streamlit as st
from googletrans import Translator
translator = Translator()

st.header("Speed Reference")

criterion = st.multiselect("Which resources do you need?", ("Translation", "Pronunciation", "Same Language Definition", "Conjugations/Declinations", "Etymology", "All"), default=None)

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

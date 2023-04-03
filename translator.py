import streamlit as st
from googletrans import Translator
translator = Translator()

st.header("Welcome to an awful online translator!")

loop_var = st.text_input("Would you like me to translate something for you?")

while loop_var != 'Quit':
    word = st.text_input('Please enter a word:')
    targ_lang = st.text_input('Enter a two letter language code for translation (en - English, de - Deutsch, it - italiano):')
    lang_detect = translator.translate(word, dest=targ_lang)
    st.write('The translation is:', lang_detect.text)
    loop_var = st.text_input("Would you like me to translate something else for you ('Quit' to exit):")

print("k bye gurlie")

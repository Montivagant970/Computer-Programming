from gtts import gTTS
import IPython.display as ipd 
from googletrans import Translator
import streamlit as st
translator = Translator()

text_input = st.text_input('Write some text to be translated and made into an audio:')
lang_code = st.text_input('Enter a two letter language code for translation (en - English, de - Deutsch, it - italiano):')

text_trans = translator.translate(text_input, dest=lang_code)

tts1=gTTS(text=text_trans.text, lang=lang_code)
tts1.save('user_audio.mp3')

st.audio('user_audio.mp3',autoplay=False))

import streamlit as st
st.header("hello world")
st.text("from Bressanone")

title = st.text_input("Please insert a movie title:", '')
st.write('The current movie title is', title)

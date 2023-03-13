import streamlit as st
st.header("hello world")
st.text("from Bressanone")

title = st.text_input("Please insert a movie title:", '')
st.write('The current movie title is:', title)

import streamlit as st
genre = st.radio("What's your favorite movie genre?",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
 else:
     st.write("You didn't select comedy.")

import streamlit as st
st.header("hello world")
st.text("from Bressanone")

import json, requests 
import streamlit as st
APIkey = 'b0dc5ff479faf43dff849169f51ad2b0'
location = st.text_input('Write a city name:', '')
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + APIkey + '&units=metric'
response = requests.get(url)  
weatherData = json.loads(response.text)
st.write('Today\'s high is:', ['main']['temp_max'], 'and today\'s low is:', ['main']['temp_min'], '.')

title = st.text_input("Please insert a movie title:", '')
st.write('The current movie title is:', title)

import streamlit as st
genre = st.radio("What's your favorite movie genre?",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
     st.write('You selected comedy.')
 else:
     st.write("You didn't select comedy.")

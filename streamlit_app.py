import streamlit as st
import pandas as pd

st.title('My Parents New Health Diner')
st.header('Breakfest Menu')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinish & Rocket Smoothie')
st.text('🐔 Hard-bolied Free-range Eggs')
st.text('🥑🍞 Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
st.dataframe(my_fruit_list)

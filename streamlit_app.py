import streamlit as st
import pandas as pd
import requests
import snowflake.connector

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
fruit_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ["Avocado", "Strawberries"])
fruits_to_show = my_fruit_list.loc[fruit_selected]
st.dataframe(fruits_to_show)


st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# puts data into a pandas data frame 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# prints the dataframe
st.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()

st.header("The Fruit load list contains:")
st.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = st.text_input('What fruit would you liketo add','Kiwi')

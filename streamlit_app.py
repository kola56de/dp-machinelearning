import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learing model')
with st.expander ('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/kola56de/dp-machinelearning/refs/heads/master/penguins_cleaned.csv')
  df
  
  st.write('**X**')
  X = df.drop('species', axis = 1)
  X

  st.write('**Y**')
  Y = df.species
  Y

with st.expander ('Data Visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color = 'species')

# Data Preparation
with st.sidebar:
  # "island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g","sex
  st.header('Input Features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgerson'))
  gender = st.selectbox('Gender', ('Male', 'Female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9 )

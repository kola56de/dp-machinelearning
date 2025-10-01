import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learing model')
with st.expander ('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/kola56de/dp-machinelearning/refs/heads/master/penguins_cleaned.csv')
  df

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#money = pd.read_csv("money_data7.csv")

st.title(':polar_bear: This is :orange[july-ya] page :polar_bear:')
#st.sidebar.success("Select a demo above.")

def plotting_demo():
  
  #uploaded_file = st.file_uploader("Choose a file")
  
  #money = pd.read_csv(uploaded_file)
  money = pd.read_csv("money_data7.csv")
  
  option = st.selectbox('How would you like to choice year ?', ('2020', '2021', '2022'))
  option2 = int(option)
  st.write('You selected:', option)

  money = money[:] [money['A_YEAR']== option2]

  fig, ax = plt.subplots(2,2, figsize=(12,8))

  plt.subplot(221)
  plt.plot( list(money['A_MONTH']), list(money['A_RATE']), color = 'salmon', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("America Rate", size = 15, color = 'salmon')

  plt.subplot(222)
  plt.plot( list(money['A_MONTH']), list(money['K_RATE']), color = 'lightskyblue', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("Korea Rate", size = 15, color = 'lightskyblue')

  plt.subplot(223)
  plt.plot( list(money['A_MONTH']), list(money['KOSPI']), color = 'lightgreen', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("KOSPI", size = 15, color = 'lightgreen')

  plt.subplot(224)
  plt.plot( list(money['A_MONTH']), list(money['HOUSE_PRICE']), color = 'lightpink', marker = 'o' )
  plt.xticks(tuple(money['A_MONTH']))
  plt.title("House Price", size = 15, color = 'lightpink')

#  st.snow()
  st.pyplot(fig)
  st.dataframe(money)

with st.form(key = 'Form1'):
  with st.sidebar:
    select_chart = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie', 'box', 'histogram', 'corr', 'word cloud'))

if select_chart == 'line':
  plotting_demo()
#  try:
#    plotting_demo()
#  except:
#    pass

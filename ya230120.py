import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


money = pd.read_csv("money_data7.csv")

st.title(':polar_bear: This is :orange[july-ya] page :polar_bear:')
st.sidebar.success("Select a demo above.")

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

st.pyplot(fig)
st.dataframe(money)

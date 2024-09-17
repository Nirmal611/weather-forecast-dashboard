import streamlit as st
import plotly.express as pe
import pandas as pd
from backend import get_data

st.title('Weather Forecast Dashboard')

place = st.text_input(label='Enter a place' , key = 'place' , placeholder='Example- Chennai')
days = st.slider(label = 'Select the number of days ' , value = 1 , min_value=1 , max_value=5 , key = 'days')
data_to_display =  st.selectbox(label='Select data to view ' , options=['Temperature' , 'Sky'] , key = 'data')

if place :
    if days == 1 :
        s=''
    else :
        s='s'
    st.subheader(f"{data_to_display} for the next {days} day{s} in {place.title()}")
    temperature,dates=get_data(place=place,day=days)

    fig = pe.line(x=dates, y=temperature, labels=('Dates' , 'Temperature'))
    st.plotly_chart(fig)


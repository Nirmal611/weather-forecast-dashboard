import streamlit as st

st.title('Weather Forecast Dashboard')

place = st.text_input(label='Enter a place' , key = 'place' , placeholder='Example- Chennai')
days = st.slider(label = 'Select the number of days ' , value = 1 , min_value=1 , max_value=5 , key = 'days')
data_to_display =  st.selectbox(label='Select data to view ' , options=['Temperature' , 'Sky'] , key = 'data')

if place :
    if days == 1 :
        s=''
    else :
        s='s'
    st.subheader(f"{data_to_display} for the next {days} day{s} in {place}")
    st.write(days,place,data_to_display)
import streamlit as st
import plotly.express as pe
from backend import get_data

api_key = st.secrets['API_KEY']

st.title('Weather Forecast Dashboard')

place = st.text_input(label='Enter a place' , key = 'place',
                      placeholder='Example- Chennai' , value='Tokyo')
days = st.slider(label = 'Select the number of days ',
                 value = 1 , min_value=1 , max_value=5 , key = 'days')
data_to_display =  st.selectbox(label='Select data to view ',
                                options=['Temperature' , 'Sky'] , key = 'data')
try:
    temperature,dates,sky = get_data(place=place,day=days,api_key)

    if days == 1:
        s = ''
    else:
        s = 's'
    st.subheader(f"{data_to_display} for the next {days} day{s} in {place.title()}")
    if data_to_display == 'Temperature':
        fig = pe.line(x=dates, y=temperature, labels={'x': 'Date', 'y': 'Temperature'})
        st.plotly_chart(fig)

    if data_to_display == 'Sky':

        images = {'Clouds': 'cloudimages/clouds.png', 'Rain':'cloudimages/rain.png',
                  'Clear': 'cloudimages/clear.png', 'Snow': 'cloudimages/snow.png'}
        image_paths = [images[condition] for condition in sky]
        st.image(image_paths, width=150 , caption = dates)

except KeyError:
    st.warning("Enter a valid city name ")
import streamlit as st
import pandas as pd
import numpy as np
import csv

DATA_URL = (
    "C:\\Users\HP\Desktop\Data Science Web App\Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Vehicle Collisions In NYC")

st.markdown("#### This application is Streamlit dashboard that can be used to display Motor Vehicle Collisions in NYC") #here '##' are used to change the font size, more the '#' smaller will be font size

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)


if st.checkbox("Show Raw Data", False):
    st.subheader('Raw Data')
    st.write(data)

    # "C:\Users\HP\Desktop\Data Science Web App\Motor_Vehicle_Collisions_-_Crashes.csv"
st.subheader('Raw Data')
st.write(data)


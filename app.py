import streamlit as st
import pandas as pd
import numpy as np
import csv
import itertools
import functools
import operator
import pydeck as pdk

DATA_URL = (
    "C:\\Users\HP\Desktop\Data Science Web App\Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Vehicle Collisions In NYC")

# here '##' are used to change the font size, more the '#' smaller will be font size
st.markdown("#### This application is Streamlit dashboard that can be used to display Motor Vehicle Collisions in NYC")


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[
                       ['CRASH_DATE', 'CRASH_TIME']])
    data.dropna(subset=['LATITUDE', 'LONGITUDE'], inplace=True)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data


data = load_data(100000)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider(
    "Number of persons injured in vehicle collisions ", 0, 19)
st.map(data.query("injured_persons >= @injured_people")
       [["latitude", "longitude"]].dropna(how="any"))


st.header("How Many collisions occured during a given time of day?")
hour = st.selectbox("Hour to look at", range(0, 24), 1)
data = data[data['date/time'].dt.hour == hour]


st.markdown("Vehicle collisions between %i:00 and %i:00" %
            (hour, (hour+1) % 24))
midpoint = (np.average(data['latitude']), np.average(data['longitude']))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
))

# if st.checkbox("Show Raw Data", False):
#     st.subheader('Raw Data')
#     st.write(data)

# "C:\Users\HP\Desktop\Data Science Web App\Motor_Vehicle_Collisions_-_Crashes.csv"
st.subheader('Raw Data')
st.write(data)

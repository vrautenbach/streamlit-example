from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("This is my first sentence")
col_names = ["Airline ID", "Name","Alias","IATA","ICAO","Callsign","Country","Active"]
routes = pd.read_csv('airlines.dat', names = col_names)
routes

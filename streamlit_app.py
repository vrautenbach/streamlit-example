from collections import namedtuple
import altair as alt
import math
import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
import streamlit as st

st.write("This is my first sentence")
col_names = ["Airline ID", "Name","Alias","IATA","ICAO","Callsign","Country","Active"]
airlines = pd.read_csv('airlines.dat', names = col_names)
airlines
groupedAirlines = airlines.groupby("Country")["Active"== Y].count()
groupedAirlines

airport_col = ['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'latitude','longitude', 'Altitude', 'Time Zone', 'DST', 'Tz db time', 'Type', 'Source']
airports = pd.read_csv('airports.dat', sep =",", names=airport_col)
airports
grouped = airports.groupby('Country')
output= grouped.aggregate({'Name':'count'})
output


latitude = airports['latitude']
longitude = airports['longitude']
airport_locations = pd.DataFrame(latitude).join(longitude)
airport_locations


map = st.map(airport_locations)
map

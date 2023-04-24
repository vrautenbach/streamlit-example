from collections import namedtuple
import altair as alt
import math
import pandas as pd
import geopandas as gpd 
from shapely.geometry import Point
import streamlit as st

st.write("This is my first sentence")
col_names = ["Airline ID", "Name","Alias","IATA","ICAO","Callsign","Country","Active Airlines"]
airlines = pd.read_csv('airlines.dat', names = col_names)
groupedAirlines = airlines.groupby("Country")["Active Airlines"].count().reset_index()
st.bar_chart(groupedAirlines, x="Country", y="Active Airlines")

non_zero_filter = airlines['Active Airlines'] != 0
ActiveAirlines = airlines[non_zero_filter]
# Get all those data points
highest_airlines = ActiveAirlines.max()
lowest_airlines = ActiveAirlines.min()
avg_airlines = ActiveAirlines.mean()

# Print the highest 
highest_airlines

#Print the lowest MPG
print('')
print(':::LOWEST ActiveAirlines:::')
print(lowest_airlines)

# Print the AVG MPG
print('')
print(':::AVERAGE ActiveAirlines:::')
print(avg_airlines)

airport_col = ['Airport ID', 'Number of airports', 'City', 'Country', 'IATA', 'ICAO', 'latitude','longitude', 'Altitude', 'Time Zone', 'DST', 'Tz db time', 'Type', 'Source']
airports = pd.read_csv('airports.dat', sep =",", names=airport_col)
grouped = airports.groupby('Country')
output= grouped.aggregate({'Number of airports':'count'}).reset_index()
st.bar_chart(output, x="Country", y="Number of airports")

latitude = airports['latitude']
longitude = airports['longitude']
airport_locations = pd.DataFrame(latitude).join(longitude)
airport_locations


map = st.map(airport_locations)
map

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("This is my first sentence")
routes = pd.read_csv('airlines.dat')
routes

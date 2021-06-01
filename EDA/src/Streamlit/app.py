# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os
from utils.stream_config import create_sliders, draw_map
from utils.dataframes import get_data_from_df, load_csv_df, load_csv_for_map

path = dir(os.getcwd())

path = os.path.dirname(__file__)
df = None

menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Link to tableau dashboard", "Download json files"])

if menu == 'Welcome':
    st.title("Welcome to Daniel Walkers EDA!")
    st.write('This project is to review popular betting patterns and discover the basic errors made by most people when it comes to sports betting')
    st.write('To interact with the data, please go to the link in the side menu.')

if menu == "Link to tableau dashboard":
    st.title("https://public.tableau.com/profile/api/publish/ComparisonLeaguesWINStraight/Story1")

if menu == "Download json files":
    st.write("To access json/csv files with the data used in the project, go to (localhost:6060/greet)")
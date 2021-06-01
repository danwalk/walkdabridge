# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import os
from utils.stream_config import create_sliders, draw_map
from utils.dataframes import get_data_from_df, load_csv_df, load_csv_for_map

path = os.path.dirname(__file__)
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Welcome", "Link to tableau dashboard", "Download json files"])

if menu == 'Welcome':
    st.title("Welcome to Daniel Walkers EDA!")
    st.write('This project is to review popular betting patterns and discover the basic errors made by most people when it comes to sports betting')
    st.write('To see more information and a dashboard containing the information as seen below, go to the link in the side menu.')
    st.image('./header.png')

 

if menu == "Graphs":
    slider_csv_graph = st.sidebar.file_uploader("Select CSV", type=['csv'])
    new_df_path_graph = None
    df_slider_graph = None
    df_slider_graph_copy = None
    hidden = None
    c_df_3 = None
    # show grahps

    if st.button('Show Graph'):
        df_3 = pd.DataFrame(
        np.random.randn(200, 3),
        columns=['a', 'b', 'c'])

        c_df_3 = alt.Chart(df_3).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
        st.write(c_df_3)
    if type(slider_csv_graph) != type(None):
        columns = [None,]
        df_slider_graph = load_csv_df(slider_csv_graph)
        st.subheader('DF:')
        st.bar_chart(df_slider_graph)
        tamano = st.sidebar.select_slider("Number of values",
                                      options=range(0, df_slider_graph.shape[0]),
                                      value=100.0)
        columns.extend(list(df_slider_graph.columns))
    
        column_choose = st.sidebar.selectbox(
            'Select a column:',
            options=columns)
        if column_choose != None:
            st.bar_chart(df_slider_graph.head(tamano)[column_choose])

if menu == "Map":
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)
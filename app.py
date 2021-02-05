import warnings

import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit import caching
from streamlit_folium import folium_static

import app_body as body

warnings.filterwarnings('ignore')

st.title('Spotify Data Analysis')

## Side Bar Information
image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)
st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort VI</h1>", unsafe_allow_html=True)

## Create Select Box and options
add_selectbox = st.sidebar.radio(
    "",
    ("Introduction and Business Question", "Data Information", "List of Tools", "Data Cleaning", 
    "Exploratory Data Analysis", "Song Genre Classification", "Recommendation Engine", 
    "Business Strategies", "Contributors")
)


if add_selectbox == 'Introduction and Business Question':
    body.introduction()

elif add_selectbox == 'Data Information':
    body.dataset()

elif add_selectbox == 'List of Tools':
    body.tools()

elif add_selectbox == 'Data Cleaning':
    body.cleaning()

elif add_selectbox == 'Exploratory Data Analysis':
    body.eda()

elif add_selectbox == 'Song Genre Classification':
    body.genre_classification()

elif add_selectbox == 'Recommendation Engine':
    body.recommenderengine()

elif add_selectbox == 'Business Strategies':
    body.conclusion()

elif add_selectbox == 'Contributors':
    body.contributors()
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import seaborn as sns
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
from streamlit import caching

def introduction():
    image = Image.open('logo/nyoy_pic.PNG').convert('RGB')
    st.image(image, caption='', width=800, height=300)
    st.write('')
    st.header('Tuloy Pa Rin')
    st.subheader('Client: Nyoy Volante')
    st.write('Nyoy Volante is a Filipino singer and songwriter, initially dubbed as "The Prince of Acoustic Pop" turned "The King of Philippine Acoustic Pop." Nyoy began his music career in the early 2000s, releasing hit songs such as Nasaan Ka Na and Someday. His song Tuloy Pa Rin, released in 2012, even landed in the Top 200 PH Daily Charts on Spotify.')
    st.write('Nyoy Volante wants to jumpstart his 2021 music career and wishes to land a spot in the Spotify PH Top Daily 200 once more. What should his next move be this 2021?')
    st.subheader('Business Objectives')
    st.write('To help Nyoy land his second spot in the coveted Top Daily 200, the following objectives must be met:')  
    st.write('1. Identify popular music genres in the Philippines.')
    st.write('2. Determine genres Nyoy can venture into.')
    st.write('3. Provide a list of potential artirts Nyoy can collaborate with.')
 
def dataset():
    st.write('')
    st.header('Spotify Data Set')
    
    st.subheader('Top 200 Daily Charts:')
    st.write('<b>Date Range</b>: January 1, 2017 - December 31, 2020', unsafe_allow_html=True)

    dailychart = {
                      'Column Name': ['date', 'position', 'track_id', 'track_name', 'artist', 'streams'], 
                      'Description': ['Daily Chart Date', 'Song Charting Position', 'Song Unique Identifier', 'Song Name', 'Name of Singer', 'Total Number of Daily Streams'],
                      'Sample Data': ['2020-12-31','200','2S80c51YXgJQhkhX603fMA','Prinsesa','6cyclemind','17516']
			}
    st.table(dailychart)

    st.subheader('Track Audio Features:')

    audiofeatures = {
                      'Column Name': ['duration_ms', 'key', 'mode', 'acousticness', 'danceability', 'energy','instrumentalness','liveness','loudness','speechiness','valence','tempo'], 
                      'Desription': ['The duration of the track in milliseconds.','The key the track is in.','Indicates the modality (major or minor) of a track, the type of scale from which it is melodic.',
				'A confidence measure from 0.0 to 1.0 of whether the track is acoustic.','Describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.',
				'A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.','Predicts whether a track contains no vocals.',
				'Detects the presence of an audience in the recording.','The overall loudness of a track in decibels (dB).','Detects the presence of spoken words in a track.','A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track.',
				'The overall estimated tempo of a track in beats per minute (BPM).']
			}
    st.table(audiofeatures)

    st.subheader('Playlist Data:')

    playlistdata = {
                      'Column Name': ['playlist_id','playlist_name','playlist_total_tracks','owner_id','owner_name','total_followers'],
                     'Description': ['Playlist Unique Identification','Name of the Playlist','Total Number of Songs in the Playlist','Playlist Owner Unique Identification','Playlist Owner','Total Followers of the Playlist']
			}
    st.table(playlistdata)


def tools():
    st.write('')
    st.header('List of Tools')
    st.write('-----------------------------------------------------------------------') 
    image = Image.open('logo/Spotify.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/jupyter.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/pandas.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/heroku.jpg').convert('RGB')
    st.image(image, caption='', width=150, height=50)
    image = Image.open('logo/streamlit.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/github.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/scipy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/seaborn.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/matplotlib.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)
    image = Image.open('logo/numpy.png').convert('RGB')
    st.image(image, caption='', width=300, height=150)

def cleaning():
    st.write('')
    st.header('Data Cleaning')
    st.write('-----------------------------------------------------------------------') 
    st.write('1. Merge Top 200 Daily Charts from 2017 - 2020 with the corresponding Artists and Tracks Data.')
    st.write('2. Add the Genre Classification obtained from the Playlist Data in the dataset above.')
    st.write('3. Drop duplicated data based on track_id.')

def eda():
    caching.clear_cache()
    st.write('')
    st.header('Exploratory Data Analysis')
    st.write('-----------------------------------------------------------------------') 
    st.write('<b>Popular Genres in the Philippines</b>', unsafe_allow_html=True)
    
    

def genre_classification():
    caching.clear_cache()
    st.write('')
    st.header('Song Genre Classification')
    st.write('-----------------------------------------------------------------------') 
    st.write('')
    st.write('Tracks obtained from various playlists of different genres were trained for genre classification.')
    st.subheader('Chosen Genres:')
    st.write('- Acoustic, Classical, Reggae, Rock, R&B') 
    st.subheader('Chosen Features:')
    st.write('- Danceability, Energy, Key, Loudness, Mode, Speechiness, Acousticness, Instrumentalness, Valence, Tempo')
    st.subheader('Selected Model')
    st.write('- XGBoost')
    st.write('- Accuracy: 77.93%')
    st.subheader('Results of other models')
    option = st.selectbox('Select Model',('kNN','SVM Linear','SVM Polynomial','SVM RBF','Decision Trees','Random Forest','XGBoost'))
    st.write('Here are the results obtained from the', option, 'model.')
    if option == 'kNN':
        st.write('')
    elif option == 'SVM Linear':
        st.write('')
    elif option == 'SVM Polynomial':
        st.write('')
    elif option == 'SVM RBF':
        st.write('')
    elif option == 'Decision Trees':
        st.write('')
    elif option == 'Random Forest':
        st.write('')
    elif option == 'XGBoost':
        st.write('')
   

def recommenderengine():
    caching.clear_cache()
    st.write('')
    st.header('Recommended Artist Collaborations')
    st.write('-----------------------------------------------------------------------') 
    st.write('')
    st.subheader("Genre Classification of Nyoy's songs")
    
    nyoygenre = {
                      'Genre': ['Acoustic','Rock','R&B'],
                     'Number of Songs': ['','','']
                       }
    st.table(nyoygenre)
    st.subheader('Top artists for Nyoy to collaborate with.')
    option = st.selectbox('Select genre',('Acoustic','Rock','R&B'))
    st.write('Under the genre ', option, ', it is highly recommended for Nyoy to collaborate with the following artists.')
    if option == 'Acoustic':
        st.write('Acoustic')
    elif option == 'Rock':
        st.write('Rock')
    elif option == 'R&B':
        st.write('R&B')

def conclusion():
    caching.clear_cache()
    st.write('')
    st.header('Recommended Business Strategies')
    st.write('-----------------------------------------------------------------------') 
    st.write('')   

def contributors():
    caching.clear_cache()
    st.write('')
    st.header('Contributors')
    st.write('-----------------------------------------------------------------------') 
    st.write('')
    
    
    st.write('Emerson Fili Chua - Mentor')
    st.write('Generoso Roberto')
    st.write('Kaye Janelle Yao')
    st.write('Rodel Arenas')
    st.write('Tyron Rex Frago')
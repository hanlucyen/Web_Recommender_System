"""
Anime Recommendation System with MyAnimeList dataset 
By Nguyen Thi Huynh Nhu
Date: 08-03-2024
"""
import pickle
import streamlit as st
import numpy as np
from sklearn.neighbors import NearestNeighbors

from PIL import Image 



st.set_page_config(page_title='Anime RS - NTHN', page_icon='🎞', layout="centered", initial_sidebar_state="auto", menu_items=None)



st.image(Image.open('C:/Users/Asus/Desktop/08032024/bear.png'))




st.header('Anime Recommendation System Using Machine Learning')
model = pickle.load(open('interface/model.pkl','rb'))
anime_names = pickle.load(open('interface/anime_names.pkl','rb'))
final_rating = pickle.load(open('interface/final_rating.pkl','rb'))
anime_pivot = pickle.load(open('interface/anime_pivot.pkl','rb'))


def fetch_poster(suggestion):
    anime_name = []
    ids_index = []
    poster_url = []

    for anime_id in suggestion:
        anime_name.append(anime_pivot.index[anime_id])

    for name in anime_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_path']
        poster_url.append(url)

    return poster_url






def recommend_anime(anime_name):
    animes_list = []
    anime_id = np.where(anime_pivot.index == anime_name)[0][0]
    distance, suggestion = model.kneighbors(anime_pivot.iloc[anime_id,:].values.reshape(1,-1), n_neighbors=11 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            animes = anime_pivot.index[suggestion[i]]
            for j in animes:
                animes_list.append(j)
    return animes_list , poster_url       



selected_animes = st.selectbox(
    "Type or select a anime from the dropdown",
    anime_names
)

if st.button('Show Recommendation'):
    recommended_animes,poster_url = recommend_anime(selected_animes)
    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(recommended_animes[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_animes[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_animes[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_animes[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_animes[5])
        st.image(poster_url[5])

    with col6:
        st.text(recommended_animes[6])
        st.image(poster_url[6])
    with col7:
        st.text(recommended_animes[7])
        st.image(poster_url[7])

    with col8:
        st.text(recommended_animes[8])
        st.image(poster_url[8])
    with col9:
        st.text(recommended_animes[9])
        st.image(poster_url[9])
    with col10:
        st.text(recommended_animes[10])
        st.image(poster_url[10])
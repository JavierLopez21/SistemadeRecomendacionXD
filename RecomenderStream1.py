import streamlit as st
import os
from data.RecomenderSystem import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
from sklearn.metrics.pairwise import euclidean_distances
import joblib
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de credenciales de Spotify
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Verificar si las credenciales están disponibles
if not client_id or not client_secret:
    st.error("❌ Las credenciales de Spotify no están configuradas. Por favor, sigue las instrucciones en el README para configurar el archivo .env.")
    st.stop()  # Detener la ejecución si las credenciales no están disponibles

# Configurar la autenticación de Spotify
try:
    credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials)
except Exception as e:
    st.error(f"❌ Error al autenticar con Spotify: {e}")
    st.stop()  # Detener la ejecución si hay un error de autenticación

# Cargar el modelo y los datos escalados
scaler = joblib.load('data/scaler.joblib')
model = joblib.load('data/modelo_mezcla_gaussiana.joblib')
scaled_df = pd.read_csv('data/data_entrenamiento_label.csv')

feats = ['danceability', 'energy', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo','mode']

# Instanciar el sistema de recomendación
n_songs = 5  # Número de canciones a recomendar
recommender = RecomenderSystem(scaler, model, scaled_df, n_songs, sp, feats)

# Configuración de Streamlit
st.set_page_config(page_title="Sistema de Recomendación de Música", page_icon="🎶")

# Título de la aplicación
st.title("Sistema de Recomendación de Música 🎶")

# Input de usuario
track_name = st.text_input("Ingrese el nombre de una canción:")
artist_name = st.text_input("Ingrese el nombre del artista:")

# Agregar imágenes atractivas
st.image("images/espoti.png", use_column_width=True)
st.image("images/IA.jpg", use_column_width=True)

if st.button("Recomendar"):
    recomendaciones = recommender.get_recomendations(track_name, artist_name)
    if len(recomendaciones) > 0:
        st.write("### Recomendaciones:")
        for track_id in recomendaciones:
            name, artist = recommender.get_track_name(track_id)
            st.write(f"**Nombre:** {name}  \n**Artista:** {artist}")
    else:
        st.write("❌ Canción no encontrada. Intente con otro nombre o artista.")

# Mensaje de pie de página
st.markdown("<footer style='text-align: center;'>Hecho con ❤️ por [Tu Nombre]</footer>", unsafe_allow_html=True)
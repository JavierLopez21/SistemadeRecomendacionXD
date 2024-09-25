# Sistema de Recomendación de Música 🎶

Bienvenido al Sistema de Recomendación de Música, una aplicación construida con Streamlit y Spotify para ofrecerte recomendaciones personalizadas de canciones basadas en tus gustos musicales.

## Descripción

Esta aplicación utiliza un modelo de mezcla gaussiana y la API de Spotify para analizar las características de las canciones y recomendarte nuevas canciones que te podrían gustar. Simplemente ingresa el nombre de una canción y el artista, y obtendrás una lista de recomendaciones.

## Características

- **Recomendaciones Personalizadas**: Basado en las características de las canciones que te gustan.
- **Interfaz Intuitiva**: Interfaz sencilla y fácil de usar gracias a Streamlit.
- **Integración con Spotify**: Utiliza la API de Spotify para obtener datos detallados de las canciones.
- **Visualmente Atractivo**: Imágenes y diseño llamativo para una mejor experiencia de usuario.

## Requisitos

- Python 3.9
- Cuenta de desarrollador de Spotify para obtener las credenciales de la API.
- Archivo `.env` con tus credenciales de Spotify:

    ```env
    SPOTIFY_CLIENT_ID=tu_spotify_client_id
    SPOTIFY_CLIENT_SECRET=tu_spotify_client_secret
    ```

## Instalacion
1.- Clona este repositorio
- git clone https://github.com/JavierLopez21/SistemadeRecomendacionXD.git
- cd SistemadeRecomendacionXD
2.- Crea un entorno virtual y activalo

- python -m venv env
- source env/bin/activate  # En Windows usa `env\Scripts\activate`

3.- Instala las dependencias
- pip install -r requirements.txt

## Uso
Ejecula la aplicacion:
- streamlit run RecomenderStream1.py

## Docker

- docker build -t recomender_app .
- docker run -p 8501:8501 --env-file .env recomender_app





# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /Recomender_App

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt ./

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 8501 para Streamlit
EXPOSE 8501

# Establece el comando para ejecutar la aplicación de Streamlit
CMD ["streamlit", "run", "RecomenderStream1.py"]

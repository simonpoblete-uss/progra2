import streamlit as st
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

def obtener_imagen_del_dia(api_key):
  url=f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
  respuesta=requests.get(url)
  datos=respuesta.json()
  return datos

st.title("Imagen del dia desde la NASA")
api_key='t4apmCnra2jnleMfw4eC8tKBsEPoPPw1dEYaFZ9i'

if st.button("Mostrar imagen del dia"):
  datos_apod=obtener_imagen_del_dia(api_key)
  if datos_apod:
    st.write(datos_apod['title'])
    st.image(datos_apod['url'],caption=datos_apod['explanation'])
  else:
    st.error('Error al obtener la imagen del dia')

import streamlit as st
import requests
import pandas as pd

st.title('mi primer dashboard modificado')
def obt(ciudad,api_key):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}'
    
    res=requests.get(url)
    return res.json()

ciudad=st.text_input('Ingrese ciudad:', 'santiago,cl')
api_key='cc4e86f910fd60d67396eb83c28f2953'
#'35aee69d9d83963d3ad8f3e1c88dc143'
if st.button('Obtener Datos Climaticos'):
    datos=obt(ciudad,api_key)
    st.write(datos)

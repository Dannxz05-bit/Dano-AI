import streamlit as st
from google import genai
import requests
from streamlit_lottie import st_lottie

# --- Configuración visual ---
st.set_page_config(page_title="Dano AI", page_icon="💠")
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- Función para cargar la esfera ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Interfaz del Reactor ---
st.title("💠 DANO AI - REACTOR UNIT")

# Animación de la esfera (Link a una esfera técnica azul)
url_esfera = "https://assets10.lottiefiles.com/packages/lf20_t3x6m5k3.json"
lottie_esfera = load_lottie_url(url_esfera)

if lottie_esfera:
    st_lottie(lottie_esfera, height=300, key="esfera")

# --- Lógica del Chat ---
# (Aquí va tu código de Gemini que ya teníamos)

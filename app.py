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

# --- Configuración de la Esfera Técnica ---
url_esfera = "https://lottie.host/7e04f02f-b472-4d2d-9477-8025219277f0/BfBV6GvzpM.json"
lottie_esfera = load_lottie_url(url_esfera)

if lottie_esfera:
    st_lottie(
        lottie_esfera, 
        speed=1, 
        reverse=False, 
        loop=True, 
        quality="high", 
        height=400, 
        key="dano_sphere"
    )
st.markdown("""
    <div style="background-color: rgba(0, 242, 255, 0.1); 
                padding: 15px; 
                border-radius: 10px; 
                border: 1px solid #00f2ff;
                text-align: center;">
        <h4 style="color: #00f2ff;">ESTADO DEL NÚCLEO: ACTIVO</h4>
        <p style="color: white; font-family: monospace;">SISTEMA ANALIZANDO CONSULTA...</p>
    </div>
""", unsafe_allow_html=True)
# --- Interfaz del Reactor ---
st.title("💠 DANO AI - REACTOR UNIT")

# Animación de la esfera (Link a una esfera técnica azul)
url_esfera = "https://assets10.lottiefiles.com/packages/lf20_t3x6m5k3.json"
lottie_esfera = load_lottie_url(url_esfera)

if lottie_esfera:
    st_lottie(lottie_esfera, height=300, key="esfera")

# --- Lógica del Chat ---
# (Aquí va tu código de Gemini que ya teníamos)

import streamlit as st
from google import genai
import requests
from streamlit_lottie import st_lottie

# --- Configuración de la Página ---
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# --- Función para cargar la esfera Lottie ---
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# --- Estilos CSS Personalizados (Diseño JARVIS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000408; color: #00f2ff; }
    h1 { color: #00f2ff; text-align: center; text-shadow: 0 0 10px #00f2ff; }
    .css-1r6slb0 { border: 2px solid #00f2ff !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Interfaz Principal ---
st.title("💠 DANO AI - REACTOR UNIT")

# Carga y muestra la esfera
url_esfera = "https://lottie.host/7e04f02f-b472-4d2d-9477-8025219277f0/BfBV6GvzpM.json"
lottie_esfera = load_lottie_url(url_esfera)

if lottie_esfera:
    st_lottie(lottie_esfera, height=350, key="dano_sphere")

# --- Configuración de la IA ---
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("Error: Configura tu GOOGLE_API_KEY en los Secrets.")
    st.stop()

# --- Lógica del Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input del Usuario
if prompt := st.chat_input("Dano AI escuchando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error("Error: Cuota temporalmente agotada. Espera unos instantes.")

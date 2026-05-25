import streamlit as st
from google import genai

# Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# Estilo para fondo oscuro y chat
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: monospace; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# Animación de partículas (Cargada directamente como video para máxima calidad)
st.markdown("""
    <div style="display: flex; justify-content: center; margin: 20px 0;">
        <video width="350" height="350" autoplay loop muted playsinline>
            <source src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqbmV0d29yayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTjJp9tZ9v2Q1O/giphy.gif" type="video/mp4">
            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqbmV0d29yayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l41lTjJp9tZ9v2Q1O/giphy.gif" width="350">
        </video>
    </div>
""", unsafe_allow_html=True)

# Lógica de la IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Dano AI escuchando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except:
            st.error("Error de sistema.")

import streamlit as st
from google import genai
import os

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. CSS Estable (Sin componentes externos)
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    .stChatMessage { border: 1px solid #00f2ff !important; background: #010a12 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Configuración de API (Verificación simple)
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Error: No se encontró GOOGLE_API_KEY en los secretos.")
    st.stop()

client = genai.Client(api_key=api_key)

# 4. Lógica de Chat
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
            # Usamos gemini-1.5-flash
            response = client.models.generate_content(
                model='gemini-1.5-flash', 
                contents=prompt
            )
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error técnico: {e}")

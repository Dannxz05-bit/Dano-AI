import streamlit as st
from google import genai
import google.generativeai as genai_v1

# 1. Configuración
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. CSS Estable
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    .stChatInput { border: 1px solid #00f2ff !important; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Configuración de API
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("No se encontró GOOGLE_API_KEY")
    st.stop()

# Usaremos la librería estándar que suele ser más estable para modelos específicos
genai_v1.configure(api_key=api_key)
model = genai_v1.GenerativeModel('gemini-1.5-flash')

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
            # Llamada directa al modelo configurado
            response = model.generate_content(prompt)
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error técnico: {str(e)}")

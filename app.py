import streamlit as st
import google.generativeai as genai

# Configuración básica
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# Estilo visual sencillo y profesional
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# Configuración de la IA
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Error: GOOGLE_API_KEY no encontrada en los Secrets.")
    st.stop()

# Configurar modelo de forma estándar
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Historial de mensajes
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Lógica del chat
if prompt := st.chat_input("Dano AI escuchando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        try:
            # Generar respuesta
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error de conexión con la IA: {e}")

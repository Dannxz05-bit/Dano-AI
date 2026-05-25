import streamlit as st
import google.generativeai as genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. CSS Estable y Seguro
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Configuración de API
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Error: GOOGLE_API_KEY no encontrada en los Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Usamos 'gemini-pro' que es más estable y compatible en Streamlit Cloud
model = genai.GenerativeModel('gemini-pro')

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
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error técnico: {e}")

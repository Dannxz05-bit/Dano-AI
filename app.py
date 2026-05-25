import streamlit as st
import google.generativeai as genai

# Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# CSS para estilo Reactor (Limpio y estable)
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# Configuración API
api_key = st.secrets.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# USAMOS EL MODELO EXACTO QUE APARECE EN TU LISTA
model = genai.GenerativeModel('gemini-2.0-flash')

# Historial de Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Lógica del Chat
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

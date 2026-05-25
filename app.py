import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. Diseño visual: Reactor de Arco CSS (Sin imágenes externas)
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: 'Courier New', monospace; margin-top: 20px; }
    
    .reactor-container {
        display: flex; justify-content: center; align-items: center;
        margin: 50px auto; width: 250px; height: 250px;
        border-radius: 50%;
        border: 4px solid #00f2ff;
        box-shadow: 0 0 40px #00f2ff, inset 0 0 20px #00f2ff;
        position: relative;
        animation: rotate 10s linear infinite;
    }
    .reactor-core {
        width: 80px; height: 80px;
        background: #ffffff;
        border-radius: 50%;
        box-shadow: 0 0 50px #fff, 0 0 100px #00f2ff;
    }
    @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# El Reactor dibujado con HTML/CSS
st.markdown("""
    <div class="reactor-container">
        <div class="reactor-core"></div>
    </div>
""", unsafe_allow_html=True)

# 3. Lógica de la IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception:
    st.error("Configura tu API KEY en los Secrets.")
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
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception:
            st.error("Error en la respuesta.")

import streamlit as st
from google import genai

# Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: 'monospace'; }
    /* Reactor estilizado con CSS puro */
    .reactor-core {
        width: 200px; height: 200px;
        border: 4px solid #00f2ff;
        border-radius: 50%;
        margin: 30px auto;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 0 50px #00f2ff;
        font-size: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# Reactor CSS Puro
st.markdown('<div class="reactor-core">⚛️</div>', unsafe_allow_html=True)

# Lógica IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error en configuración de API.")
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
            st.error("Error al conectar con el núcleo.")

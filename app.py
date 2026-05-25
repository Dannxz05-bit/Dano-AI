import streamlit as st
from google import genai

# 1. Configuración de página: Layout Wide
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="wide")

# 2. CSS "Blindado": Estética oscura con resplandor neón
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    
    /* Reactor central optimizado para no fallar */
    .reactor {
        width: 250px; height: 250px;
        margin: 50px auto;
        border-radius: 50%;
        border: 4px solid #00f2ff;
        box-shadow: 0 0 60px #00f2ff, inset 0 0 30px #00f2ff;
        display: flex; align-items: center; justify-content: center;
        animation: pulse 3s infinite ease-in-out;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); box-shadow: 0 0 60px #00f2ff; }
        50% { transform: scale(1.05); box-shadow: 0 0 90px #00f2ff; }
    }
    
    h1 { color: #00f2ff; text-align: center; font-family: 'monospace'; }
    </style>
""", unsafe_allow_html=True)

# 3. Interfaz
st.title("💠 DANO AI - REACTOR UNIT")

# Reactor CSS (100% estable)
st.markdown('<div class="reactor"></div>', unsafe_allow_html=True)

# 4. Lógica de Chat
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception:
    st.error("Error: API KEY no detectada.")
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
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception:
            st.error("Error al procesar la respuesta.")

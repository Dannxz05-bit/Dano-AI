import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. Estilos visuales JARVIS
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: 'Courier New', monospace; }
    .stChatInput { border: 2px solid #00f2ff !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Esfera Técnica (Sin errores de red)
st.components.v1.html("""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player 
        src="https://lottie.host/7e04f02f-b472-4d2d-9477-8025219277f0/BfBV6GvzpM.json" 
        background="transparent" 
        speed="1" 
        style="width: 300px; height: 300px; margin: auto;" 
        loop 
        autoplay>
    </lottie-player>
""", height=350)

# 4. Lógica de la IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error: Configura tu GOOGLE_API_KEY en los Secrets.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat
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
        except:
            st.error("Cuota agotada. Espera un momento.")

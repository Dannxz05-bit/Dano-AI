import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. CSS Estético: Animación de giro para la imagen
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: 'monospace'; }
    
    @keyframes girar {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .reactor-img {
        width: 300px;
        height: 300px;
        border-radius: 50%;
        animation: girar 10s linear infinite;
        box-shadow: 0 0 50px #00f2ff;
        border: 2px solid #00f2ff;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Reactor (Usando una imagen más densa y técnica)
st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 20px; margin-bottom: 30px;">
        <img src="https://i.pinimg.com/564x/e7/8a/a5/e78aa5a2041703e29f34546419a4a753.jpg" class="reactor-img">
    </div>
""", unsafe_allow_html=True)

# 4. Lógica IA
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

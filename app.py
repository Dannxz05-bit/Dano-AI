import streamlit as st
from google import genai
import requests
from streamlit_lottie import st_lottie

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. Función de carga optimizada
def load_lottie_url(url: str):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        return None
    return None

# 3. Diseño visual JARVIS
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 4. Contenedor dedicado para la animación
animacion_container = st.empty()

url_esfera = "https://lottie.host/7e04f02f-b472-4d2d-9477-8025219277f0/BfBV6GvzpM.json"
lottie_esfera = load_lottie_url(url_esfera)

if lottie_esfera:
    with animacion_container:
        st_lottie(lottie_esfera, height=300, key="dano_sphere")
else:
    st.write("Error cargando reactor. Verificando red...")

# 5. Lógica del Chat
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error: Falta la API KEY en los Secrets.")
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
            st.error("Cuota agotada. Intenta en unos minutos.")

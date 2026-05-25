import streamlit as st
import pyttsx3
from google import genai
from google.genai import types

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Skibidi AI", page_icon="🚽", layout="centered")

# Estilo personalizado con CSS (Un toque más gamer/cyberpunk)
st.markdown("""
    <style>
    .stApp { background-color: #0f111a; color: #ffffff; }
    .stChatInput input { background-color: #1e2235 !important; color: white !important; border-radius: 20px !important; }
    h1 { color: #ff007f; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 Dano AI")
st.subheader("El asistente más insano de Daniel")
st.write("---")

# Inicializar la API de Google
client = genai.Client(api_key="AIzaSyC_OTzhvhrbi3q84JhmHOS0kqLL14VSWQc")
# ¡Aquí le cambiamos la personalidad!
instrucciones = "Eres Dano, el asistente de Inteligencia Artificial del usuario. Responde siempre en español latino, sé muy divertido, buena onda y usa palabras graciosas de la cultura de internet si viene al caso."

# FUNCIÓN DE VOZ
def hablar(texto):
    if not st.session_state.voz_activa or not texto:
        return
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        texto_limpio = texto.replace("**", "").replace("*", "")
        engine.say(texto_limpio)
        engine.runAndWait()
        engine.stop()
    except:
        pass

# BARRA LATERAL
with st.sidebar:
    st.header("⚙️ Configuración")
    st.session_state.voz_activa = st.toggle("🔊 Activar Voz", value=True)
    st.write("---")
    if st.button("🗑️ Limpiar Historial"):
        st.session_state.mensajes = []
        st.rerun()

# MEMORIA DEL CHAT
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

for msj in st.session_state.mensajes:
    with st.chat_message(msj["rol"]):
        st.write(msj["texto"])

# ENTRADA DEL CHAT
if pregunta := st.chat_input("Escribe tu mensaje para Skibidi..."):
    with st.chat_message("user"):
        st.write(pregunta)
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=pregunta,
            config=types.GenerateContentConfig(system_instruction=instrucciones)
        )
        respuesta_texto = response.text if response.text else "De una, bro."
        
        with st.chat_message("assistant"):
            st.write(respuesta_texto)
        st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta_texto})
        
        hablar(respuesta_texto)
        
    except Exception as e:
        st.error(f"Esperando que se reactive la cuota... (Detalle: {e})")

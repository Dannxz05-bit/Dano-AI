import streamlit as st
from google import genai
from google.genai import types

# CONFIGURACIÓN DE LA APP
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# CSS PARA UN LOOK PROFESIONAL
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; }
    h1 { color: #38bdf8; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 Dano AI")
st.subheader("Tu asistente inteligente y profesional")

# CONFIGURACIÓN DE LA API KEY (Se toma desde los Secrets de Streamlit)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    client = genai.Client(api_key=api_key)
except:
    st.error("Error: Configura la GOOGLE_API_KEY en los Secrets de Streamlit.")
    st.stop()

# INSTRUCCIONES ESTRICTAS (Anti-confusión)
instrucciones = """
Eres Dano AI, un asistente virtual profesional, eficiente y servicial. 
Tu nombre es Dano AI. Nunca te llames de otra forma.
Mantienes un tono serio, claro y directo. Ayudas a los usuarios en español.
"""

# GESTIÓN DEL CHAT
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar historial
for msj in st.session_state.mensajes:
    with st.chat_message(msj["rol"]):
        st.write(msj["texto"])

# Entrada de usuario
if pregunta := st.chat_input("Dano AI te escucha..."):
    # Guardar y mostrar
    st.session_state.mensajes.append({"rol": "user", "texto": pregunta})
    with st.chat_message("user"):
        st.write(pregunta)
    
    # Generar respuesta
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=pregunta,
            config=types.GenerateContentConfig(system_instruction=instrucciones)
        )
        respuesta = response.text
        
        st.session_state.mensajes.append({"rol": "assistant", "texto": respuesta})
        with st.chat_message("assistant"):
            st.write(respuesta)
    except Exception as e:
        st.error("Ocurrió un error al procesar tu solicitud.")

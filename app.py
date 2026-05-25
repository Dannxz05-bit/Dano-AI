import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. Diseño visual estilo JARVIS
st.markdown("""
    <style>
    .stApp { background-color: #000408; color: white; }
    h1 { color: #00f2ff; text-align: center; font-family: 'Courier New', monospace; text-shadow: 0 0 15px #00f2ff; }
    .stChatInput { border: 2px solid #00f2ff !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# 3. Esfera Técnica (GIF optimizado)
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 25px;">
        <img src="https://i.pinimg.com/originals/4f/f0/65/4ff0650a75cd3cfaf6c6b713391588ab.gif" 
             width="300" 
             style="border-radius: 50%; border: 3px solid #00f2ff; box-shadow: 0 0 25px #00f2ff;">
    </div>
""", unsafe_allow_html=True)

# 4. Lógica de la IA
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error: Configura tu GOOGLE_API_KEY en los Secrets de Streamlit.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Historial de chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada del usuario
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
        except Exception as e:
            st.error("Cuota temporal agotada. Espera un momento.")

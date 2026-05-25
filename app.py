import streamlit as st
from google import genai

# 1. Configuración de página
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# 2. CSS Estético: Estilo "Dark Reactor"
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; font-family: 'monospace'; margin-bottom: 20px; }
    /* Contenedor del chat */
    .stChatInput { border: 1px solid #00f2ff !important; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# 3. Encabezado
st.title("💠 DANO AI - REACTOR UNIT")

# 4. Esfera Técnica (Círculo perfecto con brillo neón)
st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 30px;">
        <img src="https://i.pinimg.com/originals/4f/f0/65/4ff0650a75cd3cfaf6c6b713391588ab.gif" 
             style="width: 250px; height: 250px; border-radius: 50%; box-shadow: 0 0 40px #00f2ff; border: 2px solid #00f2ff;">
    </div>
""", unsafe_allow_html=True)

# 5. Lógica del Chat
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error: GOOGLE_API_KEY no detectada.")
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
        except:
            st.error("Sistema ocupado. Intenta de nuevo.")

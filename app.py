import streamlit as st
from google import genai

# Configuración visual "Dark Mode" estilo JARVIS
st.set_page_config(page_title="Dano AI", page_icon="💠")
st.markdown("""
    <style>
    .stApp { background-color: #000408; }
    h1 { color: #00f2ff; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

# Configuración del cliente
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Error: Configura tu API KEY en los Secrets.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada de usuario
if prompt := st.chat_input("Dano AI escuchando..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Usamos gemini-1.5-flash que es el más estable para evitar errores 429 constantes
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            reply = response.text
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error("Error: Cuota temporalmente agotada. Espera unos minutos.")

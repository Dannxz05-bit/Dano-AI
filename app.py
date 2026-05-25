import streamlit as st
import google.generativeai as genai

# Configuración
st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

# CSS para un estilo "Reactor" elegante y estable
st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; font-family: monospace; }
    .reactor {
        width: 200px; height: 200px;
        margin: 40px auto;
        border: 4px solid #00f2ff;
        border-radius: 50%;
        box-shadow: 0 0 50px #00f2ff;
        display: flex; align-items: center; justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")
st.markdown('<div class="reactor"></div>', unsafe_allow_html=True)

# Configuración de IA
api_key = st.secrets.get("GOOGLE_API_KEY")
if not api_key:
    st.error("Configura tu GOOGLE_API_KEY en los Secrets.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Historial y Chat
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
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")

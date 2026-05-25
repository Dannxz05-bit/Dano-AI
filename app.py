import streamlit as st
import google.generativeai as genai
import time

st.set_page_config(page_title="Dano AI", page_icon="💠", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000408 !important; }
    h1 { color: #00f2ff !important; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("💠 DANO AI - REACTOR UNIT")

api_key = st.secrets.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Usamos 'gemini-pro' que suele tener límites diferentes y más estables
model = genai.GenerativeModel('gemini-pro')

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
        # Bloque con reintento automático
        for attempt in range(3): 
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                break 
            except Exception as e:
                if "429" in str(e):
                    st.warning(f"Reactor saturado (Intento {attempt+1}/3). Esperando...")
                    time.sleep(5)
                else:
                    st.error(f"Error técnico: {e}")
                    break

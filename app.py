import streamlit as st
import google.generativeai as genai

st.title("Dano AI - Reactor")

# Configuración de la API (Asegúrate de que tu Secret sea GOOGLE_API_KEY)
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Error: No se encontró GOOGLE_API_KEY en los secretos.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Escribe algo..."):
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

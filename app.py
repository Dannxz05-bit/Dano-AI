import streamlit as st
from google import genai

# Título y configuración
st.set_page_config(page_title="Dano AI", page_icon="💠")
st.title("💠 Dano AI")

# Configuración de la API desde los Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("Error al cargar la API KEY desde los Secrets.")
    st.stop()

# Historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Interacción
if prompt := st.chat_input("Dano AI te escucha..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Respuesta directa y simple
            response = client.models.generate_content(
                model='gemini-1.5-flash',
                contents=f"Eres Dano AI, un asistente útil y profesional. Responde a esto: {prompt}"
            )
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"Error técnico: {e}")

import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(page_title="Dano AI", page_icon="💠")
st.title("💠 Dano AI")

# Retrieve API Key from Streamlit Secrets
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Error: GOOGLE_API_KEY no encontrada en los Secrets de Streamlit.")
    st.stop()

# Initialize Client
client = genai.Client(api_key=api_key)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle Chat Input
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )
            reply = response.text
            st.markdown(reply)
            
            # Append Assistant Response
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error de conexión con Gemini: {e}")

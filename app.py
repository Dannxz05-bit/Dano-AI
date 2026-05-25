import streamlit as st
import google.generativeai as genai

st.title("Diagnóstico de Dano AI")

api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("No hay API Key configurada.")
    st.stop()

genai.configure(api_key=api_key)

try:
    # Vamos a listar los modelos disponibles en tu cuenta
    st.write("Verificando modelos disponibles en tu cuenta:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            st.write(f"✅ Modelo disponible: {m.name}")
except Exception as e:
    st.error(f"Error fatal: {e}")

import streamlit as st
import google.generativeai as genai

# Conectar la clave secreta
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Escáner de Google AI 🔍")
st.write("Vamos a descubrir qué modelos tienes habilitados en tu cuenta.")

if st.button("Escanear Modelos"):
    try:
        modelos_validos = []
        # Le pedimos a Google toda su lista interna
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                modelos_validos.append(m.name)
        
        st.success("¡Búsqueda completada con éxito!")
        st.write("Estos son los modelos que puedes usar. Envíame esta lista:")
        st.write(modelos_validos)
        
    except Exception as e:
        st.error(f"Error de conexión: {e}")

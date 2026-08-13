import streamlit as st
import google.generativeai as genai

# Conecta con tu clave secreta de forma segura
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Configura el modelo
model = genai.GenerativeModel('gemini-1.5-flash')

# Diseño de la página
st.title("Mi Primera App Web con IA")
st.write("Escribe tu pregunta y la IA de Google te responderá:")

# Cuadro de chat
mensaje = st.text_input("Tu mensaje:")
if st.button("Enviar"):
    if mensaje:
        respuesta = model.generate_content(mensaje)
        st.write(respuesta.text)

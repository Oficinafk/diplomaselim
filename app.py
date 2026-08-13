import streamlit as st
import google.generativeai as genai

# Conectar la clave secreta
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.title("Mi Primera App Web con IA")
st.write("Escribe tu pregunta y la IA te responderá:")

mensaje = st.text_input("Tu mensaje:")

if st.button("Enviar"):
    if mensaje:
        try:
            # Usamos el modelo base universal que no tiene restricciones
            model = genai.GenerativeModel('gemini-pro')
            
            # Procesamos tu mensaje
            respuesta = model.generate_content(mensaje)
            st.success("¡Conexión exitosa!")
            st.write(respuesta.text)
        
        except Exception as e:
            st.error(f"Error de Google: {e}")

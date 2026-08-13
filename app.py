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
            # Forzamos a usar el modelo 1.5 Pro que es estable y público
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            # Procesamos tu mensaje
            respuesta = model.generate_content(mensaje)
            st.success("¡Conexión exitosa!")
            st.write(respuesta.text)
        
        except Exception as e:
            st.error(f"Error de Google: {e}")

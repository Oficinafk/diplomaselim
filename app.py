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
            # Le pedimos a Google que busque el nombre exacto del modelo disponible para tu cuenta
            modelos_disponibles = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            if modelos_disponibles:
                # Usamos el primer modelo válido que Google encuentre automáticamente
                modelo_elegido = modelos_disponibles[0] 
                model = genai.GenerativeModel(modelo_elegido)
                
                # Procesamos tu mensaje
                respuesta = model.generate_content(mensaje)
                st.success("¡Conexión exitosa!")
                st.write(respuesta.text)
            else:
                st.error("La clave funciona, pero no tiene modelos de IA asignados.")
        
        except Exception as e:
            st.error(f"Error de Google: {e}")

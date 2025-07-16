# app.py
import streamlit as st
from ejercicio import obtener_respuesta_agente

st.set_page_config(page_title="Agente Wikipedia", page_icon="🤖")

st.title("Agente conversacional con Wikipedia y Azure OpenAI")
st.write("Haz una pregunta y el agente te responderá usando información actualizada de Wikipedia. El agente solo responderá preguntas de geografía.")

# Sesión para el historial de mensajes
if "historial" not in st.session_state:
    st.session_state.historial = []

# Formulario de entrada de usuario
pregunta = st.chat_input("Escribe tu pregunta aquí...")

if pregunta:
    st.session_state.historial.append({"role": "user", "content": pregunta})
    respuesta = obtener_respuesta_agente(pregunta)
    st.session_state.historial.append({"role": "assistant", "content": respuesta})

# Mostrar la conversación
for msg in st.session_state.historial:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])
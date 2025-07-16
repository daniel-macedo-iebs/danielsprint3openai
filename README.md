# Agente Conversacional con Wikipedia y Azure OpenAI

Este proyecto implementa una aplicación conversacional basada en inteligencia artificial que responde preguntas utilizando información actualizada de Wikipedia, integrando capacidades de Retrieval-Augmented Generation (RAG) y function calling.  
El usuario interactúa mediante una interfaz web simple construida con Streamlit.

## Descripción

El agente:
- Recibe preguntas en lenguaje natural a través de una interfaz web.
- Busca información relevante en Wikipedia.
- Añade los fragmentos encontrados como contexto para la generación de respuestas usando Azure OpenAI.
- Devuelve una respuesta generada y contextualizada en el chat.

## Tecnologías

- Python 3.8+
- Streamlit (frontend web)
- `requests` para consultas HTTP a la API de Wikipedia
- Azure OpenAI para generación de respuestas

## Instalación

1. Clona el repositorio:  
`git clone https://github.com/tu-usuario/mi-app-conversacional.git`
`cd mi-app-conversacional`

2. (Opcional, recomendado) Crea y activa un entorno virtual:  
`python3 -m venv venv`
`source venv/bin/activate`

3. Instala las dependencias:  
`pip install -r requirements.txt`


## Configuración

Configura tus credenciales de Azure OpenAI mediante variables de entorno.  
Crea un archivo `.env` o exporta estas variables en tu terminal:  
`export ENDPOINT_URL="https://<tu-endpoint>.openai.azure.com/"`  
`export DEPLOYMENT_NAME="nombre-de-tu-despliegue"`  
`export AZURE_OPENAI_API_KEY="tu-clave"`  

Si usas un archivo `.env`, puedes requerir [python-dotenv](https://pypi.org/project/python-dotenv/) para el autoload.

## Ejecución

Arranca la aplicación web con:  
`streamlit run app.py`

Accede en tu navegador al enlace mostrado en consola (`http://localhost:8501` por defecto).

## Uso

1. Escribe cualquier pregunta en español en la interfaz web.
2. El agente busca información relevante en Wikipedia y responde usando Azure OpenAI.
3. El historial de la conversación se muestra en pantalla.

## Arquitectura y flujo de la aplicación

1. **Usuario** ingresa una pregunta a través del frontend (Streamlit).
2. **Backend** consulta la API de Wikipedia para recuperar fragmentos relevantes (function calling y RAG).
3. **Azure OpenAI** genera una respuesta tomando como contexto la información recuperada.
4. **Frontend** muestra la respuesta y el historial de la conversación.


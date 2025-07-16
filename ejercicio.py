import requests

import os
import base64
from openai import AzureOpenAI

def buscar_wikipedia(query):
    url = (
        "https://es.wikipedia.org/w/api.php"
        "?action=query"
        "&list=search"
        "&format=json"
        f"&srsearch={query}"
        "&utf8="
        "&srlimit=3"
        "&origin=*"
    )
    response = requests.get(url)
    resultados = []
    if response.status_code == 200:
        data = response.json()
        for item in data.get("query", {}).get("search", []):
            titulo = item["title"]
            snippet = item["snippet"]
            pageid = item["pageid"]
            enlace = f"https://es.wikipedia.org/?curid={pageid}"
            resultados.append({"titulo": titulo, "fragmento": snippet, "enlace": enlace})
    return resultados

def obtener_respuesta_agente(pregunta):
    endpoint = os.getenv("ENDPOINT_URL", "https://danielpruebaopenai.openai.azure.com/")
    deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-2024-11-20")
    subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "key")
    # Inicializar el cliente de Azure OpenAI con autenticación basada en claves
    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )

    resultados = buscar_wikipedia(pregunta)

    # Prepara el contexto con los resultados de Wikipedia
    contexto_wikipedia = "\n".join(
        [f"{r['titulo']}: {r['fragmento']} ({r['enlace']})" for r in resultados]
    )

    #Prepare la indicación de chat
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "Es un asistente de inteligencia artificial que ayuda a los usuarios a encontrar información sobre geografía. Rechaza amablemente cualquier pregunta que no tenga que ver con la geografía"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hasta que fecha has aprendido"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Pregunta: {pregunta}\n\nInformación encontrada en Wikipedia:\n{contexto_wikipedia}\n\nResponde usando la información relevante."
                }
            ]
        }
    ]
    # Incluir el resultado de voz si la voz está habilitada
    messages = chat_prompt
    # Generar finalización
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages
    )
    return completion.choices[0].message.content
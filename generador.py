import os
import requests
from datetime import datetime
import re

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_contenido_premium():
    if not GROQ_API_KEY: return None
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # Le pedimos que la primera línea sea SIEMPRE el título
    prompt = """
    Escribe un artículo técnico de 800 palabras para un blog de ingeniería. 
    REGLA DE ORO: La primera línea debe ser un TÍTULO llamativo y único (sin negritas ni #).
    A partir de la segunda línea, desarrolla el contenido en Markdown.
    
    Temas sugeridos (elige uno al azar): IA en ciberseguridad, automatización con Python, 
    nuevas funciones de Godot 4.x, redes neuronales o hardware para devs.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.8 # Más creativo para que no repita temas
    }
    
    response = requests.post(URL_GROQ, headers=headers, json=data)
    if response.status_code != 200: return None
    return response.json()['choices'][0]['message']['content']

raw_text = generar_contenido_premium()

if raw_text:
    # Separamos la primera línea (título) del resto del cuerpo
    lineas = raw_text.split('\n')
    titulo_ia = lineas[0].strip().replace('"', '')
    cuerpo = "\n".join(lineas[1:])

    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    file_path = os.path.join(folder, f"premium-{date_str}.md")
    
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "{titulo_ia}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{cuerpo}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ ¡Artículo único creado!: {titulo_ia}")

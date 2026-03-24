import os
import requests
from datetime import datetime

# 1. Configuración de la IA (Groq)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_contenido_ia():
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Le pedimos a la IA que elija una herramienta útil
    prompt = "Escribe un artículo corto en formato Markdown sobre una herramienta de IA útil para programadores o creadores de contenido. Incluye un título matador, 3 beneficios y una conclusión. El tono debe ser profesional y emocionante. No añadas introducciones extrañas, solo el contenido del artículo."
    
    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(URL_GROQ, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

# 2. Preparar el archivo
folder = "src/pages/herramientas"
os.makedirs(folder, exist_ok=True)

now = datetime.now()
date_str = now.strftime("%Y-%m-%d-%H%M")
file_path = os.path.join(folder, f"ia-news-{date_str}.md")

# 3. Obtener el texto de la IA
texto_ia = generar_contenido_ia()

# 4. Crear el archivo final con el frontmatter de Astro
final_content = f"""---
layout: ../../layouts/Layout.astro
title: "Novedad en IA: {now.strftime('%d/%m/%Y')}"
fecha: "{now.strftime('%d/%m/%Y')}"
---

{texto_ia}
"""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"✅ ¡IA ha redactado un nuevo artículo en {file_path}!")

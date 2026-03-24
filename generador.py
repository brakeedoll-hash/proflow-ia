import os
import requests
from datetime import datetime

# 1. Configuración
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_contenido_ia():
    if not GROQ_API_KEY:
        print("❌ ERROR: La variable GROQ_API_KEY está vacía.")
        return None

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # He corregido el espacio aquí abajo:
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": "Escribe un artículo corto en Markdown sobre una herramienta de IA útil para programadores o para desarrollo de juegos en Godot."}]
    }
    
    print("🤖 Intentando conectar con Groq...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    
    if response.status_code != 200:
        print(f"❌ Error de Groq (Status {response.status_code}):")
        print(response.text)
        return None
        
    res_json = response.json()
    return res_json['choices'][0]['message']['content']

# 2. Lógica principal
texto = generar_contenido_ia()

if texto:
    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    file_path = os.path.join(folder, f"ia-news-{date_str}.md")
    
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "IA Update {datetime.now().strftime('%d/%m/%Y')}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{texto}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ ¡Artículo creado!: {file_path}")
else:
    print("⚠️ No se pudo generar el artículo.")
    exit(1)

# Prompt enfocado en SEO y Conversión
    prompt = """
    Actúa como un experto en SEO y Marketing Digital. 
    Escribe un artículo de blog optimizado para Google sobre una herramienta de IA (software, plugin de Godot, o app productiva).
    
    Estructura obligatoria:
    1. Título llamativo con la palabra 'Mejor' o 'Gratis'.
    2. Introducción que ataque un problema del programador.
    3. Lista de 3 beneficios clave.
    4. Una sección de 'Por qué deberías usarlo hoy'.
    5. Un llamado a la acción (CTA) invitando a probar herramientas similares.
    
    IMPORTANTE: Usa un lenguaje sencillo pero profesional. No menciones que eres una IA.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7 # Esto le da un toque más creativo y menos robótico
    }

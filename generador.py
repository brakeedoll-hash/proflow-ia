import os
import requests
import random
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_noticia_real():
    if not GROQ_API_KEY: return None
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # Categorías para que el bot varíe el contenido
    temas = ["Últimas noticias IA 2026", "Lanzamientos hardware marzo 2026", "Ciberseguridad noticias hoy", "Novedades Godot Engine 2026"]
    busqueda = random.choice(temas)
    
    # PROMPT: Le ordenamos que use su conocimiento actualizado (Llama 3 tiene acceso a datos recientes)
    # y que se base en hechos reales de marzo de 2026.
    prompt = f"""
    Eres un reportero técnico real. Investiga y redacta una noticia VERDADERA y ACTUAL sobre: {busqueda}.
    
    REQUISITOS:
    1. La noticia debe haber ocurrido en las últimas 48 horas de marzo de 2026.
    2. El TÍTULO debe ser real y periodístico (Primera línea, sin #).
    3. Escribe 800 palabras detallando nombres de empresas, productos o eventos reales.
    4. Usa Markdown con subtítulos H2.
    5. No inventes specs; si no estás seguro, usa datos confirmados de la industria.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5 # Bajamos la temperatura para que sea más fiel a la realidad y menos "creativo"
    }
    
    print(f"🕵️ Buscando información real sobre: {busqueda}...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    if response.status_code != 200: return None
    return response.json()['choices'][0]['message']['content']

raw_text = generar_noticia_real()

if raw_text:
    lineas = raw_text.split('\n')
    titulo_real = lineas[0].strip().replace('"', '').replace('#', '')
    cuerpo_real = "\n".join(lineas[1:])

    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join(folder, f"noticia-{timestamp}.md")
    
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "{titulo_real}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{cuerpo_real}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"📰 Noticia Real Publicada: {titulo_real}")

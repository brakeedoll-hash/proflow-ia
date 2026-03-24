import os
import requests
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_contenido_premium():
    if not GROQ_API_KEY:
        print("❌ ERROR: Falta GROQ_API_KEY")
        return None

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # PROMPT PARA ARTÍCULOS LARGOS (600-800 PALABRAS)
    prompt = """
    Actúa como un experto en Ingeniería de Sistemas y Redactor Tech. 
    Escribe un artículo EXTENSO y profundo en Markdown sobre una herramienta de IA o técnica avanzada de desarrollo (Godot, Python, o Automatización).
    
    ESTRUCTURA OBLIGATORIA:
    1. Título H1 impactante.
    2. Introducción detallada (mínimo 2 párrafos).
    3. H2: 'Análisis Técnico de la Herramienta'.
    4. H2: 'Ventajas para el Desarrollo Moderno'.
    5. H2: 'Guía de Implementación Paso a Paso' (incluye un ejemplo de código o lógica).
    6. H2: 'Conclusión y Futuro de esta Tecnología'.
    
    REGLAS: Mínimo 600 palabras. No menciones que eres una IA. 
    Usa un tono educativo, profesional y optimizado para SEO con palabras clave técnicas.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.6 # Menos creativo, más preciso y técnico
    }
    
    print("🤖 Generando artículo de alta calidad para AdSense...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    
    if response.status_code != 200: return None
    return response.json()['choices'][0]['message']['content']

texto = generar_contenido_premium()

if texto:
    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    file_path = os.path.join(folder, f"premium-ia-{date_str}.md")
    
    # Extraemos un título limpio para el frontmatter
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "Análisis: Innovación en IA {datetime.now().strftime('%Y')}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{texto}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ ¡Artículo Premium creado!: {file_path}")

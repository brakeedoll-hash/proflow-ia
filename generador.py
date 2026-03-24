import os
import requests
import random
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_noticia_variada_real():
    if not GROQ_API_KEY: return None
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # LISTA DE TEMAS REALES (Sin nada de Godot para variar)
    fuentes_reales = [
        "Nuevos procesadores NVIDIA RTX 50 series y AMD Ryzen 2026",
        "Avances de OpenAI y el nuevo modelo GPT-5 en marzo 2026",
        "Ciberseguridad: Gran filtración de datos en empresas de Europa hoy",
        "Starlink y la nueva velocidad de internet satelital en Costa Rica",
        "SpaceX: Lanzamiento exitoso de la Starship en marzo 2026",
        "Apple anuncia nuevas gafas Vision Pro 2: Características reales",
        "Descubrimiento científico en computación cuántica esta semana"
    ]
    
    tema_hoy = random.choice(fuentes_reales)
    
    # PROMPT AGRESIVO PARA EVITAR REPETICIONES
    prompt = f"""
    Eres un periodista de tecnología internacional. Hoy es {datetime.now().strftime('%d de marzo de 2026')}.
    Tu misión es redactar una noticia REAL y SERIA sobre: {tema_hoy}.

    REGLAS CRÍTICAS:
    1. PROHIBIDO hablar de Godot Engine. Si lo mencionas, el artículo será rechazado.
    2. La primera línea es el TITULAR (Sin #, sin negritas, máximo 12 palabras).
    3. Mínimo 800 palabras. Usa datos técnicos, nombres de CEOs y fechas de marzo 2026.
    4. Usa Markdown (H2 para subtítulos).
    5. No inventes, actúa como si estuvieras leyendo la noticia en Reuters o The Verge.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4 # Muy bajo para que no se ponga "creativo" e invente cosas
    }
    
    print(f"📡 Generando noticia REAL sobre: {tema_hoy}...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    if response.status_code != 200: return None
    return response.json()['choices'][0]['message']['content']

raw_text = generar_noticia_variada_real()

if raw_text:
    lineas = raw_text.split('\n')
    titulo_final = lineas[0].strip().replace('"', '').replace('#', '')
    cuerpo_final = "\n".join(lineas[1:])

    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join(folder, f"tech-news-{timestamp}.md")
    
    # El frontmatter ahora es dinámico y limpio
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "{titulo_final}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{cuerpo_final}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ Noticia publicada con éxito: {titulo_final}")

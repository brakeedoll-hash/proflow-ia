import os
import requests
import random
from datetime import datetime

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
URL_GROQ = "https://api.groq.com/openai/v1/chat/completions"

def generar_noticia_real_pro():
    if not GROQ_API_KEY: return None
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    # Fuentes de temas de alta relevancia en marzo 2026
    temas_reales = [
        "Nuevas GPUs NVIDIA RTX 50 'Blackwell' y GDDR7",
        "Lanzamiento de procesadores AMD Ryzen serie 9000 con arquitectura Zen 6",
        "Actualizaciones de OpenAI: GPT-5 y Sora para el público general",
        "Ciberseguridad: Nueva vulnerabilidad en procesadores Intel Nova Lake",
        "SpaceX: Progreso de la Starship y misiones a la Luna en 2026",
        "Apple Vision Pro 2: Mejoras en micro-OLED y peso",
        "Avances en Redes: Starlink Mini y cobertura global en Costa Rica"
    ]
    
    seleccion = random.choice(temas_reales)
    
    # EL PROMPT DE ALTA PRECISIÓN (Evita inventar datos)
    prompt = f"""
    Eres un analista senior de 'Digital Foundry' y 'The Verge'. 
    Hoy es {datetime.now().strftime('%d de marzo de 2026')}.
    Redacta una noticia técnica REAL y TRANSPARENTE sobre: {seleccion}.

    REGLAS DE ORO PARA EVITAR ALUCINACIONES:
    1. PROHIBIDO INVENTAR NÚMEROS: Si no existe un dato oficial de núcleos o frecuencia, di 'según filtraciones de fuentes de la industria' o 'se estima un aumento porcentual'.
    2. CONTEXTO 2026: Usa tecnologías de este año (PCIe 5.0/6.0, DDR5/6, Wi-Fi 7). 
    3. TERMINOLOGÍA REAL: Si hablas de NVIDIA usa 'Blackwell', si es AMD usa 'Zen 6', si es Intel usa 'Nova Lake'.
    4. TRANSPARENCIA: Si la noticia es un rumor fuerte, indícalo claramente al lector.
    5. ESTRUCTURA: Primera línea = TÍTULO profesional. Resto = Markdown con H2 (mínimo 800 palabras).
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3 # Temperatura muy baja para máxima fidelidad a los hechos
    }
    
    print(f"🕵️ Investigando y redactando noticia real sobre: {seleccion}...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    if response.status_code != 200: return None
    return response.json()['choices'][0]['message']['content']

raw_text = generar_noticia_real_pro()

if raw_text:
    lineas = raw_text.split('\n')
    titulo_noticia = lineas[0].strip().replace('"', '').replace('#', '')
    cuerpo_noticia = "\n".join(lineas[1:])

    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_path = os.path.join(folder, f"real-news-{timestamp}.md")
    
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "{titulo_noticia}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{cuerpo_noticia}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ Noticia real publicada: {titulo_noticia}")

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
    
    # PROMPT ESTRATÉGICO PARA INGRESOS PASIVOS
    prompt = """
    Actúa como un experto en SEO y Marketing Digital. 
    Escribe un artículo de blog optimizado para Google sobre una herramienta de IA (software de productividad, plugin de Godot, o herramienta de código).
    
    Estructura obligatoria en Markdown:
    1. Título llamativo (H1) que incluya palabras como 'Mejor', 'Gratis' o '2026'.
    2. Introducción que ataque un problema real de un programador o desarrollador.
    3. Lista de 3 beneficios clave (con viñetas).
    4. Una sección titulada '¿Por qué deberías probarlo hoy?'.
    5. Un llamado a la acción (CTA) profesional.
    
    REGLAS: No digas que eres una IA. Usa un tono emocionante y profesional. 
    Si la herramienta tiene versión de pago, menciónala como una inversión.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    print("🤖 Generando contenido optimizado para SEO...")
    response = requests.post(URL_GROQ, headers=headers, json=data)
    
    if response.status_code != 200:
        print(f"❌ Error de Groq: {response.status_code}")
        return None
        
    res_json = response.json()
    return res_json['choices'][0]['message']['content']

# 2. Lógica de guardado
texto = generar_contenido_ia()

if texto:
    folder = "src/pages/herramientas"
    os.makedirs(folder, exist_ok=True)
    
    # Nombre de archivo basado en fecha para evitar duplicados
    date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
    file_path = os.path.join(folder, f"ia-expert-{date_str}.md")
    
    final_content = f"""---
layout: ../../layouts/Layout.astro
title: "Recomendación IA {datetime.now().strftime('%d/%m/%Y')}"
fecha: "{datetime.now().strftime('%d/%m/%Y')}"
---

{texto}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ ¡Artículo de marketing creado!: {file_path}")
else:
    print("⚠️ Falló la generación de contenido.")
    exit(1)

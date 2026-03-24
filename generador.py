import os
from datetime import datetime

# 1. Definir la ruta de la carpeta (Aseguramos que exista)
folder = "src/pages/herramientas"
if not os.path.exists(folder):
    os.makedirs(folder)

# 2. Fecha y nombre de archivo único
now = datetime.now()
date_str = now.strftime("%Y-%m-%d-%H%M")
file_name = f"herramienta-ia-{date_str}.md"
file_path = os.path.join(folder, file_name)

# 3. El contenido con la RUTA CORREGIDA (../../layouts/Layout.astro)
content = f"""---
layout: ../../layouts/Layout.astro
title: "Cómo usar IA para optimizar scripts en Godot"
fecha: "{now.strftime('%d/%m/%Y')}"
---

# Optimización de GDScript con Inteligencia Artificial

En la ingeniería de sistemas, la eficiencia es clave. Hoy probamos una herramienta de IA que ayuda a depurar nodos y mejorar el rendimiento de las barras de vida y XP en proyectos RPG.

### Beneficios clave:
* **Menos Bugs:** Detecta errores de indentación automáticamente.
* **Velocidad:** Genera estructuras de datos complejas en segundos.
* **Aprendizaje:** Ideal para estudiantes de la UISIL que inician en desarrollo de juegos.

*Este artículo fue generado automáticamente por el motor de ProFlow IA.*
"""

# 4. Escribir el archivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Artículo generado en: {file_path}")

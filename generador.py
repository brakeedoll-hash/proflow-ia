import os
from datetime import datetime

# 1. Definir dónde se guardará el artículo
folder = "src/pages/herramientas"
os.makedirs(folder, exist_ok=True)

# 2. Obtener la fecha de hoy para el nombre del archivo
date_str = datetime.now().strftime("%Y-%m-%d-%H%M")
file_name = f"ia-godot-auto-{date_str}.md"
file_path = os.path.join(folder, file_name)

# 3. El contenido del artículo (Aquí luego conectaremos la IA real)
content = f"""---
layout: ../../layouts/Layout.astro
title: "Auto-Generador de Código para Godot - {date_str}"
fecha: "{date_str}"
---

# Auto-Generador de Sistemas RPG en Godot

Esta herramienta lee tu árbol de nodos y crea automáticamente la lógica para barras de XP, estadísticas de personajes (ideal para estructurar a un protagonista como Akira Oda) y sistemas de subida de nivel sin escribirGDScript desde cero.

*Generado automáticamente por nuestro bot el {date_str}.*
"""

# 4. Crear el archivo
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Archivo creado exitosamente: {file_path}")

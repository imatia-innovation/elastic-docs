#!/usr/bin/env python3
"""
Script para insertar imágenes extraídas de PDFs en los markdown de la wiki
Busca imágenes en static/img/{modulo}/ e inserta en docs/{modulo}/intro.md
"""

import os
from pathlib import Path

# Mapeo de módulos
MODULES = {
    "almacen": "Almacén",
    "ventas": "Ventas",
    "compras": "Compras",
    "finanzas": "Finanzas",
    "crm": "CRM",
    "laboral": "Laboral",
    "produccion": "Producción",
    "trazabilidad": "Trazabilidad",
    "calidad": "Calidad",
    "guia_de_uso": "Guía de Uso"
}

def get_images_for_module(module_key):
    """Obtiene lista de imágenes para un módulo
    
    Args:
        module_key: Clave del módulo
    
    Returns:
        Lista de rutas relativas de imágenes
    """
    
    project_root = Path(__file__).parent.parent
    img_dir = project_root / "static" / "img" / module_key
    
    if not img_dir.exists():
        return []
    
    # Obtener todas las imágenes PNG, ordenadas
    images = sorted([f"/img/{module_key}/{img.name}" for img in img_dir.glob("*.png")])
    return images

def generate_image_markdown(images, module_key):
    """Genera código markdown para insertar imágenes
    
    Args:
        images: Lista de rutas de imágenes
        module_key: Clave del módulo
    
    Returns:
        String con markdown de imágenes
    """
    
    if not images:
        return ""
    
    markdown_lines = ["\n## Imágenes de Referencia\n"]
    
    for image_path in images:
        # Extraer nombre amigable del archivo
        filename = os.path.basename(image_path)
        # Generar alt text
        alt_text = f"Imagen del módulo {MODULES.get(module_key, module_key)}"
        
        markdown_lines.append(f"![{alt_text}]({image_path})\n")
    
    return "".join(markdown_lines)

def insert_images_in_module(module_key):
    """Inserta imágenes en el markdown del módulo
    
    Args:
        module_key: Clave del módulo
    
    Returns:
        Número de imágenes insertadas
    """
    
    project_root = Path(__file__).parent.parent
    markdown_file = project_root / "docs" / module_key / "intro.md"
    
    # Obtener imágenes
    images = get_images_for_module(module_key)
    
    if not images:
        return 0
    
    if not markdown_file.exists():
        print(f"  ⚠ Archivo no encontrado: {markdown_file}")
        return 0
    
    # Leer contenido actual
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar si ya está la sección de imágenes
    if "## Imágenes de Referencia" in content:
        # Reemplazar sección existente
        import re
        pattern = r'\n## Imágenes de Referencia\n.*?(?=\n##|\Z)'
        new_section = generate_image_markdown(images, module_key)
        content = re.sub(pattern, new_section, content, flags=re.DOTALL)
        print(f"  ✓ Actualizada sección de imágenes")
    else:
        # Añadir al final
        new_section = generate_image_markdown(images, module_key)
        content += new_section
        print(f"  ✓ Añadida nueva sección de imágenes")
    
    # Guardar contenido actualizado
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return len(images)

def main():
    """Procesa todos los módulos e inserta imágenes"""
    
    print("=" * 60)
    print("INSERTOR DE IMÁGENES EN MARKDOWN")
    print("=" * 60)
    
    total_images = 0
    
    for module_key, module_name in MODULES.items():
        images = get_images_for_module(module_key)
        
        if images:
            print(f"\n📋 Módulo: {module_name}")
            print(f"   Imágenes encontradas: {len(images)}")
            
            images_inserted = insert_images_in_module(module_key)
            total_images += images_inserted
        else:
            print(f"\n⚠ {module_name}: Sin imágenes")
    
    print("\n" + "=" * 60)
    print(f"✅ PROCESO COMPLETADO")
    print(f"   Total de imágenes insertadas: {total_images}")
    print("=" * 60)

if __name__ == "__main__":
    main()

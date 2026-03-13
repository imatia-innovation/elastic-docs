#!/usr/bin/env python3
"""
Script para reorganizar la wiki siguiendo la estructura del manual PDF
y filtrar imágenes para mantener solo las funcionales del ERP
"""

import os
import re
from pathlib import Path

def get_content_images_filtered(module_key):
    """Obtiene solo las imágenes de contenido funcional (excluyendo portadas)
    
    Las primeras páginas suelen ser:
    - Portadas
    - Logos de Imatia  
    - Índices
    - Páginas de presentación
    
    Mantenemos imágenes de páginas 8+ donde comienza el contenido útil
    """
    
    project_root = Path(__file__).parent.parent
    img_dir = project_root / "static" / "img" / module_key
    
    if not img_dir.exists():
        return []
    
    all_images = sorted([f for f in img_dir.glob("*.png")])
    
    # Filtrar imágenes del contenido (excluir primeras páginas)
    filtered = []
    for img in all_images:
        filename = img.name
        # Extraer número de página
        match = re.search(r'_page(\d+)_', filename)
        if match:
            page_num = int(match.group(1))
            # Mantener imágenes a partir de página 8 (evita portadas y logos)
            if page_num >= 8:
                filtered.append(f"/img/{module_key}/{filename}")
    
    return filtered

def generate_structured_intro():
    """Genera estructura mejorada del intro.md siguiendo el manual"""
    
    content = """# Almacén

## Descripción

El **módulo de almacén** de Elastic Business ERP permite gestionar de forma integral:

- **Inventario**: Control centralizado del stock disponible
- **Parámetros**: Configuración de familias de artículos y generación de códigos
- **Modelos de costes**: Valoración de inventarios con diferentes métodos
- **Niveles de seguridad**: Automatización de reorden de stock

## Estructura del módulo

El módulo de almacén se organiza en 4 áreas principales:

### 1. Parámetros
Configuración de identificadores que permiten generar códigos y descripciones únicos en los artículos.

- **Acceso**: Almacén >> Parámetros
- **Organización**: Por familias de artículos
- Tipos: Explícitos (valores libres) e Implícitos (lista predefinida)

[Ver documentación completa →](01-parametros.md)

### 2. Modelo de Costes
Definición de estrategias de valoración de inventarios.

- **Acceso**: Almacén >> Modelo de costes
- **Tipos de modelo**:
  - Modelo básico
  - Modelo con sobrecostes
  - Modelo personalizado

[Ver documentación completa →](02-modelo-costes.md)

### 3. Stock de Seguridad
Establecimiento de niveles mínimos automáticos de inventario.

- **Acceso**: Almacén >> Stock de seguridad
- Control automático de reordenes
- Alertas de stock bajo

[Ver documentación completa →](03-stock-seguridad.md)

### 4. Familias de Artículos
Definición de categorías y grupos de productos.

- Clasificación jerárquica
- Propiedades compartidas dentro de familia

[Ver documentación completa →](04-familias-articulos.md)

## Características principales

✓ **Gestión centralizada** - Un único eje de referencia para todos los artículos  
✓ **Configuración flexible** - Adaptable a diferentes modelos de negocio  
✓ **Automatización** - Reordenes y alertas automáticas  
✓ **Trazabilidad** - Historiales de movimientos y cambios  

## Integración con otros módulos

- **Compras**: Recepción de mercancía en almacén
- **Ventas**: Disponibilidad de stock para pedidos
- **Producción**: Consumo de materiales y control de BOM
- **Finanzas**: Valoración de inventarios para contabilidad

## Tutorial visual

A continuación se muestran imágenes de los principales procesos y pantallas del módulo:

"""
    return content

def main():
    """Reorganiza la wiki del almacén"""
    
    project_root = Path(__file__).parent.parent
    intro_file = project_root / "docs" / "almacen" / "intro.md"
    
    print("=" * 70)
    print("REORGANIZADOR DE WIKI - SECCIÓN ALMACÉN")
    print("=" * 70)
    
    # Generar contenido estructurado
    base_content = generate_structured_intro()
    
    # Obtener imágenes filtradas
    images = get_content_images_filtered("almacen")
    
    print(f"\n📋 Módulo: Almacén")
    print(f"   Imágenes filtradas (excluyendo portadas): {len(images)}")
    print(f"   Se mantienen imágenes de página 8 en adelante")
    
    # Construir galería de imágenes
    if images:
        base_content += "\n## Pantallas del Sistema\n\n"
        
        # Agrupar imágenes por página
        pages = {}
        for img in images:
            match = re.search(r'_page(\d+)_', img)
            if match:
                page = int(match.group(1))
                if page not in pages:
                    pages[page] = []
                pages[page].append(img)
        
        for page in sorted(pages.keys()):
            base_content += f"### Página {page}\n\n"
            for img in pages[page]:
                base_content += f"![Pantalla del módulo]({img})\n\n"
    
    # Guardar archivo
    with open(intro_file, 'w', encoding='utf-8') as f:
        f.write(base_content)
    
    print(f"   ✓ Contenido reorganizado")
    print(f"   ✓ Archivo guardado: {intro_file}")
    
    print("\n" + "=" * 70)
    print("✅ REORGANIZACIÓN COMPLETADA")
    print("=" * 70)

if __name__ == "__main__":
    main()

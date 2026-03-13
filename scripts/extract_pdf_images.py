#!/usr/bin/env python3
"""
Script para extraer imágenes de PDFs y añadirlas a la wiki
Procesa PDFs de docs/assets/source-pdfs/{modulo}/ 
y guarda imágenes en static/img/{modulo}/
"""

import os
import sys
from pathlib import Path
from PIL import Image
import fitz  # PyMuPDF

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

def extract_images_from_pdf(pdf_path, output_dir, module_name):
    """Extrae imágenes de un PDF
    
    Args:
        pdf_path: Ruta del PDF
        output_dir: Carpeta de destino
        module_name: Nombre del módulo
    """
    
    print(f"  Procesando: {os.path.basename(pdf_path)}")
    
    try:
        # Abrir PDF
        pdf_document = fitz.open(pdf_path)
        image_count = 0
        
        # Iterar sobre páginas
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            
            # Obtener imágenes de la página
            image_list = page.get_images()
            
            for img_index in range(len(image_list)):
                xref = image_list[img_index][0]
                pix = fitz.Pixmap(pdf_document, xref)
                
                # Convertir a PNG
                if pix.n - pix.alpha < 4:  # Grayscale or RGB
                    pix_rgb = pix
                else:  # CMYK
                    pix_rgb = fitz.Pixmap(fitz.csRGB, pix)
                
                # Generar nombre de archivo
                image_name = f"{module_name}_page{page_num + 1}_img{img_index + 1}.png"
                output_path = os.path.join(output_dir, image_name)
                
                # Guardar imagen
                pix_rgb.save(output_path)
                image_count += 1
                print(f"    ✓ Extraída imagen: {image_name}")
        
        pdf_document.close()
        return image_count
        
    except Exception as e:
        print(f"    ✗ Error procesando PDF: {str(e)}")
        return 0

def main():
    """Procesa todos los PDFs en source-pdfs"""
    
    # Definir rutas
    project_root = Path(__file__).parent.parent
    source_root = project_root / "docs" / "assets" / "source-pdfs"
    static_root = project_root / "static" / "img"
    
    print("=" * 60)
    print("EXTRACTOR DE IMÁGENES DE PDFs")
    print("=" * 60)
    
    if not source_root.exists():
        print(f"✗ Carpeta de fuente no encontrada: {source_root}")
        sys.exit(1)
    
    total_images = 0
    
    # Procesar cada módulo
    for module_key, module_name in MODULES.items():
        module_dir = source_root / module_key
        
        if not module_dir.exists():
            print(f"\n⚠ Carpeta no existe: {module_dir}")
            continue
        
        # Buscar PDFs en la carpeta del módulo
        pdf_files = list(module_dir.glob("*.pdf"))
        
        if not pdf_files:
            print(f"\n⚠ Sin PDFs en: {module_key}/")
            continue
        
        print(f"\n📋 Módulo: {module_name}")
        print(f"   Carpeta: {module_key}/")
        
        # Crear carpeta de salida
        output_dir = static_root / module_key
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Procesar cada PDF
        module_images = 0
        for pdf_file in pdf_files:
            images_extracted = extract_images_from_pdf(str(pdf_file), str(output_dir), module_key)
            module_images += images_extracted
        
        total_images += module_images
        print(f"   Total imágenes extraídas: {module_images}")
    
    print("\n" + "=" * 60)
    print(f"✅ PROCESO COMPLETADO")
    print(f"   Total de imágenes extraídas: {total_images}")
    print("=" * 60)
    
    # Mostrar próximos pasos
    if total_images > 0:
        print("\n📌 Próximos pasos:")
        print("   1. Las imágenes están en: static/img/{modulo}/")
        print("   2. Ejecuta: python scripts/insert_pdf_images_to_docs.py")
        print("   3. Esto insertará las imágenes automáticamente en los markdown")

if __name__ == "__main__":
    # Verificar si PyMuPDF está instalado
    try:
        import fitz
    except ImportError:
        print("⚠ PyMuPDF no está instalado")
        print("Instálalo con: pip install PyMuPDF")
        sys.exit(1)
    
    main()

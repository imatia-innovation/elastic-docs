#!/usr/bin/env python3
"""
Script para convertir PDFs de sources/ a Markdown procesado
Fase 1: Extrae PDFs, genera archivos raw por página
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple
import json
import re

try:
    import PyPDF2
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError:
    print("ERROR: Instala las dependencias con:")
    print("  pip install PyPDF2 pdf2image pillow pytesseract")
    print("  (y descargar Tesseract OCR si usas OCR)")
    sys.exit(1)


class PDFExtractor:
    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.sources_dir = self.workspace / "docs" / "assets" / "source-pdfs"
        self.docs_dir = self.workspace / "docs"
        self.raw_dir = self.docs_dir / "_raw"
        self.assets_dir = self.docs_dir / "assets" / "pdf-images"
        
        # Crear directorios
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        
        self.metadata = {}
    
    def find_pdfs(self) -> Dict[str, List[Path]]:
        """Encuentra todos los PDFs organizados por módulo"""
        pdfs_by_module = {}
        
        for module_dir in sorted(self.sources_dir.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith('.'):
                continue
            
            pdf_files = list(module_dir.glob("*.pdf"))
            if pdf_files:
                pdfs_by_module[module_dir.name] = sorted(pdf_files)
        
        return pdfs_by_module
    
    def extract_text_from_pdf(self, pdf_path: Path) -> List[str]:
        """Extrae texto de cada página del PDF"""
        texts = []
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page_num, page in enumerate(reader.pages):
                    text = page.extract_text()
                    # Detectar si la página está vacía o es sólo escaneo
                    if len(text.strip()) < 20:
                        text = f"[TODO_OCR] Página {page_num + 1} - Posible escaneo sin OCR\n\n{text}"
                    texts.append(text)
        except Exception as e:
            print(f"  ERROR extrayendo texto de {pdf_path.name}: {e}")
            texts.append(f"[ERROR_EXTRACTION] {str(e)}")
        
        return texts
    
    def extract_images_from_pdf(self, pdf_path: Path, module_name: str) -> Dict[int, str]:
        """Extrae imágenes de cada página del PDF"""
        images_map = {}
        
        try:
            images = convert_from_path(pdf_path, dpi=150)
            for page_num, image in enumerate(images, 1):
                # Guardar imagen
                img_filename = f"{pdf_path.stem}_page_{page_num:03d}.png"
                img_path = self.assets_dir / module_name
                img_path.mkdir(parents=True, exist_ok=True)
                
                full_img_path = img_path / img_filename
                image.save(full_img_path, 'PNG')
                
                # Ruta relativa para Markdown
                rel_path = f"/img/pdf-images/{module_name}/{img_filename}"
                images_map[page_num] = rel_path
        except Exception as e:
            print(f"  ERROR extrayendo imágenes de {pdf_path.name}: {e}")
        
        return images_map
    
    def create_raw_markdown(self, pdf_path: Path, module_name: str, 
                           texts: List[str], images_map: Dict[int, str]) -> None:
        """Crea archivo .md raw por página"""
        
        filename_base = pdf_path.stem
        raw_module_dir = self.raw_dir / module_name
        raw_module_dir.mkdir(parents=True, exist_ok=True)
        
        for page_num, text in enumerate(texts, 1):
            raw_filename = f"{page_num:03d}_{filename_base}.md"
            raw_path = raw_module_dir / raw_filename
            
            # Contenido
            content = f"""# {filename_base} - Página {page_num}

**Origen:** `{pdf_path.relative_to(self.workspace)}`
**Módulo:** {module_name}

---

## Texto extraído

{text}

"""
            
            # Agregar imagen si existe
            if page_num in images_map:
                content += f"\n## Imagen de la página\n\n![Página {page_num}]({images_map[page_num]})\n"
            
            # Escribir
            with open(raw_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"    ✓ {raw_filename}")
        
        # Guardar metadata
        self.metadata[f"{module_name}/{filename_base}"] = {
            "pages": len(texts),
            "pdf_path": str(pdf_path.relative_to(self.workspace)),
            "has_images": len(images_map) > 0,
            "image_pages": list(images_map.keys())
        }
    
    def process_all_pdfs(self) -> None:
        """Procesa todos los PDFs encontrados"""
        pdfs = self.find_pdfs()
        
        print("\n" + "="*70)
        print("FASE 1: Extrayendo PDFs a Markdown raw")
        print("="*70)
        
        total_files = sum(len(files) for files in pdfs.values())
        print(f"\nEncontrados {total_files} PDFs organizados en {len(pdfs)} módulos\n")
        
        for module_name in sorted(pdfs.keys()):
            print(f"\n📁 Módulo: {module_name}")
            print("-" * 70)
            
            for pdf_path in pdfs[module_name]:
                print(f"  📄 Procesando: {pdf_path.name}")
                
                # Extraer texto
                texts = self.extract_text_from_pdf(pdf_path)
                print(f"    ✓ {len(texts)} páginas de texto")
                
                # Extraer imágenes
                images_map = self.extract_images_from_pdf(pdf_path, module_name)
                if images_map:
                    print(f"    ✓ {len(images_map)} imágenes extraídas")
                
                # Crear raw markdown
                self.create_raw_markdown(pdf_path, module_name, texts, images_map)
        
        # Guardar metadata
        metadata_path = self.raw_dir / "_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
        
        print("\n" + "="*70)
        print("✅ FASE 1 COMPLETADA")
        print("="*70)
        print(f"\n✓ Archivos raw generados en: {self.raw_dir}")
        print(f"✓ Imágenes extraídas en: {self.assets_dir}")
        print(f"✓ Metadata guardada en: {metadata_path}")
        print("\nPróximo paso: Ejecutar fase 2 para generar Markdown final")


def main():
    # Encontrar raíz del workspace
    current_dir = Path(__file__).parent.parent
    
    if not (current_dir / "docs").exists():
        print(f"ERROR: No se encontró carpeta docs en {current_dir}")
        sys.exit(1)
    
    extractor = PDFExtractor(current_dir)
    extractor.process_all_pdfs()


if __name__ == "__main__":
    main()

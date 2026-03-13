#!/usr/bin/env python3
"""
Fase 2: Limpia archivos raw de PDFs y genera Markdown final estructurado
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple
from collections import defaultdict


class MarkdownGenerator:
    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.docs_dir = self.workspace / "docs"
        self.raw_dir = self.docs_dir / "_raw"
        self.metadata_file = self.raw_dir / "_metadata.json"
        
        if not self.metadata_file.exists():
            print("ERROR: No se encontró _metadata.json de Fase 1")
            raise FileNotFoundError("Ejecuta Fase 1 primero")
        
        with open(self.metadata_file) as f:
            self.metadata = json.load(f)
        
        self.generated_files = defaultdict(list)
    
    def read_raw_files_for_module(self, module_name: str) -> List[Tuple[int, str]]:
        """Lee todos los raw files de un módulo en orden"""
        module_raw_dir = self.raw_dir / module_name
        
        if not module_raw_dir.exists():
            return []
        
        files = []
        for raw_file in sorted(module_raw_dir.glob("*.md")):
            # Extraer número de página
            match = re.match(r'(\d+)_', raw_file.name)
            if match:
                page_num = int(match.group(1))
                with open(raw_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                files.append((page_num, content))
        
        return files
    
    def clean_pdf_text(self, text: str) -> str:
        """Limpia artefactos comunes de extracción PDF"""
        
        # Remover líneas repetidas excesivas
        lines = text.split('\n')
        cleaned_lines = []
        prev_line = ""
        
        for line in lines:
            # Evitar líneas duplicadas consecutivas
            if line.strip() != prev_line.strip() or len(cleaned_lines) == 0:
                cleaned_lines.append(line)
            prev_line = line
        
        text = '\n'.join(cleaned_lines)
        
        # Limpiar espacios excesivos
        text = re.sub(r' {3,}', '  ', text)  # Múltiples espacios → 2 espacios
        text = re.sub(r'\n{4,}', '\n\n', text)  # Múltiples líneas vacías → 2
        
        # Remover líneas de separación de PDF (patrones comunes)
        text = re.sub(r'^[-_=\*]{3,}$', '', text, flags=re.MULTILINE)
        
        # Limpiar referencias de página
        text = re.sub(r'Página \d+', '', text)
        text = re.sub(r'P\. \d+', '', text)
        
        # Remover TODO_OCR si hay contenido
        if len(text.strip()) > 100:
            text = text.replace('[TODO_OCR]', '')
        
        return text.strip()
    
    def detect_section_structure(self, text: str) -> List[Tuple[str, str]]:
        """Detecta títulos y subsecciones en el texto extraído"""
        
        lines = text.split('\n')
        sections = []
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Detectar patrones de títulos
            if len(stripped) < 100 and stripped:  # Títulos suelen ser cortos
                # Títulos en mayúsculas
                if stripped.isupper() and len(stripped) > 5:
                    sections.append(('##', stripped))
                # Títulos con patrón numérico
                elif re.match(r'^\d+[\.\)\-]\s+', stripped):
                    sections.append(('###', re.sub(r'^\d+[\.\)\-]\s+', '', stripped)))
                # Títulos entre guiones o asteriscos
                elif re.match(r'^[\*_]{2,}.*[\*_]{2,}$', stripped):
                    sections.append(('##', stripped.strip('*_ ')))
        
        return sections
    
    def generate_module_docs(self, module_name: str) -> None:
        """Genera documentación final para un módulo"""
        
        print(f"\n  📝 Generando documentación para: {module_name}")
        
        # Leer todos los raw files
        raw_files = self.read_raw_files_for_module(module_name)
        if not raw_files:
            print(f"    ⚠️  No hay archivos raw para {module_name}")
            return
        
        # Combinar todo el contenido
        full_content = []
        section_titles = {}
        
        for page_num, raw_content in raw_files:
            # Limpiar contenido
            cleaned = self.clean_pdf_text(raw_content)
            
            if cleaned and '[ERROR' not in cleaned:
                full_content.append(cleaned)
        
        if not full_content:
            print(f"    ⚠️  Sin contenido válido para {module_name}")
            return
        
        # Combinar todo
        combined_text = '\n\n---\n\n'.join(full_content)
        
        # Crear carpeta del módulo si no existe
        module_dir = self.docs_dir / module_name
        module_dir.mkdir(parents=True, exist_ok=True)
        
        # Número total de páginas
        total_pages = len(raw_files)
        
        # Generar un archivo README para ahora
        readme_path = module_dir / "_readme_from_pdf.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"""# {module_name.upper()} - Contenido extraído de PDF

> **Nota:** Esta es una extracción automática de PDF a Markdown. 
> Requiere revisión y reorganización manual según estructura deseada.

**Estadísticas:**
- Páginas procesadas: {total_pages}
- Tamaño del contenido: {len(combined_text)} caracteres

## Contenido extraído

{combined_text}

---

## Próximos pasos

1. ✓ Revisar y corriegir el texto
2. ⏳ Reorganizar en secciones temáticas
3. ⏳ Extraer tablas y formatear correctamente
4. ⏳ Agregar imágenes desde `docs/assets/pdf-images/{module_name}/`
5. ⏳ Crear estructura final con archivos temáticos
6. ⏳ Actualizar tabla de contenidos

## Módulo: {module_name}

**PDF original:** `build/sources/{module_name}/`
**Raw files:** `docs/_raw/{module_name}/`
**Assets:** `docs/assets/pdf-images/{module_name}/`
""")
        
        print(f"    ✓ Archivo generado: {readme_path.relative_to(self.docs_dir)}")
        self.generated_files[module_name].append(str(readme_path))
    
    def process_all_modules(self) -> None:
        """Procesa todos los módulos"""
        
        print("\n" + "="*70)
        print("FASE 2: Limpieza y reorganización de documentación")
        print("="*70)
        
        # Extraer módulos únicos
        modules = set()
        for key in self.metadata.keys():
            module = key.split('/')[0]
            modules.add(module)
        
        print(f"\nProcesando {len(modules)} módulos...\n")
        
        for module_name in sorted(modules):
            try:
                self.generate_module_docs(module_name)
            except Exception as e:
                print(f"    ❌ Error procesando {module_name}: {e}")
        
        # Resumen
        print("\n" + "="*70)
        print("✅ FASE 2 COMPLETADA")
        print("="*70)
        
        total_generated = sum(len(files) for files in self.generated_files.values())
        print(f"\n✓ Generados {total_generated} archivos")
        print(f"✓ Ubicación: {self.docs_dir}")
        
        print("\n📋 Resumen por módulo:")
        for module_name in sorted(self.generated_files.keys()):
            print(f"   - {module_name}: {len(self.generated_files[module_name])} archivo(s)")
        
        print("\n⏭️  Próximos pasos:")
        print("   1. Revisa los archivos generados en docs/{modulo}/")
        print("   2. Reorganiza el contenido según estructura deseada")
        print("   3. Crea intro.md con índice del módulo")
        print("   4. Agrega imágenes desde docs/assets/pdf-images/")
        print("   5. Genera _category_.json para cada módulo (Docusaurus)")


def main():
    current_dir = Path(__file__).parent.parent
    
    if not (current_dir / "docs" / "_raw").exists():
        print("ERROR: No se encontró docs/_raw")
        print("Ejecuta Fase 1 primero: python scripts/pdf_to_markdown_extractor.py")
        exit(1)
    
    generator = MarkdownGenerator(current_dir)
    generator.process_all_modules()


if __name__ == "__main__":
    main()

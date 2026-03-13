#!/usr/bin/env python3
"""
Script para limpiar y hacer compatible el contenido de los PDFs con MDX/Docusaurus
Escapa caracteres problemáticos y mejora la estructura
"""

import re
from pathlib import Path
from typing import List

class MDXCleaner:
    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.docs_dir = self.workspace / "docs"
        self.modules = [
            "almacen", "antifraude", "calidad", "compras", "crm", 
            "finanzas", "guia_de_uso", "laboral", "produccion", 
            "trazabilidad", "ventas"
        ]
    
    def clean_mdx_content(self, content: str) -> str:
        """Limpia contenido para que sea compatible con MDX"""
        
        # Remover frontmatter duplicado (excepto el primero)
        content = re.sub(r'^---\n.*?\n---\n\n(?=---)', '', content, flags=re.DOTALL)
        
        # Escapar líneas que empiezan con caracteres especiales que MDX interpreta
        # Esto incluye líneas que comienzan con - (que MDX interpreta como JSX)
        lines = content.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Si la línea es una línea de separación ASCII (muchos -, =, etc)
            if re.match(r'^[\-=_]{5,}$', line):
                # Convertirla a un comentario o dejarla vacía
                cleaned_lines.append('')
            # Si la línea tiene caracteres especiales al inicio que causan problemas
            elif re.match(r'^[\-]{1,}\s*[a-zA-Z]', line):
                # Es probable que sea una lista, déjalo como está
                cleaned_lines.append(line)
            else:
                cleaned_lines.append(line)
        
        content = '\n'.join(cleaned_lines)
        
        # Remover múltiples líneas vacías
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        # Remover espacios al final de líneas
        content = '\n'.join(line.rstrip() for line in content.split('\n'))
        
        # Remover notas de generación automática redundantes
        content = re.sub(r'\n+> \*\*Nota:\*\*\s+Esta es una extracción.*?\n\n', '\n\n', content, flags=re.DOTALL)
        
        return content.strip()
    
    def process_reference_file(self, module_dir: Path, module_name: str) -> bool:
        """Procesa un archivo de referencia completa"""
        ref_file = module_dir / "00-referencia-completa.md"
        
        if not ref_file.exists():
            return False
        
        try:
            with open(ref_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            print(f"    ERROR: No se pudo leer {ref_file}")
            return False
        
        # Limpiar contenido
        cleaned_content = self.clean_mdx_content(content)
        
        # Escribir de vuelta
        try:
            with open(ref_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            print(f"    ✓ Limpiado: 00-referencia-completa.md")
            return True
        except Exception as e:
            print(f"    ERROR escribiendo archivo: {e}")
            return False
    
    def process_all_modules(self) -> None:
        """Procesa todos los módulos"""
        print("\n" + "="*70)
        print("LIMPIANDO CONTENIDO PARA COMPATIBILIDAD CON MDX")
        print("="*70 + "\n")
        
        success_count = 0
        for module_name in self.modules:
            module_dir = self.docs_dir / module_name
            
            if not module_dir.exists():
                continue
            
            print(f"📦 Limpiando módulo: {module_name}")
            if self.process_reference_file(module_dir, module_name):
                success_count += 1
            print()
        
        print("="*70)
        print(f"✅ LIMPIEZA COMPLETADA - {success_count} módulos procesados")
        print("="*70)

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    
    cleaner = MDXCleaner(workspace_root)
    cleaner.process_all_modules()

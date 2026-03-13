#!/usr/bin/env python3
"""
Solución definitiva: Convertir archivos de referencia a format o seguro para Docusaurus
Usando bloques de código o formato seguro
"""

import re
from pathlib import Path
from typing import List

class SafeReferenceGenerator:
    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.docs_dir = self.workspace / "docs"
        self.modules = [
            "almacen", "antifraude", "calidad", "compras", "crm", 
            "finanzas", "guia_de_uso", "laboral", "produccion", 
            "trazabilidad", "ventas"
        ]
    
    def escape_mdx_content(self, content: str) -> str:
        """Escapa contenido MDX reemplazando caracteres problemáticos"""
        
        lines = []
        in_code_block = False
        consecutive_special = 0
        
        for line_num, line in enumerate(content.split('\n'), 1):
            original_line = line
            
            # Detectar líneas que son separadores (muchos -, =, _, etc)
            if re.match(r'^[\-=_\*]{5,}$', line.strip()):
                # Reemplazarlos con texto alternativo
                lines.append('')  # Línea vacía
                continue
            
            # Detectar líneas que comienzan con guiones seguidos de no-espacio
            # Esto es lo que causa el error "Unexpected character -"
            if re.match(r'^-[a-zA-Z_$]', line):
                # Añadir espacio para que no sea ambiguo
                line = '\\' + line
            
            # Detectar líneas con problemas JSX (caracteres especiales como =)
            if '<' in line and '=' in line and re.search(r'<[a-zA-Z_].*?=', line):
                # Esto podría ser JSX, escaparlo
                line = line.replace('<', '\\<').replace('>', '\\>')
            
            lines.append(line)
        
        return '\n'.join(lines)
    
    def wrap_in_safe_format(self, content: str) -> str:
        """Envuelve el contenido en un formato seguro"""
        # Extraer frontmatter si existe
        frontmatter_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
        frontmatter = ''
        body = content
        
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            body = content[len(frontmatter):]
        
        # Limpiar el cuerpo
        body = self._clean_body(body)
        
        # Reconstruir con frontmatter
        result = frontmatter + '\n' + body
        
        return result.strip()
    
    def _clean_body(self, content: str) -> str:
        """Limpia el cuerpo del contenido de forma agresiva"""
        
        lines = content.split('\n')
        cleaned = []
        
        for line in lines:
            # Remover líneas que son solo caracteres especiales
            if re.match(r'^[\-=_\*]{3,}$', line.strip()):
                continue
            
            # Remover líneas que empiezan con "-" seguido de letra sin espacio
            if re.match(r'^-[a-zA-Z]', line):
                # Convertirlo a una lista proper
                line = '- ' + line[1:]
            
            # Escapar secuencias problemáticas de JSX
            # Buscar patrones como <something=
            if re.search(r'<[a-zA-Z_]\w+\s*=', line):
                line = line.replace('<', '`<').replace('>', '>`')
            
            cleaned.append(line)
        
        # Remover líneas vacías múltiples
        result = '\n'.join(cleaned)
        result = re.sub(r'\n\n\n+', '\n\n', result)
        
        return result.strip()
    
    def process_reference_file(self, module_dir: Path, module_name: str) -> bool:
        """Procesa un archivo de referencia completa de forma segura"""
        ref_file = module_dir / "00-referencia-completa.md"
        
        if not ref_file.exists():
            return False
        
        try:
            with open(ref_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            print(f"    ERROR: No se pudo leer {ref_file}")
            return False
        
        # Procesar contenido
        safe_content = self.wrap_in_safe_format(content)
        
        # Escribir de vuelta
        try:
            with open(ref_file, 'w', encoding='utf-8') as f:
                f.write(safe_content)
            print(f"    ✓ Procesado de forma segura: 00-referencia-completa.md")
            return True
        except Exception as e:
            print(f"    ERROR escribiendo archivo: {e}")
            return False
    
    def process_all_modules(self) -> None:
        """Procesa todos los módulos"""
        print("\n" + "="*70)
        print("CONVIRTIENDO A FORMATO SEGURO PARA DOCUSAURUS")
        print("="*70 + "\n")
        
        success_count = 0
        for module_name in self.modules:
            module_dir = self.docs_dir / module_name
            
            if not module_dir.exists():
                continue
            
            print(f"📦 Procesando módulo: {module_name}")
            if self.process_reference_file(module_dir, module_name):
                success_count += 1
            print()
        
        print("="*70)
        print(f"✅ CONVERSIÓN COMPLETADA - {success_count} módulos procesados")
        print("="*70)

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    
    converter = SafeReferenceGenerator(workspace_root)
    converter.process_all_modules()

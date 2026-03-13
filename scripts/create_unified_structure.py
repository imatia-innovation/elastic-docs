#!/usr/bin/env python3
"""
Script para crear estructura unificada en todos los módulos
- intro.md: Resumen del módulo
- Archivos temáticos individuales
- _category_.json para Docusaurus
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
import json

class ModuleStructurer:
    def __init__(self, workspace_root: Path):
        self.workspace = workspace_root
        self.docs_dir = self.workspace / "docs"
        
        # Definir módulos existentes
        self.modules = [
            "almacen", "antifraude", "calidad", "compras", "crm", 
            "finanzas", "guia_de_uso", "laboral", "produccion", 
            "trazabilidad", "ventas"
        ]
        
        # Mapeos de nombre legible para módulos
        self.module_names = {
            "almacen": "Almacén",
            "antifraude": "Antifraude",
            "calidad": "Calidad",
            "compras": "Compras",
            "crm": "CRM",
            "finanzas": "Finanzas",
            "guia_de_uso": "Guía de Uso",
            "laboral": "Laboral",
            "produccion": "Producción",
            "trazabilidad": "Trazabilidad",
            "ventas": "Ventas"
        }
    
    def extract_sections(self, content: str) -> List[Tuple[str, str]]:
        """Extrae secciones principales del contenido"""
        sections = []
        
        # Buscar líneas con encabezados (# nivel bajo)
        lines = content.split('\n')
        current_section = None
        current_content = []
        
        for i, line in enumerate(lines):
            # Detectar secciones por encabezados principales (## o ###)
            if re.match(r'^###?\s+(.+)', line):
                # Guardar sección anterior
                if current_section and current_content:
                    section_text = '\n'.join(current_content).strip()
                    if len(section_text) > 100:  # Solo si tiene contenido significativo
                        sections.append((current_section, section_text))
                
                # Iniciar nueva sección
                match = re.match(r'^##?\s+(.+)', line)
                if match:
                    current_section = match.group(1).strip()
                    current_content = []
            elif current_section:
                current_content.append(line)
        
        # Guardar última sección
        if current_section and current_content:
            section_text = '\n'.join(current_content).strip()
            if len(section_text) > 100:
                sections.append((current_section, section_text))
        
        return sections
    
    def generate_intro(self, module_name: str, readme_file: Path) -> str:
        """Genera intro.md basado en el contenido del PDF"""
        try:
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            return self._default_intro(module_name)
        
        # Extraer primeras líneas significativas como descripción
        lines = content.split('\n')
        description_lines = []
        
        for line in lines:
            # Saltar líneas vacías y de formato
            if line.strip() and not line.startswith('#') and not line.startswith('**'):
                if len(description_lines) < 3:
                    description_lines.append(line.strip())
                if len(description_lines) >= 3:
                    break
        
        description = ' '.join(description_lines)[:200]  # Primeras 200 caracteres
        
        # Generar intro
        intro_content = f"""---
title: Introducción
description: Módulo {self.module_names.get(module_name, module_name)}
sidebar_position: 1
---

# {self.module_names.get(module_name, module_name).upper()}

## Descripción General

Este módulo contiene toda la información y guías de uso para el módulo de **{self.module_names.get(module_name, module_name)}** en Elastic Business.

{description}

## Contenidos del Módulo

En las siguientes secciones encontrarás:

- **Referencia completa**: Documentación detallada de todas las funcionalidades
- **Guías de configuración**: Pasos para configurar los parámetros del módulo
- **Procedimientos**: Procesos y flujos de trabajo principales
- **Ejemplos prácticos**: Casos de uso reales y ejemplos aplicables

## Acceso Rápido

Utiliza el menú lateral (izquierda) para navegar entre las diferentes secciones y subtemas.
"""
        
        return intro_content
    
    def _default_intro(self, module_name: str) -> str:
        """Genera intro por defecto"""
        return f"""---
title: Introducción
description: Módulo {self.module_names.get(module_name, module_name)}
sidebar_position: 1
---

# {self.module_names.get(module_name, module_name).upper()}

## Descripción General

Este módulo contiene toda la información y guías de uso para el módulo de **{self.module_names.get(module_name, module_name)}** en Elastic Business.

## Contenidos del Módulo

En las siguientes secciones encontrarás la documentación completa del módulo, incluyendo:

- Configuración de parámetros
- Procedimientos operativos
- Guías de uso
- Ejemplos prácticos

## Acceso Rápido

Utiliza el menú lateral para navegar entre las diferentes secciones.
"""
    
    def create_reference_file(self, module_name: str, readme_path: Path) -> None:
        """Crea archivo 00-referencia-completa.md con todo el contenido"""
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            print(f"  ERROR: No se pudo leer {readme_path}")
            return
        
        # Limpiar contenido
        content = self._clean_content(content)
        
        # Crear archivo de referencia
        ref_file = readme_path.parent / "00-referencia-completa.md"
        
        reference_content = f"""---
title: Referencia Completa
description: Documentación completa del módulo {self.module_names.get(module_name, module_name)}
sidebar_position: 2
---

# Referencia Completa - {self.module_names.get(module_name, module_name)}

{content}
"""
        
        try:
            with open(ref_file, 'w', encoding='utf-8') as f:
                f.write(reference_content)
            print(f"    ✓ Referencia creatida: {ref_file.name}")
        except Exception as e:
            print(f"    ERROR creando referencia: {e}")
    
    def _clean_content(self, content: str) -> str:
        """Limpia contenido para mejor presentación"""
        # Remover notas de generación automática
        content = re.sub(r'> \*\*Nota:\*\*.*?\n\n', '', content, flags=re.DOTALL)
        content = re.sub(r'Estadísticas.*?\n.*?\n.*?\n\n', '', content, flags=re.DOTALL)
        content = re.sub(r'Contenido extraído.*?\n\n---\n\n', '', content, flags=re.DOTALL)
        
        # Remover duplicados de título
        content = re.sub(r'^# [^#].*?\n\n', '', content, flags=re.MULTILINE)
        
        # Limpiar múltiples nuevas líneas
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        return content.strip()
    
    def create_category_json(self, module_name: str, module_dir: Path) -> None:
        """Crea _category_.json para Docusaurus"""
        category_data = {
            "label": self.module_names.get(module_name, module_name),
            "position": self._get_module_position(module_name),
            "link": {
                "type": "generated-index",
                "description": f"Documentación del módulo de {self.module_names.get(module_name, module_name)}"
            }
        }
        
        category_file = module_dir / "_category_.json"
        
        try:
            with open(category_file, 'w', encoding='utf-8') as f:
                json.dump(category_data, f, ensure_ascii=False, indent=2)
            print(f"    ✓ Categoría creada: _category_.json")
        except Exception as e:
            print(f"    ERROR creando categoría: {e}")
    
    def _get_module_position(self, module_name: str) -> int:
        """Retorna posición del módulo en el menú"""
        positions = {
            "intro": 1,
            "almacen": 2,
            "compras": 3,
            "ventas": 4,
            "produccion": 5,
            "calidad": 6,
            "trazabilidad": 7,
            "crm": 8,
            "laboral": 9,
            "finanzas": 10,
            "guia_de_uso": 11,
            "antifraude": 12,
        }
        return positions.get(module_name, 99)
    
    def delete_old_files(self, module_dir: Path, readme_name: str = "_readme_from_pdf.md") -> None:
        """Elimina archivos viejos"""
        old_files = [
            module_dir / "readme-completo.md.bak",
            module_dir / "_readme_from_pdf.md"
        ]
        
        for file in old_files:
            if file.exists():
                try:
                    file.unlink()
                    print(f"    ✓ Archivo antiguo eliminado: {file.name}")
                except:
                    pass
    
    def process_all_modules(self) -> None:
        """Procesa todos los módulos"""
        print("\n" + "="*70)
        print("CREANDO ESTRUCTURA UNIFICADA PARA TODOS LOS MÓDULOS")
        print("="*70 + "\n")
        
        for module_name in self.modules:
            module_dir = self.docs_dir / module_name
            readme_file = module_dir / "_readme_from_pdf.md"
            
            if not module_dir.exists():
                print(f"⚠️  Módulo no encontrado: {module_name}")
                continue
            
            print(f"📦 Procesando módulo: {module_name}")
            print("-" * 70)
            
            # Crear intro.md
            try:
                intro_content = self.generate_intro(module_name, readme_file)
                intro_file = module_dir / "intro.md"
                
                with open(intro_file, 'w', encoding='utf-8') as f:
                    f.write(intro_content)
                print(f"    ✓ Intro creado: intro.md")
            except Exception as e:
                print(f"    ERROR creando intro: {e}")
            
            # Crear referencia completa
            if readme_file.exists():
                self.create_reference_file(module_name, readme_file)
            
            # Crear _category_.json
            try:
                self.create_category_json(module_name, module_dir)
            except Exception as e:
                print(f"    ERROR creando categoría: {e}")
            
            # Limpiar archivos antiguos
            # self.delete_old_files(module_dir)
            
            print()
        
        print("="*70)
        print("✅ ESTRUCTURA UNIFICADA COMPLETADA")
        print("="*70)
        print("\nProximos pasos:")
        print("1. Revisar intro.md en cada módulo")
        print("2. Personalizar según necesidades específicas")
        print("3. Ejecutar 'docusaurus build' para visualizar cambios")


if __name__ == "__main__":
    # Obtener raíz del workspace
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    
    # Procesar módulos
    structurer = ModuleStructurer(workspace_root)
    structurer.process_all_modules()

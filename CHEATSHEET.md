# ⚡ Referencia Rápida: PDF a Markdown - Checklist

## 🎯 ¿Qué se hizo?

```
✅ Fase 1: Extrajeron 31+ PDFs (~430 páginas) → docs/_raw/
✅ Fase 2: Limpiaron contenido → 12 archivos _readme_from_pdf.md
✅ Fase 3: Ejemplo completo → docs/almacen/ (estructura lista)
✅ Scripts: 3 automatizados + 4 archivos batch
✅ Documentación: Guías completas generadas
```

## 📁 Archivos Nuevos Creados

### Scripts Automatizados

| Script | Propósito | Ejecutar |
|--------|-----------|----------|
| `pdf_to_markdown_extractor.py` | Fase 1: Extraer PDFs | `python scripts/pdf_to_markdown_extractor.py` |
| `markdown_generator_phase2.py` | Fase 2: Limpiar Markdown | `python scripts/markdown_generator_phase2.py` |
| `example_almacen_full_structure.py` | Ejemplo: Almacén completo | `python scripts/example_almacen_full_structure.py` |
| `run_phase1.bat` | Atajo Fase 1 (Windows) | `scripts/run_phase1.bat` |
| `run_phase2.bat` | Atajo Fase 2 (Windows) | `scripts/run_phase2.bat` |
| `install_dependencies.bat` | Instalar librerías | `scripts/install_dependencies.bat` |

### Documentación Generada

| Archivo | Ubicación |
|---------|-----------|
| esta referencia | `PDF_TO_MARKDOWN_GUIDE.md` ← YOU ARE HERE |
| guía completa | `PDF_TO_MARKDOWN_GUIDE.md` |
| resumen técnico | `CONVERSION_SUMMARY.md` |
| README scripts | `scripts/README.md` |

### Contenido Nuevo en docs/

| Carpeta | Archivos | Estado |
|---------|----------|--------|
| `docs/almacen/` | intro + 3 docs + config | ✅ **EJEMPLO COMPLETO** |
| `docs/_raw/` | 92+ archivos raw | ✅ Referencia |
| `docs/{otros}/` | `_readme_from_pdf.md` | ✅ Listos para procesar |
| `docs/assets/pdf-images/` | (vacío sin poppler) | ⚠️ Necesita poppler |

---

## ⚙️ Cómo Usar

### Opción A: Rápida (15 min/módulo)

```bash
# 1. Abrir archivo raw
code docs/{modulo}/_readme_from_pdf.md

# 2. Copiar estructura del almacén
cp docs/almacen/*.md docs/{modulo}/

# 3. Editar con nuevo contenido
code docs/{modulo}/intro.md

# 4. Compilar
npm run build
```

### Opción B: Profesional (60-120 min/módulo)

1. Leer `_readme_from_pdf.md`
2. Crear intro.md con tabla de contenidos
3. Extraer 3-5 temas principales → 01-*.md, 02-*.md, etc.
4. Crear _category_.json
5. Agregar imágenes si existen
6. Validar en Docusaurus

---

## 📊 Estado Actual

### Módulos Completados
- ✅ **almacen** - intro + 3 temas + config
- ✅ **ventas** - 14 archivos manuales

### Módulos en Fase Raw
- ⏳ **compras**, **crm**, **finanzas**, **guia_de_uso**
- ⏳ **laboral**, **old**, **produccion**, **programacion**, **trazabilidad**
- ⏳ **aplicación**, **calidad**

### Tamaño Aproximado
- Total: 430 páginas → ~500 KB de contenido

---

## 🚀 Próximos Pasos

### Esta Semana
```
[ ] Revisar docs/almacen/ (ejemplo completo)
[ ] Procesar docs/compras/ (copiar estructura del almacén)
[ ] Procesar docs/crm/ (mismo proceso)
[ ] Validar npm run build sin errores
```

### Próximas 2 Semanas
```
[ ] Completar 3-4 módulos más
[ ] Procesar imágenes (instalar poppler si es necesario)
[ ] Crear índice general en docs/index.md
[ ] Agregar cross-links entre módulos
```

### Mes 1
```
[ ] Completar todos los 13 módulos
[ ] Revisar contenido contra PDFs
[ ] Optimizar estructura y navegación
[ ] Publicar wiki v1.0
```

---

## 💾 Archivos Críticos

### No tocar / Usar como referencia
```
build/sources/          ← PDFs originales (BACKUP)
docs/_raw/              ← Archivos intermedios (REFERENCIA)
docs/old/               ← Documento antiguo (FALLBACK)
```

### Editar activamente
```
docs/almacen/           ← MODELO (copiable)
docs/{tu_modulo}/       ← TRABAJO
scripts/                ← REUTILIZABLE
```

---

## 🔍 Quick Troubleshooting

| Problema | Solución |
|----------|----------|
| No se ve módulo en Docusaurus | Verifica `_category_.json` existe |
| Imágenes no aparecen | Copia a `docs/assets/` y usa `/img/...` |
| Links rotos | Usa rutas relativas: `[Link](01-file.md)` |
| Contenido incompleto | Revisar `_readme_from_pdf.md` o `docs/old/` |
| npm build falla | Verifica caracteres especiales en nombres |

---

## 📞 Contacto y Recursos

- **Documentación detallada:** `PDF_TO_MARKDOWN_GUIDE.md`
- **Resumen técnico:** `CONVERSION_SUMMARY.md`
- **Scripts help:** `scripts/README.md`
- **Ejemplo modelo:** `docs/almacen/`

---

## ✨ Bonus: Automatizar Otros Módulos

Si necesitas procesar un módulo igual que almacén:

```bash
# 1. Crear estructura
python scripts/example_almacen_full_structure.py

# 2. Adaptar el script Python para tu módulo
# (Copiar `example_almacen_full_structure.py` y editarlo)

# 3. Ejecutar
python scripts/example_{tu_modulo}.py
```

Ejemplo: para COMPRAS:
```python
# Cambiar en example_almacen_full_structure.py:
# - "almacen" → "compras"  
# - Título → "Compras"
# - Secciones → Que tengas en tu PDF
```

---

**¡Todo listo para continuar! 🎉**

Próximo paso: Abre `docs/almacen/intro.md` para ver el ejemplo completo.

# PDF to Markdown Conversion Pipeline

Proceso de dos fases para convertir todos los PDFs de `build/sources/` a markdown estructurado en `docs/`.

## Estructura

```
scripts/
├── install_dependencies.bat    # Instala PyPDF2, pdf2image, pillow
├── run_phase1.bat             # Ejecuta extracción de PDFs
├── pdf_to_markdown_extractor.py     # Script de Fase 1
└── markdown_generator_phase2.py     # Script de Fase 2 (próximamente)
```

## FASE 1: Extracción de PDFs

### Paso 1: Instalar dependencias

```bash
# Opción A: Hacer doble-click en install_dependencies.bat
# O manualmente:

pip install PyPDF2 pdf2image pillow
```

**Nota sobre OCR (Tesseract):**
- Si necesitas OCR para PDFs escaneados:
  - Descarga desde: https://github.com/UB-Mannheim/tesseract/wiki
  - O: `choco install tesseract` (si tienes Chocolatey)

### Paso 2: Ejecutar Fase 1

```bash
# Opción A: Doble-click en run_phase1.bat
# Opción B: Manualmente en terminal:

python scripts/pdf_to_markdown_extractor.py
```

### Salida de Fase 1

El script genera:

#### `docs/_raw/` - Archivos intermedios
```
_raw/
├── _metadata.json              # Metadata de extracción
├── almacen/
│   ├── 001_Modulo_almacen.md
│   ├── 002_Modulo_almacen.md
│   └── ...
├── ventas/
│   ├── 001_Ley_antifraude.md
│   ├── 002_Modulo_ventas.md
│   └── ...
└── {modulo}/
    └── {page:03d}_{filename}.md
```

Cada archivo contiene:
- Metadatos (origen, módulo, página)
- Texto extraído del PDF
- [TODO_OCR] si la página parecía ser escaneo
- Ruta a imagen de página si se extrajo

#### `docs/assets/pdf-images/` - Imágenes
```
pdf-images/
├── almacen/
│   ├── Modulo_almacen_page_001.png
│   └── ...
├── ventas/
│   ├── Ley_antifraude_page_001.png
│   └── ...
└── {modulo}/
    └── {filename}_page_{page:03d}.png
```

## FASE 2: Generación de Markdown Final

*(Próximamente)*

El script `markdown_generator_phase2.py` tomará los archivos `_raw/` y generará:

- `docs/{modulo}/intro.md` - Índice del módulo
- `docs/{modulo}/{tema}.md` - Archivos temáticos
- `docs/index.md` - Índice principal actualizado
- Estructura de carpetas con `_category_.json` para Docusaurus

### Características Fase 2
- ✓ Reconstruye títulos y subtítulos detectando jerarquías
- ✓ Convierte listas rotas por PDF a listas Markdown
- ✓ Organiza contenido por secciones lógicas
- ✓ Inserta imágenes con referencias correctas
- ✓ Marca secciones OCR con `[REVISAR]` para revisión manual
- ✓ Usa `build/sources/old/` como fallback si hay problemas

## Módulos a Procesar

Encontrados en `build/sources/`:

| Módulo | PDFs | Estado |
|--------|------|--------|
| almacen | 4 | ⏳ Pendiente |
| aplicación | ? | ? |
| calidad | ? | ? |
| compras | ? | ? |
| crm | ? | ? |
| finanzas | ? | ? |
| guia_de_uso | ? | ? |
| laboral | ? | ? |
| produccion | ? | ? |
| programacion | ? | ? |
| trazabilidad | ? | ? |
| ventas (*)| 2 | ✅ Manual (requiere Phase 2) |
| versiones | ? | ? |

(*) Ventas ya tiene documentación manual en `docs/ventas/`

## Troubleshooting

### Error: "No module named 'PyPDF2'"
```bash
pip install PyPDF2
```

### Error: "pdf2image not found"
```bash
pip install pdf2image
```

### Error: "Pillow not installed"
```bash
pip install Pillow
```

### Imágenes no se extraen
- Verifica que `poppler` está instalado:
  - Windows: `choco install poppler` o descarga desde http://blog.alivate.com.au/poppler-windows/
  - Linux: `apt install poppler-utils`
  - macOS: `brew install poppler`

### Pages aparecen con [TODO_OCR] pero no son escaneos
- El script detecta páginas con poco texto extraído
- Revisa manualmente si son tablas complejas o imágenes
- Fase 2 te permite marcar estas áreas para revisión manual

## Flujo Completo

```
1. Install dependencies
   ↓
2. Run Phase 1 (PDF extraction)
   ├─ Extrae texto por página
   ├─ Extrae imágenes
   └─ Genera docs/_raw/{module}/*.md
   ↓
3. Run Phase 2 (Markdown cleanup)
   ├─ Lee _raw files
   ├─ Reconstruye estructura
   ├─ Limpia artefactos de PDF
   └─ Genera docs/{module}/*.md
   ↓
4. Manual Review
   ├─ Revisar [TODO_OCR] 
   ├─ Revisar [REVISAR] sections
   └─ Ajustar si es necesario
   ↓
5. Publish
```

## Próximos Pasos

1. ✅ Crea scripts (ya hecho)
2. ⏳ Instala dependencias: `install_dependencies.bat`
3. ⏳ Ejecuta Fase 1: `run_phase1.bat`
4. ⏳ Crea Phase 2 script (markdown_generator_phase2.py)
5. ⏳ Ejecuta Fase 2
6. ⏳ Revisa output en `docs/_raw/` antes de publicar

---

**Autor:** Copilot PDF Conversion Pipeline
**Versión:** 1.0 (Fase 1 lista)
**Última actualización:** 2024

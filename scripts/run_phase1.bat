@echo off
REM Script para ejecutar Fase 1 de extraccion de PDFs

echo.
echo ===============================================
echo FASE 1: Extrayendo PDFs a Markdown raw
echo ===============================================
echo.

REM Cambiar a directorio del script
cd /d "%~dp0.."

python scripts/pdf_to_markdown_extractor.py

if errorlevel 1 (
    echo.
    echo ERROR: Algo fallo durante la extraccion
    pause
    exit /b 1
)

echo.
echo ===============================================
echo FASE 1 completada exitosamente
echo ===============================================
echo.
echo Archivos generados:
echo - docs/_raw/          (archivos markdown intermedios)
echo - docs/assets/pdf-images/ (imagenes extraidas)
echo - docs/_raw/_metadata.json (metadata de extraccion)
echo.
pause

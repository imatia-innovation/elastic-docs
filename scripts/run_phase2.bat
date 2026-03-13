@echo off
REM Script para ejecutar Fase 2 de limpieza y reorganizacion de Markdown

echo.
echo ===============================================
echo FASE 2: Limpieza y reorganizacion de Markdown
echo ===============================================
echo.

REM Cambiar a directorio del script
cd /d "%~dp0.."

python scripts/markdown_generator_phase2.py

if errorlevel 1 (
    echo.
    echo ERROR: Algo fallo durante la generacion
    pause
    exit /b 1
)

echo.
echo ===============================================
echo FASE 2 completada exitosamente
echo ===============================================
echo.
echo Archivos generados en: docs/{modulo}/_readme_from_pdf.md
echo.
echo Proximos pasos:
echo 1. Revisa los archivos en docs/{modulo}/
echo 2. Reorganiza el contenido manualmente
echo 3. Crea intro.md e indices temáticos
echo 4. Agrega imagenes desde docs/assets/pdf-images/
echo.
pause

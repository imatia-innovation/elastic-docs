@echo off
REM Script para instalar dependencias de PDF extraction en Windows

echo.
echo ===============================================
echo Instalando dependencias para extraccion de PDFs
echo ===============================================
echo.

REM Verificar si pip existe
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python/pip no encontrado
    echo Instala Python desde https://www.python.org/
    exit /b 1
)

echo [1/4] Instalando PyPDF2...
python -m pip install PyPDF2 --quiet

echo [2/4] Instalando pdf2image...
python -m pip install pdf2image --quiet

echo [3/4] Instalando Pillow...
python -m pip install Pillow --quiet

echo.
echo ===============================================
echo OK: Dependencias instaladas
echo ===============================================
echo.
echo Nota: Para OCR necesitarás Tesseract opcional
echo   - Descarga desde: https://github.com/UB-Mannheim/tesseract/wiki
echo   - O instala: choco install tesseract
echo.

pause

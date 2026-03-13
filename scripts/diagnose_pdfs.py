#!/usr/bin/env python3
"""
Script para diagnosticar la ubicación de PDFs
"""

from pathlib import Path
import os

def main():
    project_root = Path(__file__).parent.parent
    source_root = project_root / "docs" / "assets" / "source-pdfs"
    
    print("=" * 70)
    print("DIAGNÓSTICO DE PDFs")
    print("=" * 70)
    
    print(f"\n📁 Buscando PDFs en: {source_root}")
    print(f"   Existe carpeta: {source_root.exists()}\n")
    
    modules = ["almacen", "ventas", "compras", "finanzas", "crm", "laboral", "produccion", "trazabilidad", "calidad", "guia_de_uso"]
    
    total_pdfs = 0
    
    for module in modules:
        module_dir = source_root / module
        
        if not module_dir.exists():
            print(f"⚠ {module:20} - Carpeta no existe")
            continue
        
        # Buscar PDFs
        pdfs = list(module_dir.glob("*.pdf"))
        
        if pdfs:
            print(f"✓ {module:20} - {len(pdfs)} PDF(s):")
            for pdf in pdfs:
                size_mb = pdf.stat().st_size / (1024 * 1024)
                print(f"    • {pdf.name} ({size_mb:.2f} MB)")
            total_pdfs += len(pdfs)
        else:
            print(f"  {module:20} - Sin PDFs")
    
    print("\n" + "=" * 70)
    print(f"TOTAL: {total_pdfs} archivos PDF encontrados")
    print("=" * 70)
    
    if total_pdfs == 0:
        print("\n⚠ No se encontraron PDFs. Verifica que:")
        print("  1. Los PDFs están en docs/assets/source-pdfs/{modulo}/")
        print("  2. La carpeta fue sincronizada correctamente")
        print("  3. Los archivos tienen extensión .pdf")

if __name__ == "__main__":
    main()

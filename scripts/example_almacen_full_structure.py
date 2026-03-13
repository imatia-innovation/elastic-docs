#!/usr/bin/env python3
"""
Script de ejemplo: Convierte módulo ALMACEN en documentación final estructurada
Usa esto como plantilla para otros módulos
"""

import re
from pathlib import Path


def create_almacen_structure():
    """Crea estructura completa del módulo almacén"""
    
    workspace = Path(__file__).parent.parent
    almacen_dir = workspace / "docs" / "almacen"
    almacen_dir.mkdir(exist_ok=True)
    
    # Leer contenido raw
    readme_path = almacen_dir / "_readme_from_pdf.md"
    if not readme_path.exists():
        print("ERROR: No existe _readme_from_pdf.md")
        print("Ejecuta Fase 2 primero")
        return
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
    
    print("\n" + "="*70)
    print("EJEMPLO: Generando estructura para módulo ALMACEN")
    print("="*70)
    
    # 1. CREAR INTRO.MD
    intro_content = """# Almacén

Manual completo del **módulo de almacén** de Elastic Business ERP.

El módulo de almacén permite gesionar el inventario, parámetros de artículos, costes y niveles de stock de seguridad.

## Contenido Principal

- [Parámetros](01-parametros.md) - Configuración de parámetros para generar códigos y descripciones de artículos
- [Modelo de Costes](02-modelo-costes.md) - Configuración de tres modelos de cálculo de costes
- [Stock de Seguridad](03-stock-seguridad.md) - Definición de niveles mínimos de inventario

## Características

✓ **Parámetros configurables** - Define valores para generar códigos únicos  
✓ **Modelos de costes flexibles** - Básico, con sobrecostes, o personalizado  
✓ **Control de stock** - Establece niveles de seguridad automáticos  

## Documentación Relacionada

- Ver también: [Compras](/docs/compras) - Recepción de mercancía
- Ver también: [Producción](/docs/produccion) - Consumo de materiales
- Ver también: [Finanzas](/docs/finanzas) - Valoración de inventarios
"""
    
    intro_path = almacen_dir / "intro.md"
    with open(intro_path, 'w', encoding='utf-8') as f:
        f.write(intro_content)
    print(f"✓ Creado: intro.md")
    
    # 2. CREAR 01-PARAMETROS.MD
    parametros_content = """# Parámetros

Los parámetros son identificadores que permiten **generar configuraciones únicas en los artículos**.

## ¿Qué son los parámetros?

Los parámetros se utilizan para:
- Generar códigos internos de artículos automáticamente
- Crear descripciones basadas en características
- Organizar artículos por familias

## Acceso en el Sistema

**Ruta:** Almacén → Parámetros

Los parámetros se establecen organizados por **familias**.

## Estructura de un Parámetro

### Cabecera (Configuración básica)

| Campo | Descripción |
|-------|-------------|
| **Código** | Codificación única del parámetro |
| **Acrónimo** | Abreviatura usada en descripciones |
| **Descripción** | Descripción completa del parámetro |
| **Unidades** | Unidad de medida asociada (opcional) |
| **Tipo** | Explícito o Implícito (ver sección Tipos) |

## Tipos de Parámetros

### Tipo Explícito
- El parámetro **no está formado por una lista predefinida**
- Los valores son **libres durante la creación del artículo**
- Solo pueden ser **valores numéricos**
- No se habilitan botones de inserción

### Tipo Implícito
- El parámetro **está formado por una lista de valores predefinidos**
- Al seleccionar tipo implícito, se habilitan **botones de inserción**
- Permite añadir valores del parámetro

## Valores de Parámetros (Tipo Implícito)

Los valores de parámetros tienen **tres columnas**:

| Campo | Descripción |
|-------|-------------|
| **Valor** | El valor del parámetro (aparecerá en el código del artículo) |
| **Descripción** | Descripción del valor (aparecerá en la descripción del artículo) |
| **Acrónimo** | Si existe, se usa en lugar de la descripción |

## Ejemplo Práctico

**Parámetro:** Color (Tipo Implícito)

Valores predefinidos:
- Valor: `R` → Descripción: `Rojo` → Acrónimo: `RJ`
- Valor: `A` → Descripción: `Azul` → Acrónimo: `AZ`
- Valor: `V` → Descripción: `Verde` → Acrónimo: `VD`

## Flujo de Trabajo

1. Crear parámetros base (Código, descripción, tipo)
2. Si es implícito, añadir valores permitidos
3. Asignar parámetros a familias de artículos
4. Usar en creación de artículos para generar códigos automáticos

## Tips y Consideraciones

⚠️ Los parámetros se organizan por familias  
⚠️ Una vez creados, algunos campos pueden no ser modificables  
⚠️ Los acrónimos aparecen en las descripciones de artículos  
"""
    
    parametros_path = almacen_dir / "01-parametros.md"
    with open(parametros_path, 'w', encoding='utf-8') as f:
        f.write(parametros_content)
    print(f"✓ Creado: 01-parametros.md")
    
    # 3. CREAR 02-MODELO-COSTES.MD
    costes_content = """# Modelo de Costes

La configuración de costes en Elastic permite definir cómo se calcula el precio de costo de cada artículo.

## Introducción

El coste de un artículo es fundamental para:
- Calcular márgenes de beneficio
- Conocer rentabilidad de operaciones
- Tomar decisiones de precios
- Valorar inventarios (contabilidad)

## Acceso en el Sistema

**Ruta:** Almacén → Modelo de Costes

## Tres Modelos Disponibles

### 1. Modelo Básico

El modelo más simple y directo.

**Características:**
- La empresa establece un **coste estándar para cada artículo**
- Apto para un **período de tiempo determinado**
- Responsabilidad del cliente **mantenerlo actualizado**

**Configuración:**
El coste estándar se calcula en base a:
- **Coste de materia prima**
- **Coste de mano de obra**
- **Coste de maquinaria**

Dependiendo del proceso productivo de la empresa.

**Actualización de Materia Prima:**
- Opción A: Coste concreto fijo
- Opción B: Media de las entradas históricas
- Opción C: Tarifa de un proveedor (se actualiza automáticamente)

### 2. Modelo con Sobrecostes

Para empresas con costes adicionales más allá de los básicos.

**Características:**
- Extiende el modelo básico con **sobrecostes configurables**
- Permite costes **partidas fijas o variables**
- Se aplican sobre **materia prima, mano de obra o maquinaria**

**Ejemplos de Sobrecostes:**
- Costes de transporte y logística
- Costes de almacenaje
- Costes administrativos asignados
- Gastos de calidad

### 3. Modelo Personalizado

Para empresas con requerimientos especiales.

Se puede contactar con Imatia para configurar modelos personalizados según necesidades específicas.

## Creación de un Modelo de Costes

**Paso 1: Acceder**
1. Ir a: Almacén → Modelo de Costes
2. Hacer clic en "Nuevo registro"

**Paso 2: Configurar cabecera**
En esta versión inicial, configura:
- Nombre del modelo
- Tipo (básico / con sobrecostes / personalizado)
- Parámetros generales

**Paso 3: Definir componentes**
- Coste de materia prima
- Coste de mano de obra
- Coste de maquinaria
- Sobrecostes (si aplica)

**Paso 4: Asignar a artículos**
Una vez creado, asigna el modelo a los artículos correspondientes.

## Impacto en el Sistema

El modelo de costes afecta a:
- **Albaranes de entrada** - Valoración automática
- **Informes financieros** - Activo/Pasivo circulante
- **Márgenes comerciales** - Análisis de rentabilidad
- **Precios de venta** - Cálculo automático de márgenes

## Tips Importantes

💡 Revisa periódicamente los modelos para mantenerlos actualizados  
💡 Valida los costes con Contabilidad  
💡 Usa el modelo básico si no tienes sobrecostes adicionales  
⚠️ Los cambios en modelos afectan a cálculos históricos  
"""
    
    costes_path = almacen_dir / "02-modelo-costes.md"
    with open(costes_path, 'w', encoding='utf-8') as f:
        f.write(costes_content)
    print(f"✓ Creado: 02-modelo-costes.md")
    
    # 4. CREAR 03-STOCK-SEGURIDAD.MD
    stock_content = """# Stock de Seguridad

El stock de seguridad es el **nivel mínimo de inventario** que debe mantenerse para evitar roturas de stock.

## ¿Qué es el Stock de Seguridad?

Es una **reserva de almacén** para proteger contra:
- Variaciones en la demanda
- Retrasos en entregas de proveedores
- Picos de ventas inesperados
- Incertidumbre en la cadena de suministro

## Acceso en el Sistema

**Ruta:** Almacén → Stock de Seguridad

## Configuración

Cada artículo puede tener asignado:
- **Nivel mínimo de stock** (unidades)
- **Período de revisión** (semanal, mensual, etc.)
- **Tipo de reabastecimiento**

## Impacto Operacional

### Alertas de Reabastecimiento

El sistema alerta cuando:
- Stock actual < Stock de seguridad
- Necesidad urgente de compra

### Cálculo de Necesidades

Se utiliza para:
- Planificar compras automáticas
- Determinar cantidad de pedidos mínimos
- Optimizar inversión en almacén

### Punto de Reorden (Reorder Point)

$$ \\text{Punto de Reorden} = \\text{Stock Seguridad} + \\text{Consumo Medio} \\times \\text{Plazo Entrega} $$

**Ejemplo:**
- Stock seguridad: 100 unidades
- Consumo medio: 50 unidades/día
- Plazo entrega proveedor: 10 días
- Punto de reorden: 100 + (50 × 10) = 600 unidades

## Mejores Prácticas

✓ Revisa stock de seguridad anualmente  
✓ Ajusta según variabilidad de demanda  
✓ Coordina con compras para una planeación óptima  
⚠️ Stock muy alto = mayor costo de almacenaje  
⚠️ Stock muy bajo = riesgo de ruptura  

## Relación con Otros Módulos

- **Compras:** Los niveles de seguridad determinan necesidad de compra
- **Producción:** Stock mínimo de materias primas para producción
- **Ventas:** Capacidad de respuesta a pedidos
- **Finanzas:** Inversión en capital circulante
"""
    
    stock_path = almacen_dir / "03-stock-seguridad.md"
    with open(stock_path, 'w', encoding='utf-8') as f:
        f.write(stock_content)
    print(f"✓ Creado: 03-stock-seguridad.md")
    
    # 5. CREAR _CATEGORY_.JSON
    category_json = """{
  "label": "Almacén",
  "position": 2,
  "link": {
    "type": "generated-index",
    "description": "Módulo de gestión de almacén con parámetros, costes y control de stock"
  }
}"""
    
    category_path = almacen_dir / "_category_.json"
    with open(category_path, 'w', encoding='utf-8') as f:
        f.write(category_json)
    print(f"✓ Creado: _category_.json")
    
    # Resumen
    print("\n" + "="*70)
    print("✅ ESTRUCTURA COMPLETADA PARA ALMACEN")
    print("="*70)
    print("""
Archivos creados:
  ✓ intro.md                  - Índice principal del módulo
  ✓ 01-parametros.md          - Guía completa de parámetros
  ✓ 02-modelo-costes.md       - Explicación de 3 modelos de costes
  ✓ 03-stock-seguridad.md     - Configuration de niveles mínimos
  ✓ _category_.json           - Config de navegación Docusaurus

Ubicación: docs/almacen/

Próximos pasos:
  1. Revisa los archivos generados
  2. Valida la información con los PDFs
  3. Agrega imágenes si existen (docs/assets/pdf-images/almacen/)
  4. Repite este proceso para otros módulos
  5. Ejecuta: npm run build
""")


if __name__ == "__main__":
    create_almacen_structure()

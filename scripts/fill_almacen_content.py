#!/usr/bin/env python3
"""
Script para completar los archivos markdown del almacén con contenido del PDF
"""

from pathlib import Path

def main():
    project_root = Path(__file__).parent.parent
    
    # Contenido para intro.md
    intro_content = """# Almacén

## Introducción

El **módulo de Almacén** de Elastic Business ERP proporciona una gestión integral del inventario y la valoración de stocks. Permite configurar los artículos mediante parámetros, establecer modelos de costes flexibles, definir niveles de seguridad automáticos y organizar los productos en familias.

## Estructura del módulo

El módulo de Almacén se organiza en cuatro áreas funcionales principales:

### 1. Parámetros
Configuración de identificadores que permiten generar códigos y descripciones únicos en los artículos según familias.

**Acceso:** Almacén >> Parámetros

[Ver documentación →](01-parametros.md)

### 2. Modelo de Costes
Definición de estrategias de valoración de inventarios con múltiples opciones de cálculo.

**Acceso:** Almacén >> Modelo de costes

[Ver documentación →](02-modelo-costes.md)

### 3. Stock de Seguridad
Establecimiento de niveles mínimos automáticos de inventario mediante cálculos inteligentes.

**Acceso:** Almacén >> Procesos >> Stock de seguridad

[Ver documentación →](03-stock-seguridad.md)

### 4. Familias de Artículos
Definición de categorías y grupos de productos con propiedades compartidas.

**Acceso:** Almacén >> Familia de artículos

[Ver documentación →](04-familias-articulos.md)

## Características principales

✓ **Gestión centralizada** - Control integral del inventario desde un único punto  
✓ **Configuración flexible** - Adaptable a diferentes estructuras de productos  
✓ **Automatización inteligente** - Reordenes y cálculos automáticos  
✓ **Trazabilidad completa** - Historiales de movimientos y cambios  
✓ **Múltiples modelos de costes** - Básico, con sobrecostes o personalizado  

## Integración con otros módulos

El módulo de Almacén se integra con:

- **Compras** - Recepción de mercancía y actualización de stocks
- **Ventas** - Disponibilidad de stock para pedidos y albaranes
- **Producción** - Consumo de materiales y control de lista de materiales (BOM)
- **Finanzas** - Valoración de inventarios para la contabilidad
"""

    # Contenido para 01-parametros.md
    parametros_content = """# Parámetros

## Descripción

Los parámetros se definen como identificadores que permiten generar configuraciones únicas en los artículos. La creación de artículos mediante parámetros sirve para generar automáticamente el código interno y descripción del artículo.

## Acceso

En Elastic Business se accede mediante la siguiente ruta:

**Almacén >> Parámetros**

Los parámetros se establecen por **FAMILIAS de artículos**.

## Configuración básica

Cada parámetro está formado por una serie de valores. Antes de añadir valores, primero hay que definir la configuración básica del parámetro.

En la cabecera del parámetro se muestran los siguientes campos:

### Campos principales

| Campo | Descripción |
|-------|-------------|
| **Código** | Codificación identificativa del parámetro |
| **Acrónimo** | Se utiliza como abreviatura de la descripción |
| **Descripción** | Descripción completa del parámetro |
| **Unidades** | Permite asociar una unidad de medida al parámetro |
| **Tipo** | Define cómo se comporta el parámetro |

## Tipos de parámetros

### Tipo Explícito
- El parámetro no está formado por una lista predefinida de valores
- Los valores son libres durante la creación del artículo
- Los valores solo pueden ser numéricos
- Útil para especificaciones variables (dimensiones, pesos, etc.)

### Tipo Implícito
- Uno de los valores del parámetro forma parte de la configuración del artículo
- Se habilitan los botones de inserción para añadir valores predefinidos
- Útil para características fijas de la familia (colores, materiales, etc.)

## Tabla de valores de parámetros

Cuando el parámetro es de tipo implícito, se pueden definir los valores posibles. Cada valor tiene tres columnas:

| Columna | Descripción |
|---------|-------------|
| **Valor** | Indica el valor del parámetro; este aparecerá en el código del artículo si así se configura |
| **Descripción** | Descripción del valor; aparecerá en la descripción del artículo |
| **Acrónimo** | Si el valor tiene acrónimo, este se usará en lugar de la descripción en el código |

## Grupos de parámetros

Se permite configurar **grupos de parámetros**, que es útil cuando existe un uso compartido de valores. Esto agiliza la creación de parámetros nuevos reutilizando configuraciones anteriores.

## Proceso de trabajo

1. Acceder a Almacén >> Parámetros
2. Seleccionar la familia donde se crearán los parámetros
3. Crear nuevo parámetro con código, acrónimo y descripción
4. Definir el tipo (Explícito o Implícito)
5. Si es implícito, añadir los valores posibles
6. Guardar la configuración

## Relación con familias de artículos

Los parámetros configurados se utilizan posteriormente en la definición de **Familias de artículos** para determinar cómo se generarán automáticamente los códigos de los artículos que pertenezcan a esa familia.
"""

    # Contenido para 02-modelo-costes.md
    costes_content = """# Modelo de Costes

## Descripción

El módulo de Modelo de Costes permite definir estrategias flexibles de valoración de inventarios. Elastic Business soporta tres tipos de modelos adaptados a diferentes necesidades empresariales.

## Acceso

En Elastic Business se accede mediante:

**Almacén >> Modelo de costes**

## Tipos de modelos de costes

### 1. Modelo Básico

El modelo básico establece un coste estándar para cada uno de los artículos durante un periodo de tiempo determinado.

**Características:**
- Responsabilidad del cliente mantenerlo y actualizarlo
- El coste estándar se calcula basándose en:
  - Coste de materia prima
  - Coste de mano de obra
  - Coste de maquinaria
- El coste de materia prima puede configurarse como:
  - Coste concreto fijo
  - Media de las entradas recibidas
  - Tarifa de un proveedor específico (actualizable automáticamente)

**Ideal para:** Empresas con estructura de costes simple y relativamente estable.

### 2. Modelo con Sobrecostes

Para empresas que necesitan un modelo más completo que contemple costes más allá de los básicos, el sistema permite configurar un modelo de costes con la posibilidad de añadir **sobrecostes configurables**.

**Características:**
- Incluye los tres costes básicos (materia prima, mano de obra, maquinaria)
- Permite añadir partidas de costes adicionales
- Los sobrecostes pueden ser:
  - **Partidas fijas:** coste constante por unidad
  - **Partidas variables:** porcentaje sobre materia prima, mano de obra o maquinaria
- Flexible y adaptable a diferentes estructuras de costes

**Ideal para:** Empresas con costes indirectos o gastos de transformación adicionales.

### 3. Modelo Personalizado

Adaptación completa del sistema de costes según necesidades específicas de la empresa.

## Configuración del modelo de costes

### Creación de un nuevo modelo

1. Ir a **Almacén >> Modelo de costes**
2. Añadir un nuevo registro
3. Cubrir los campos de la cabecera

### Campos de la cabecera

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Nombre identificativo del modelo |
| **Fecha inicio** | Fecha de inicio de vigencia del modelo |
| **Fecha fin** | Fecha hasta la que tendrá validez el modelo |

### Pestañas del modelo

**Partidas:** Aquí se añaden los costes que necesitemos para el modelo con sobrecostes
- Definición de cada partida de coste
- Configuración como fija o variable
- Base de cálculo (si es variable)

**Familias:** Se muestran todas las familias que usan este modelo de costes
- Permite activar el modelo como predeterminado

**Artículos:** Se muestran todos los artículos que usan este modelo de costes

## Aplicación del modelo

### A nivel de familia

Los modelos de costes se pueden asignar a nivel de **Familia de artículos**:

1. Ir a **Almacén >> Familia de artículos >> Activas**
2. Entrar en los detalles de la familia
3. Asignar el modelo de costes
4. Marcar como "Activo" para usar por defecto

### A nivel de artículo

También se puede aplicar directamente a artículos individuales dentro de una familia.

## Consideraciones

- Se pueden añadir múltiples modelos de costes a una misma familia
- Un artículo puede tener asignado un modelo específico diferentes al de su familia
- Es responsabilidad de la empresa mantener actualizado el modelo de costes básico
"""

    # Contenido para 03-stock-seguridad.md
    stock_content = """# Stock de Seguridad

## Descripción

El cálculo de stock de seguridad permite que Elastic Business calcule automáticamente los stocks mínimos óptimos del almacén basándose en datos históricos de ventas/consumos y parámetros configurables.

## Acceso

En Elastic Business se accede mediante:

**Almacén >> Procesos >> Stock de seguridad**

## Fórmula de cálculo

El stock mínimo se calcula en base a:

1. **Ventas/Consumos diarios** del período que el usuario decida (trimestral, anual, etc.)
2. **Plazo de entrega del proveedor** (expresado en días)
3. **Coeficiente de tasa de servicio** del artículo (factor de seguridad)

### Parámetros del cálculo

| Parámetro | Descripción |
|-----------|-------------|
| **Período de análisis** | Intervalo de tiempo histórico a considerar (ej: año 2024) |
| **Plazo de entrega** | Días que tarda el proveedor en entregar después de realizar el pedido |
| **Coeficiente de servicio** | Factor de seguridad (opcional); si no se especifica se usa 1 |

**Nota:** El coeficiente de tasa de servicio es opcional. Si no se proporciona, el sistema utiliza automáticamente el valor 1.

## Proceso de cálculo

### Paso 1: Seleccionar el artículo

Selecciona sobre qué artículo deseas realizar el cálculo de stock de seguridad.

### Paso 2: Elegir el período

Define el período histórico que deseas utilizar para el cálculo:
- Tienes la opción de descartar ciertos meses para que no los tenga en cuenta
- Esto es útil para excluir períodos anómalos o estacionales

### Paso 3: Ejecutar el cálculo

Pulsa el botón calcular y el sistema procesará los datos.

### Paso 4: Revisar y aplicar

El sistema proporciona un valor de stock de seguridad calculado. En este momento puedes:
- **Aceptar el valor propuesto** y volcarlo sobre la configuración del artículo
- **Editar el resultado** manualmente si lo consideras necesario
- **Rechazarlo** si no se ajusta a tu política de stock

## Ejemplo práctico

**Artículo:** 60108001 EFILUX 360 FT

**Datos:**
- Período de análisis: Año 2024 (consumo total: 7,647 unidades)
- Plazo de entrega del proveedor: 30 días
- Tasa de servicio: 1 (por defecto)

**Resultado:** Stock de seguridad calculado = 629 unidades

## Ventajas del cálculo automático

✓ **Basado en datos reales:** Usa históricos reales de consumo  
✓ **Flexible:** Permite excluir períodos atípicos del análisis  
✓ **Adaptativo:** Se recalcula fácilmente según cambios en el mercado  
✓ **Optimizado:** Reduce el riesgo de rupturas de stock  
✓ **Eficiente:** Minimiza stocks innecesarios  

## Recomendaciones

1. Revisar periódicamente los stocks de seguridad (mensualmente o trimestralmente)
2. Ajustar los parámetros con cambios significativos en la demanda
3. Considerar factores externos (estacionalidad, promociones, etc.)
4. Validar que el coeficiente de servicio refleja tu política de disponibilidad
"""

    # Contenido para 04-familias-articulos.md
    familias_content = """# Familias de Artículos

## Descripción

Las Familias de Artículos son conjuntos de productos que comparten características comunes. Permiten aplicar configuraciones de manera masiva a todos los artículos de una familia, facilitando la gestión centralizada de grupos de productos.

## Acceso

En Elastic Business se accede mediante:

**Almacén >> Familia de artículos**

## Concepto de familia

Una familia es una agrupación lógica de artículos que comparten:
- **Características técnicas similares**
- **Procesos de fabricación comunes**
- **Modelos de costes aplicables**
- **Parámetros de configuración**
- **Políticas de valoración**

## Configuración de familias

### Información básica de la familia

- **Código:** Identificador único de la familia
- **Descripción:** Nombre descriptivo de la familia
- **Tipo de familia:** Categoría o clasificación
- **Estado:** Activa/Inactiva

### Asociación de parámetros

Cada familia puede tener asociados parámetros que determinan:
- Cómo se generan automáticamente los códigos de los artículos
- Qué características variables pueden tener los productos

**Ejemplo:** Una familia "Tuberías de PVC" podría tener parámetros para:
- Diámetro (20mm, 25mm, 32mm, etc.)
- Presión (PN10, PN16, PN25)

### Asignación de modelo de costes

Cada familia debe tener asignado un modelo de costes que define:
- Cómo se valoran los artículos en inventario
- Qué estructura de costes se utiliza

Los artículos individuales pueden sobrescribir el modelo de la familia si lo requieren.

## Uso de familias

### Creación de artículos

Cuando creas un artículo:
1. Seleccionas la familia a la que pertenece
2. El sistema aplica automáticamente la configuración de esa familia
3. Los parámetros de la familia se usan para generar el código

### Gestión masiva

Las familias permiten:
- Cambiar la configuración común a múltiples artículos
- Aplicar nuevos parámetros a todos los artículos de una familia
- Modificar el modelo de costes para toda una familia

### Organización

Las familias facilitan:
- La búsqueda y clasificación de artículos
- La generación de reportes por categoría de producto
- La organización de procesos de fabricación
- La aplicación de políticas comunes

## Relación con otros elementos

```
Familia de Artículos
    ↓
    ├─→ Parámetros (generación de códigos)
    ├─→ Modelo de Costes (valoración)
    ├─→ Artículos (múltiples)
    └─→ Configuración compartida
```

## Beneficios de usar familias

✓ **Eficiencia:** Configuración masiva de múltiples artículos  
✓ **Coherencia:** Asegura que artículos similares se traten de igual forma  
✓ **Mantenibilidad:** Cambios en la familia se propagan a sus artículos  
✓ **Escalabilidad:** Facilita el crecimiento del catálogo de productos  
✓ **Organización:** Estructura clara del inventario  
"""

    # Guardar archivos
    files = {
        "docs/almacen/intro.md": intro_content,
        "docs/almacen/01-parametros.md": parametros_content,
        "docs/almacen/02-modelo-costes.md": costes_content,
        "docs/almacen/03-stock-seguridad.md": stock_content,
        "docs/almacen/04-familias-articulos.md": familias_content,
    }
    
    print("=" * 70)
    print("LLENADOR DE CONTENIDO - MÓDULO ALMACÉN")
    print("=" * 70)
    
    for file_path, content in files.items():
        full_path = project_root / file_path
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Actualizado: {file_path}")
    
    print("\n" + "=" * 70)
    print("✅ MÓDULO ALMACÉN COMPLETADO")
    print("=" * 70)

if __name__ == "__main__":
    main()

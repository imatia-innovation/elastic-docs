# Stock de Seguridad

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

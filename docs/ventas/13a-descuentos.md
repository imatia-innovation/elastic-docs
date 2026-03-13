# Descuentos

Los descuentos son reducciones de precio aplicadas a documentos o líneas de venta en función de condiciones definidas.

**Ruta de acceso:** `Ventas >> Configuración >> Descuentos`

## Tipos de descuentos

Existen **dos tipos** de descuentos en la aplicación:

### Descuentos por línea

- Se aplican sobre las líneas de pedido cuando se cumplen unas condiciones definidas
- El importe bruto de la línea debe encontrarse entre los límites marcados (nivel inferior y nivel superior)
- Es posible indicar un período de vigencia mediante los campos "Desde" y "Hasta"
- Se aplican a artículos específicos en líneas concretas

### Descuentos generales

- Se pueden configurar con un valor fijo o uno variable
- No influyen las fechas de validez (aunque pueden tenerlas)
- Se aplican a todo el documento globalmente

## Estados de descuentos

Los descuentos se encuentran agrupados por estados:

- **Activos:** Descuentos que están en vigor. Permite configurar únicamente descuento general o por línea
- **Grupos activos:** Descuentos en vigor que se encuentran agrupados. Permite realizar una combinación entre descuentos generales o por línea
- **De baja:** Descuentos que han dejado de estar vigentes
- **Grupos de baja:** Grupos activos que se han dado de baja

## Acceso y estructura del formulario

Desde el formulario de búsqueda, una vez localizado el descuento, se accede a él mediante **doble clic** sobre el detalle. El formulario posee dos secciones perfectamente diferenciadas:

- **Parte superior:** Cabecera del descuento
- **Parte inferior:** Pestañas de configuración

## Cabecera del descuento

En la cabecera se encuentran los datos principales de los descuentos.

| Campo | Descripción |
|-------|------------|
| **Acrónimo** | Acrónimo identificativo del descuento |
| **Descripción** | Descripción del descuento |
| **Tipo** | Permite definir si es general (aplica al documento) o por artículo (aplica a las líneas) |
| **Dto. fijo** | Valor numérico fijo del descuento |
| **Dto. variable** | Valor en porcentaje que se aplica sobre base imponible |
| **Dto. variable línea** | Valor en porcentaje que se aplica sobre base imponible de la línea |
| **Dto. cascada variable** | Valor en porcentaje de descuento en cascada |
| **Recargo** | Check que indica el importe del descuento en la columna Recargo |
| **Desde** | Fecha desde aplicación del descuento |
| **Hasta** | Fecha hasta aplicación del descuento |
| **Nivel inferior** | Límite inferior de importe en el que se aplica el descuento |
| **Nivel superior** | Límite superior de importe en el que se aplica el descuento |
| **Fecha baja** | Fecha de baja del descuento |

### Consideraciones importantes

> **Nota:** Se pueden establecer condiciones para que el descuento se aplique automáticamente o no en función de los parámetros de los artículos.

> **Tipo de descuento:** El tipo seleccionado determina cómo se aplicará:
> - **General:** Se aplica al total del documento
> - **Por artículo/línea:** Se aplica a líneas específicas

## Pestañas de configuración

### Clientes

Se muestran los clientes asociados a un descuento determinado. Los descuentos pueden:
- Aplicarse a clientes específicos
- Restringirse a un grupo de clientes
- Utilizarse de forma general si no se asignan clientes

### Comerciales

Se muestran los comerciales asociados al descuento determinado. Permite:
- Asignar descuentos a comerciales específicos
- Vincular descuentos con políticas comerciales
- Controlar descuentos por representante

### Artículos

Se muestran los artículos a los que se les aplica el grupo activo. Permite:
- Definir qué artículos están sujetos a descuentos
- Crear políticas de descuento por producto
- Configurar descuentos por familia de productos

### Familias

Se muestran las familias a las que se agrupa el grupo activo. Permite:
- Aplicar descuentos a todas las familias de forma conjunta
- Gestionar descuentos a nivel de categoría
- Simplificar la configuración de múltiples productos

## Grupos de descuentos

Un **grupo de descuento** es una agrupación de descuentos que permite:
- Aplicar combinaciones entre descuentos generales y por línea
- Gestionar múltiples descuentos de forma coordinada
- Asociar grupos completos a clientes o comerciales específicos

### Estados de grupos

- **Grupos activos:** Grupos de descuentos en vigor que permiten realizar combinaciones entre descuentos generales o por línea
- **Grupos de baja:** Grupos activos que se han dado de baja

### Ventajas de usar grupos

- **Flexibilidad:** Combinación de múltiples descuentos
- **Eficiencia:** Gestión centralizada de políticas de descuento
- **Control:** Aplicación coordinada de descuentos relacionados
- **Escalabilidad:** Facilita la creación de políticas complejas

## Aplicacion de descuentos en documentos

Los descuentos configurados se aplican automáticamente o manualmente según su configuración:

### Aplicación automática

Cuando los descuentos cumplen las condiciones establecidas, se aplican automáticamente en:
- Presupuestos
- Pedidos
- Albaranes
- Facturas

### Descuentos por volumen

Los descuentos pueden estar basados en:
- Importe total de la compra
- Cantidad de unidades
- Período de tiempo (fecha desde-hasta)
- Combinación de factores

### Prioridad de descuentos

Cuando un cliente puede tener múltiples descuentos aplicables:
1. El sistema evalúa todas las condiciones
2. Aplica el descuento que resulte más favorable
3. Permite combinación de descuentos si está configurada

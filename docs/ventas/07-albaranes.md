# Albaranes

En el flujo de ventas, una vez generado el pedido, el siguiente paso es crear el albarán de ventas. **Es desde el albarán donde se da la mercancía de baja en el almacén.**

**Ruta de acceso:** `Ventas >> Albaranes`

## Pantalla principal

Los albaranes se muestran agrupados por estados, donde aquellos que hacen referencia a la recepción del pedido muestran el estado desde el punto de vista del almacén, y los que hacen referencia a la facturación desde el punto de vista de la facturación del pedido.

En la zona central tenemos **8 pestañas** donde se recogen los albaranes por estado:

- **No expedidos:** Pestaña donde se pueden crear albaranes
- **Expedidos:** Albaranes ya despachados
- **No expedibles:** Pestaña donde se pueden crear albaranes
- **No facturados:** Pestaña donde se pueden crear albaranes
- **Facturados:** Albaranes facturados
- **No facturables:** No se pueden facturar
- **Anulados:** Albaranes cancelados
- **Todos:** Todos los albaranes

## Estructura del formulario del albarán

El formulario destaca dos partes: la **cabecera**, en la parte superior, y **cuatro pestañas** con toda la información y funcionalidad necesarias.

## Cabecera del albarán

En la cabecera se encuentran los datos principales del albarán. Una vez seleccionado el albarán de ventas, según la configuración existente, se precargan los datos (cliente, fecha del documento, moneda, etc.).

### Checks especiales

- **Expedido:** Indica que el material ya ha sido dado de baja del sistema
- **De abono:** Indica que es un albarán de abono, que implica devolución de material por parte del cliente

## Pestaña Básico

Similar a Presupuestos, contiene datos de dirección fiscal, cliente y observaciones.

## Pestaña Gestión

Se visualizan los datos de pago y un resumen económico del albarán, incluyendo impuestos. Se divide en 4 bloques:

- Datos de cobro
- Comisiones
- Importes detalles
- Importes transporte
- Importes totales

## Pestaña Líneas

Es donde se define las características del albarán. Se divide en **4 subpestañas**:

### Líneas

Se pueden añadir nuevos artículos al albarán. Se divide en:

**Parte superior:**
- Selección de posibles descuentos
- Almacén donde se dará de alta la mercancía

**Tabla inferior:**
- Detalles de las líneas del albarán

> **Nota:** En las líneas de albaranes se tienen dos botones de acción: uno para añadir pedidos y otro para añadir detalles de pedidos.

### Previa expediciones

Muestra información relativa a la previa expedición del material:
- De qué ubicación se va a retirar
- Información relativa al stock
- Configuración del artículo para las expediciones

### Resumen

Se permite personalizar los conceptos que saldrán en la impresión, manteniendo los datos económicos del documento.

### Albaranes de abono

Se muestran todos los albaranes de abono asociados al albarán de ventas.

## Pestaña Documentos asociados

Se mostrarán los documentos relacionados con el albarán:

- Presupuestos
- Pedidos
- Órdenes de preparación/carga
- Facturas
- Incidencias / RMA

Cada pestaña muestra información básica del correspondiente documento.

## Pestaña Comerciales adicionales

Se permiten asociar comerciales adicionales con su comisión correspondiente.

## Pestaña Adicional

Se muestran todos los datos referentes a fechas de envío, aceptación, etc.

### Datos de registro

| Campo | Descripción |
|-------|------------|
| **F. creación** | Fecha de creación del registro |
| **Creador** | Usuario que creó el registro |
| **Ejercicio fiscal** | Periodo contable o fiscal |
| **F. últ. modificación** | Fecha de última modificación |
| **Usuario últ. mod.** | Usuario que realizó la última modificación |

### Información de fechas

| Campo | Descripción |
|-------|------------|
| **F. de entrega** | Fecha prevista o real de entrega |
| **F. expedido** | Fecha de expedición del albarán |
| **F. anulado** | Fecha de anulación si aplica |
| **F. movimiento** | Fecha del movimiento de mercancía en almacén |
| **Fecha de impresión** | Fecha de impresión del albarán |
| **Motivo anulación** | Razón de anulación |

### Otros datos

| Campo | Descripción |
|-------|------------|
| **Envío** | Relación con el envío |
| **Fecha de envío** | Fecha del envío |
| **Mantenimiento** | Relación con el mantenimiento |

### Información de facturación

| Campo | Descripción |
|-------|------------|
| **Pendiente factura** | Indica si aún no ha sido facturado |
| **Factura** | Número o referencia de la factura asociada |
| **Notas factura** | Observaciones relacionadas con la factura |
| **No facturable** | Check para indicar que no puede ser facturado |
| **Concepto** | Descripción general del albarán |

### Otros datos (checks)

| Campo | Descripción |
|-------|------------|
| **Duplicado** | Indica si ya se imprimió el albarán 2 veces |
| **Consigna de cobro** | Se trata de una consignación para posterior cobro |
| **No expedible** | No es expedible |
| **No imprimir albarán** | No se debe imprimir |

## Pestaña Ficheros

Se asocian documentos digitalizados:
- Se pueden capturar directamente desde un origen
- Arrastrar a la pestaña para adjuntar directamente
- Escanear directamente un documento

Para adjuntar un fichero pulsar el icono del clip azul y seleccionar el fichero del ordenador.

## Pestaña Calidad

| Campo | Descripción |
|-------|------------|
| **Código** | Identificador único del registro de calidad |
| **Fecha apertura** | Fecha de apertura del incidente |
| **Creador** | Usuario que registró |
| **Descripción no conformidad** | Detalle del defecto detectado |
| **Cod. artículo** | Código del artículo afectado |
| **Desc. artículo** | Descripción del artículo |
| **Nº lote** | Número de lote con incidencia |

## Botones de Acción

### Generar factura (F2)
Se generará automáticamente la factura del albarán de ventas. Se solicitará la Fecha de emisión.

### Autoselección de lotes/nº de serie
Si el albarán no procede de una orden de preparación, con esta funcionalidad se asignarán automáticamente los lotes.

### Expedir
Con esta acción se realiza la baja del material del almacén.

### Generar albarán de abono
Esta acción aparece deshabilitada si el albarán no está expedido. Una vez expedido, se puede generar. Realiza movimientos de alta en el almacén según la cantidad especificada.

### Clonar Albarán
Realiza una copia del albarán habilitando diferentes opciones de copia de datos.

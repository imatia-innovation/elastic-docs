# Pedidos

El pedido es el documento de confirmación de la venta.

**Ruta de acceso:** `Ventas >> Pedidos`

## Cómo crear un pedido

Una vez que se han dado de alta clientes y se les ha asignado artículos y tarifas, ya puedes realizar directamente el pedido. También es posible crear pedidos directamente desde los presupuestos.

> **Nota:** En el presupuesto viene dado cubierto por defecto ciertos datos básicos.

Para generar un nuevo pedido se tiene que pulsar el icono **"Añadir registro"** (cruz verde). Se desplegará una ventana dividida en **9 pestañas**.

## Pantalla principal

En la pestaña principal se puede ver a la izquierda un desplegable con todos los presupuestos, dividido en Años, Estado y Empresa.

En la zona central tenemos **5 pestañas** donde se recogen los presupuestos por estado:

- **No expedidos:** Única pestaña donde se pueden crear pedidos
- **Expedidos:** Pedidos ya despachados
- **Anulados:** Pedidos cancelados
- **Bloqueados:** Pedidos bloqueados
- **Todos:** Todos los pedidos

> **Nota:** Dentro de la pestaña "No expedidos" se da la posibilidad de realizar las siguientes acciones:
> - Generar albarán
> - Generar órdenes de preparación/carga

## Estructura del formulario del pedido

La ventana del pedido de ventas se divide en dos secciones, en la parte superior, la **cabecera** y en la parte inferior, un conjunto de **9 pestañas**.

## Cabecera del pedido

Se pueden ver los datos básicos del pedido, los cuales pasarán a ser fijos una vez se pase a albarán.

| Campo | Descripción |
|-------|------------|
| **Empresa** | Nombre de la empresa contra la que se crea el pedido. Si multiempresa, aparecerá la definida por defecto |
| **División** | División específica de la empresa |
| **Departamento** | Departamento dentro de la división que solicita el pedido |
| **Pedido** | Código de identificación del documento. Autonumérico secuencial o configurado |
| **Tipo** | Tipo de documento de venta |
| **Cliente** | Campo obligatorio. Viene cubierto si se genera desde un presupuesto |
| **Grupos de empresas** | Indica si el cliente pertenece a grupos configurados |
| **Condiciones del solicitante** | Las condiciones de cobro son del cliente solicitante |
| **Cliente facturación** | Cliente al que se emitirá la factura |
| **Comercial** | Comercial asociado al documento |
| **Comisión** | Comisión del comercial |
| **F. documento** | Campo obligatorio. Fecha del documento |
| **En programación** | Check que indica si el pedido está en una programación |
| **Base total** | Suma total de importes base sin impuestos |
| **Importe total** | Suma total con impuestos |
| **Importe mínimo venta** | Configurado en la ficha de cliente |
| **Saldo** | Saldo disponible para el cliente |
| **Moneda** | Tipo de moneda del pedido |
| **Conversión** | Tipo de cambio si es moneda diferente |
| **Prioritario** | Check que identifica el pedido como prioritario |

## Pestaña Básico

Se distribuye en bloques iniciales: Dirección fiscal, Datos cliente y Observaciones. Los datos se cubren automáticamente al seleccionar un cliente.

> **Nota:** Los datos vendrán cubiertos si vienen de presupuesto o se cubrirán al seleccionar el cliente.

## Pestaña Gestión

Se visualizan los datos de pago y un resumen económico del pedido, incluyendo impuestos. Se divide en 5 bloques:

- Datos de cobro
- Comisiones
- Importes detalles
- Importes transporte
- Importes totales

> **Nota:** Los datos vendrán cubiertos si vienen de presupuesto. Se pueden hacer cambios si se modifican las líneas.

## Pestaña Líneas

Se visualiza una relación detallada de la última versión creada, línea a línea.

### Campos principales

| Campo | Descripción |
|-------|------------|
| **Descuentos** | Dto. General y Dto. Pronto pago |
| **Márgenes** | Margen sobre ventas y Margen sobre costes |
| **Descuento** | Permite aplicar o modificar el descuento sobre la línea |
| **IVA** | Permite aplicar o modificar el IVA de la línea |
| **Almacén** | Almacén principal de donde se consume el producto |
| **Subalmacén** | Subalmacén específico dentro del almacén principal |

## Botones de acción

### Artículos
Permite seleccionar artículos dados de alta en el sistema. Se permite añadir artículos a la **Cesta de artículos**.

### Configurador
Permite la creación o selección de artículos paramétricos. Si el artículo está creado, el sistema lo añade automáticamente.

### Agrupaciones
Artículos físicos existentes agrupados en un artículo ficticio (Kits).

### Histórico de precios
Permite consultar el histórico de precios.

### Actualizar costes
Permite actualizar los costes de los artículos según configuración.

## Detalle ampliado

Al hacer doble click en una línea del pedido, se abre una ventana con información del artículo.

### Subpestaña de Observaciones
- **Observaciones:** Observaciones del detalle
- **Observaciones internas:** Para uso interno

### Subpestaña de Comerciales/Agentes adicionales
Se permite añadir comerciales adicionales y su comisión (manual o automática).

### Subpestaña Despiece manual
Se permite editar el despiece de un artículo:
1. Activar el check **"Despiece variable"**
2. Marcar **"Insertar detalles"** para mostrarlos como nuevos artículos dependientes

## Pestaña Documentos asociados

Se mostrarán los documentos relacionados con el pedido:
- Presupuestos
- Órdenes de preparación/carga
- Pedido de compras
- Albaranes
- Facturas
- Incidencias/RMA

## Pestaña Adicional

Se muestran todos los datos referentes a fechas de envío, aceptación, etc.

### Datos de registro

| Campo | Descripción |
|-------|------------|
| **F. creación** | Fecha en la que se creó el registro |
| **Creador** | Usuario que creó el registro |
| **Ejercicio fiscal** | Periodo contable o fiscal |
| **F. últ. modificación** | Fecha de última modificación |
| **Usuario últ. mod.** | Usuario que realizó la última modificación |

### Información de fechas

| Campo | Descripción |
|-------|------------|
| **F. recepción pedido** | Fecha de recepción en el sistema |
| **F. confirmación** | Fecha y hora de confirmación |
| **F. entrega real** | Fecha de entrega real |
| **F. bloqueado** | Fecha de bloqueo si aplica |
| **F. anulado** | Fecha de anulación si aplica |
| **Fecha de impresión** | Fecha de impresión |
| **Condiciones de entrega** | Condiciones específicas de entrega |
| **Fecha prevista de entrega** | Fecha estimada |
| **F. expedido** | Fecha de envío a albarán |
| **No bloquear** | No bloquear bajo ciertas circunstancias |
| **Motivo anulación** | Razón de anulación |

### Validación

| Campo | Descripción |
|-------|------------|
| **Pendiente validación** | Indicador de validación pendiente |
| **Fecha validación** | Fecha de validación |
| **Usuario validación** | Usuario que validó |

### Otros datos

| Campo | Descripción |
|-------|------------|
| **Presupuesto** | Presupuesto del cual se generó |
| **Pedido origen** | Pedido original del cual se duplicó |
| **Prioridad** | Asignar prioridad |
| **Oportunidad** | Asociar a oportunidad (Módulo CRM) |
| **Consigna de cobro** | Pertenece a consigna de cobro |
| **No imprimir albarán** | Se arrastra al albarán |
| **Concepto** | Campo de texto libre para anotaciones |

## Pestaña Producción

### Configuración

- **Check excluir de programación automática:** Excluye si hay programación automática
- **Observaciones OP:** Observaciones para arrastrar a las órdenes

### Subpestaña Órdenes
Muestra las órdenes generadas a raíz de los detalles si fueron enviadas a producción.

### Subpestaña Programaciones
Muestra la programación en la cual está el pedido.

### Subpestaña Puntos de control
Muestra los puntos de control en la programación.

## Pestaña Comerciales Adicionales

Se permite relacionar más de un comercial. El principal aparece en la cabecera y los auxiliares con su modelo de comisión e importe aparecen en esta pestaña.

## Pestaña Subcontratación

Indica si el pedido pertenece a un proceso de subcontratación de material.

En la parte inferior se indica cuál es el pedido de consigna de compras (pedido del proveedor para el servicio de subcontratación).

En el apartado Material recibido se visualizan los materiales que se recibirán tras la subcontratación.

## Pestaña Ficheros

Se permite adjuntar archivos en diversos formatos.

| Campo | Descripción |
|-------|------------|
| **Nombre** | Nombre del fichero |
| **Descripción** | Breve descripción |
| **Fecha** | Fecha de adjunción |
| **Usuario** | Usuario que adjunta |

## Botones de acción (icono engranaje)

### Generar factura (F2)
Se generará automáticamente la factura del albarán de ventas. Se solicitará la Fecha de emisión.

### Autoselección de lotes/nº de serie
Si el albarán no procede de una orden de preparación, con esta funcionalidad se asignarán automáticamente los lotes.

### Expedir
Con esta acción se realiza la baja del material del almacén.

### Generar albarán de abono
Esta acción aparece deshabilitada si el albarán no está expedido. Una vez expedido, se puede generar. En función de la cantidad especificada, se realizarán movimientos de alta en el almacén.

### Clonar Albarán
Realiza una copia del albarán habilitando opciones de copia de datos.

# Gestión de Cobros

En este apartado vemos cómo gestiona Elastic los cobros a sus clientes. Engloba los trámites administrativos y financieros necesarios hasta que se cobre su importe.

**Ruta de acceso:** `Ventas >> Gestión de cobros`

Se divide en **cinco submenús**:
- Recibos
- Anticipos
- Remesa de cobro
- Contabilización de pagos/cobros, pagarés
- Gestión de apuntes

---

## Recibos

El recibo es el documento que crea una obligación de pagar por parte del cliente una vez que se ha emitido la factura.

**Ruta específica:** `Ventas >> Gestión de cobros >> Recibos`

### Pantalla de recibos

El formulario de recibos consta de varias **pestañas** que permiten clasificar los recibos en función de su estado:

- **Pendientes:** Recibos pendientes de pago
- **Cobrados:** Recibos totalmente pagados
- **Devueltos:** Recibos devueltos por la entidad bancaria. Se crea un duplicado
- **Impagados:** Recibos sin cobrar con fecha de vencimiento vencida
- **Todos:** Todos los recibos creados independientemente del estado

> **Nota:** Como se explicó en el apartado Facturas, desde ese mismo apartado se generan los recibos y se les pone el estado correspondiente.

### Estructura del formulario del recibo

El formulario posee dos secciones perfectamente diferenciadas:
- **Parte superior:** Cabecera del recibo
- **Parte inferior:** Conjunto de pestañas con datos e información

### Cabecera del recibo

En la cabecera se encuentran los datos principales del recibo. Los únicos datos obligatorios son:
- **Cliente**
- **Fecha de emisión**
- **Fecha de vencimiento**

### Pestañas del recibo

#### Básico
Hace referencia a los datos económicos para el cobro:
- Datos bancarios de la empresa
- Datos de importes (moneda, gastos, comisión, etc.)
- Datos relacionados con el estado del recibo

#### Recibos agrupados
Se utiliza en las agrupaciones de recibos para mostrar los recibos que componen una agrupación.

#### Histórico
Se muestran los recibos relacionados entre sí.

#### Apuntes
Se generan según la configuración. Según se van poniendo como pagados o no pagados, se van generando apuntes.

#### Ficheros
Se asocian documentos digitalizados, capturados o arrastrados. Se puede escanear directamente un documento.

#### SII
Aparecen los datos de envío del cliente.

### Generar recibos

Hay **dos formas** de crear recibos:

1. **Desde las facturas de forma manual:**
   - `Ventas >> Facturas >> Pestaña Recibos >> Generar recibo`

2. **Automáticamente cuando se generan apuntes:**
   - `Ventas >> Gestión de cobros >> Recibos >> Pestaña Apuntes`

---

## Anticipos

Los anticipos se usan para gestionar aportaciones monetarias para un proveedor antes de haber hecho una compra o adelantar una transferencia bancaria sin que se haya emitido una factura.

### Estados de anticipos

Los anticipos se muestran agrupados por estados:

- **Pendientes:** Anticipos pendientes de ejecutarse para un proveedor
- **Validados:** Anticipos ya aplicados a un proveedor
- **Eliminados:** Anticipos eliminados

### Estructura del formulario de anticipo

El formulario posee dos secciones diferenciadas:
- **Parte superior:** Cabecera del anticipo
- **Parte inferior:** Conjunto de dos pestañas

### Cabecera del anticipo

En la cabecera se encuentran los datos principales. Los datos obligatorios son:
- **Nombre del proveedor**
- **Importe**
- **Moneda**
- **Conversión**
- **Fecha de creación**

### Pestañas del anticipo

#### Recibos
Aquí se muestran los recibos generados de un anticipo.

#### Ficheros
Se pueden asociar documentos digitalizados, capturados o arrastrados. Se puede escanear directamente un documento.

### Crear un anticipo

Para crear un anticipo:
1. **Insertar todos los datos obligatorios:**
   - Proveedor
   - Moneda
   - Importe
   - Conversión

---

## Remesas de Cobro

Esta funcionalidad permite llevar a cabo los cobros de recibos de manera masiva. Permite a su vez la gestión bancaria y la emisión de los cuadernos correspondientes para su cobro por gestión telemática.

> **Nota:** Puede ser utilizado como comodín para gestionar remesas temporales que no tienen por qué enviarse a gestión de cobro mediante cuaderno bancario (ej: generar una remesa de recibos de contado para un representante comercial).

### Estados de remesas

Los cobros se muestran agrupados por estados:

- **Pendientes:** Remesas aún no enviadas al banco
- **Enviadas:** Remesas ya enviadas al banco
- **Validadas:** Remesas enviadas y cobradas

### Estructura del formulario de remesa

El formulario posee dos secciones diferenciadas:
- **Parte superior:** Cabecera de la remesa de cobro
- **Parte inferior:** Conjunto de pestañas

### Cabecera de la remesa

Los únicos datos obligatorios son:
- **Descripción**
- **Forma de cobro**

Se muestran otros datos como:
- Fecha de envío al banco
- Fecha de vencimiento
- Fecha de validación
- Importe de la remesa
- Margen de días

> **Nota:** La forma de cobro determina cómo se quieren gestionar los recibos y el modelo del asiento a generar en la contabilización.

### Pestañas de la remesa

#### Básico
- Datos bancarios del cobro
- Datos del ordenante
- Permite añadir observaciones para impresiones

> **Nota:** Por defecto, el sufijo bancario es "000". Para otros códigos: `Tablas maestras >> GENERAL >> Sufijo para remesas`.

#### Pendientes
Se añaden y quitan los recibos pendientes de cobro.

#### Cobrados
Se muestran los recibos cobrados. Si se marcan como cobrados, los asientos se generan automáticamente.

> **Nota:** Si quieres generar asientos manualmente, desactivar la propiedad correspondiente.

#### Devueltos
Se muestran los recibos devueltos por el banco.

> **Nota:** Para volver a generar un recibo devuelto, seleccionar "Generar recibo hijo".
> **Nota:** Si una línea se muestra en verde, significa que es un recibo de una devolución.

#### Apuntes
Se van generando según los recibos se ponen como cobrados o devueltos.

> **Nota:** La forma de cobro seleccionada determinará el modelo de apuntes. Se generarán apuntes vinculados a la forma de cobro (ej: "A vencimiento: CO" cobran directamente; "A descuento: CA" puede generar cuenta puente).

#### Ficheros
Se pueden asociar documentos digitalizados, capturados o arrastrados.

### Crear y gestionar una remesa de cobro

#### Procedimiento general

La aplicación permite realizar múltiples acciones en torno a las remesas de cobro: crear, añadir recibos, enviar al banco, dar por cobrados, etc.

> **Nota:** La remesa gestiona el cobro de manera masiva, es decir, cobra y genera el apunte al poner fecha de cobro.

#### Consideraciones importantes

- **F. envío al banco:** Si se cubre, se bloquea la remesa y no se permite añadir recibos. Se habilitan botones de "Cobrar recibos" y "Devolver recibos"
- **Correcciones:** Si el usuario se equivoca, se permite borrar la fecha y quitar el recibo
- **F. vencimiento:** Será la fecha última que prevalezca, aunque haya otra en los recibos
- **Margen de días:** Si hay datos en este campo, vencerá en esa fecha
- **Prioridad:** Es posible cambiar la prioridad de prevalencia
- **F. validación:** Es la que da por resuelta y gestionada la remesa
- **Recibos devueltos:** Es necesario generar los recibos hijos para poder reenviar

### Cuadernos de envío al banco

Los cuadernos son ficheros con estructura estándar para mandar la orden al banco. La elección del cuaderno dependerá del tipo de devolución realizado.

> **Ejemplo:** Cuaderno B2B Core permite máximo 2 días de devolución.

Según el tipo de remesa estarán activos unos cuadernos u otros.

---

## Contabilización de Pagos/Cobros, Pagarés

Este módulo permite registrar, gestionar y contabilizar operaciones de cobro y pago mediante pagarés, tanto emitidos como recibidos.

**Ruta de acceso:** `Ventas >> Gestión de cobros >> Contabilización de pagos/cobros, pagarés`

### Vista general de registros

Al entrar aparece una tabla con todos los pagarés existentes para la empresa seleccionada.

#### Selección de empresa y fecha
- **Desplegable Empresa:** (ej. Tireworld, S.A.)
- **Campo Desde fecha:** Filtrar registros a partir de un día concreto

#### Pestañas de estado

- **Pendientes:** Pagarés aún no cobrados ni pagados
- **Pagados:** Operaciones ya contabilizadas como cobro o pago efectivo
- **Devueltos:** Pagarés rechazados por el banco
- **Anulados:** Borradores o registros cancelados antes de contabilización

#### Columnas clave

| Campo | Descripción |
|-------|------------|
| **Cód. Documento y Número** | Tipo (pagaré) y folio |
| **Razón social / Nombre comercial** | Tercero implicado |
| **Cód. cliente / Cód. proveedor** | Vinculación automática |
| **F. emisión / recepción** | Fechas con selector de calendario |
| **F. vencimiento** | Plazo legal |
| **F. envío banco** | Cuando se presenta al cobro |
| **Importe** | Valor monetario |
| **Cuenta bancaria** | IBAN usado |
| **Emisión / Recepción / Contabilizado** | Checkboxes de estado |
| **Apuntes no contabilizados** | Número de asientos pendientes |

### Formulario de detalle del pagaré

#### Datos generales

| Campo | Descripción |
|-------|------------|
| **Empresa** | Desplegable para cambiar compañía |
| **Número** | Alfanumérico, generable o editable |
| **Emisión / Recepción** | Fecha de formalización |
| **Vencimiento** | Plazo legal del pagaré |
| **Envío a banco** | Cuando se presenta al cobro |
| **Pago / Cobro** | Día efectivo de la transacción |
| **Devolución** | En caso de rechazo |
| **Impreso y Anulado** | Auditoría interna |
| **Importe** | Validado que coincida con suma de recibos |
| **Tipo** | Selector (emitido, recibido) |
| **Cliente / Proveedor** | Campo con autocompletar y lupa |
| **Razón social y NIF** | Se rellenan automáticamente |

#### Dirección

- **Dirección, País, Provincia, Localidad, C.P**
- Estos datos sirven para generar asientos contables con la cuenta fiscal correcta

#### Banco

| Campo | Descripción |
|-------|------------|
| **Cuenta bancaria** | Desplegable con cuentas habilitadas |
| **Entidad, Oficina, DC, Cuenta** | Se rellenan al elegir o manualmente |
| **IBAN / SWIFT-BIC** | Imprescindibles para internacionales |

> **Nota:** Se bloquea edición tras la primera contabilización.

#### Otros datos

| Campo | Descripción |
|-------|------------|
| **Gastos** | Comisiones, timbres u otros costes |
| Pueden especificarse como porcentaje o cantidad fija |
| **Validación** | Evita que gastos superen porcentaje configurable |

#### Observaciones

Campo multilineal libre para apuntes internos, histórico de cambios o instrucciones.

### Pestañas adicionales del formulario

#### Básico
Vista principal con todos los campos descritos.

#### Recibos
Listado de recibos electrónicos o físicos generados del pagaré. Botones para crear, importar o exportar en formatos SEPA.

#### Apuntes
Muestra el asiento contable vinculado: débitos y créditos automáticos. Permite previsualizar antes de contabilizar.

#### Ficheros
Área de arrastrar y soltar para adjuntar PDFs, imágenes o documentos escaneados.

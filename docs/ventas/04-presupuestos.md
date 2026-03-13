# Presupuestos

El presupuesto es el documento a partir del cual el cliente valida las referencias pedidas e inicia el ciclo de ventas.

**Ruta de acceso:** `Ventas >> Presupuestos`

## Acceso al formulario

Elastic BUSINESS dispone del formulario Presupuestos de ventas al que se accede a traves del:
- Menú desplegable
- O directamente a través del icono de acceso rápido de la barra de botones

## Pestañas de estado

En la pantalla principal se pueden ver presupuestos diferentes estados:

- **En estudio:** Se muestran presupuestos que todavía están en elaboración
- **Abiertos:** Se muestran presupuestos que se han recibido, pero todavía no se han confirmado
- **Aceptados:** Se muestran los presupuestos que tienen generado un pedido
- **No aceptados:** Se muestran los presupuestos rechazados
- **Anulados:** Se muestran los presupuestos anulados. Se permite controlar motivo de anulación
- **Todos:** Se muestran todos los presupuestos realizados independientemente del estado

## Estructura del presupuesto

La ventana del presupuesto posee dos secciones perfectamente diferenciadas:

### Parte superior - Cabecera del presupuesto

En la cabecera se encuentran los datos principales de identificación del cliente y otros datos importantes en la gestión de este:

| Campo | Descripción |
|-------|------------|
| **Cliente** | Campo obligatorio. Según la configuración existente, se precargan datos desde la ficha correspondiente |
| **Moneda** | Precargada desde el cliente |
| **Conversión** | Factor de cambio si es una moneda diferente a la de la empresa |
| **Fecha de documento** | Editable según las necesidades |

> **Nota:** Una vez seleccionado el cliente, según la configuración existente, se precargan datos como la moneda, la conversión, la fecha de documento, etc. Todos ellos editables según las necesidades.

### Parte inferior - Pestañas del presupuesto

Un conjunto de **7 pestañas** donde se muestran los datos e información referentes al presupuesto:

## Pestaña Básico

Pestaña que sirve para definir el estado del presupuesto e identificar al cliente. Existe la posibilidad de utilizar el campo observaciones para anotar una incidencia o aclaración referente al presupuesto.

### Datos básicos - Datos generales

| Campo | Descripción |
|-------|------------|
| **Dirección (Fiscal)** | Datos de la dirección fiscal por defecto |
| **C.P** | Código postal |
| **País** | País |
| **Provincia** | Provincia |
| **Localidad** | Localidad |
| **Dirección (Cliente)** | Filtro de selección de direcciones ya configuradas en el cliente |
| **Contacto** | Contacto definido por defecto en el cliente. En la lupa se permite seleccionar otro |
| **Oferta cliente** | Campo abierto que hace referencia al nº del presupuesto utilizado por el cliente |
| **Observaciones** | Campo libre para definir cualquier incidencia. Solo se visualiza en el documento |
| **Observaciones internas** | Campo libre para incidencias de carácter interno. Se arrastran al pedido |

### Datos básicos - Otros datos generales

Información relativa al presupuesto que no procede añadir a Observaciones.

### Datos básicos - Datos de transporte

| Campo | Descripción |
|-------|------------|
| **Tipos de portes** | Datos de la dirección fiscal por defecto |
| **Modelo de portes** | Modelo seleccionado |
| **Transportista** | Empresa transportista |
| **Matrícula** | Matrícula del vehículo |
| **Ref. transportista** | Referencia del transportista |
| **Contacto** | Nombre del contacto en la empresa transportista |
| **Tlf. contacto** | Número de teléfono del contacto |
| **Peso bruto (Kg)** | Peso total incluido el embalaje |
| **Peso neto (Kg)** | Peso sin incluir el embalaje |
| **m³** | Volumen total en metros cúbicos |
| **Bultos** | Número total de bultos |
| **Palés** | Número total de palés |
| **Observaciones de transporte** | Observaciones relativas al transporte |

## Pestaña Gestión

Esta pestaña hace referencia a los importes que se necesitan para el presupuesto. Es una pestaña de información completa donde poder ver toda la información monetaria.

### Datos de pago

| Campo | Descripción |
|-------|------------|
| **Formas de cobro** | Método o medio a través del cual se realizará el cobro |
| **Período de cobro** | Intervalo de tiempo en el que se espera realizar el cobro |

### Importes detalles

| Campo | Descripción |
|-------|------------|
| **Importe bruto** | Importe total antes de descuentos o impuestos |
| **Importe neto** | Importe total después de descuentos, antes de impuestos |
| **Base** | Importe sobre el cual se calculan los impuestos (IVA) |
| **Dto. línea** | Importe del descuento en línea |
| **Dto. general** | Importe del descuento general |
| **Dto. pronto pago** | Importe del descuento por pronto pago |
| **IVA** | Porcentaje y cantidad |
| **RE** | Importe del Recargo de Equivalencia |

### Importes transporte

| Campo | Descripción |
|-------|------------|
| **Facturar portes** | Check que se activa si debe facturarse el porte al cliente |
| **Base** | Gasto planificado imputado |
| **Manual** | Check para imputar costes de forma manual |
| **Coste transporte** | Campo donde se pueden imputar los costes |
| **Tipo IVA** | IVA imputado al transporte |
| **IVA** | Porcentaje aplicado e importe resultante |

### Importes totales

| Campo | Descripción |
|-------|------------|
| **Base total** | Importe sobre el cual se calculan los impuestos |
| **Importe total** | Base total + IVA |
| **Impuestos totales** | IVA aplicado a la base total |
| **Importe total ME** | Base total + IVA en moneda extranjera |

## Pestaña Líneas

Está formada por una tabla principal donde se añaden las líneas de artículos que se van a incluir en el presupuesto.

### Campos principales de la tabla

| Campo | Descripción |
|-------|------------|
| **Cod. Artículo** | Código del artículo. Al introducirlo, se completa automáticamente. Editable |
| **Descripción** | Descripción completa del artículo. Editable |
| **Cantidad** | Campo que habrá que cubrir |
| **Ud. Cant** | Unidad de medida del artículo. Editable |
| **Importe tarifa** | Campo editable o precargado si el artículo está relacionado con el cliente |
| **Unidad de tarifa** | Campo editable o precargado por defecto |
| **Descuento** | Desplegable con descuentos del cliente |
| **% dto** | Campo a cubrir manualmente para indicar un descuento |
| **IVA** | Porcentaje de IVA que se puede cambiar |

### Apartado Márgenes

Se mostrará el margen sobre ventas y el margen sobre costes.

### Cómo añadir una línea

Existen diferentes formas de añadir una línea:

#### 1. Crear líneas sin artículos
Funcionaría como un campo de texto para realizar anotaciones.

#### 2. Insertar artículos a través de su código
Escribir en la columna código el código del artículo y se autocompletará la información.

#### 3. Icono "Artículos"
Al pulsar el icono aparece un desplegable con tres subpestañas:
- **Artículos cliente:** Artículos que tiene relacionado el cliente en su ficha
- **Todos los artículos:** Muestra todos los artículos creados
- **Cesta de artículos:** Muestra artículos añadidos

Aquí solo hay que cubrir la cantidad de artículo y el precio si se necesita.

### Crear un artículo paramétrico

Para añadir un nuevo artículo que no existe en el almacén:

1. Pulsar el icono de **Configurar**
2. Se despliega una ventana donde se selecciona una familia o se añaden valores
3. Si el artículo ya está creado, el sistema lo añade automáticamente
4. Si no existe, pregunta si se desea crear

> **Nota:** Lo más conveniente es usar los parámetros que tienen configurados las familias.

Tras crear el artículo se muestra una ventana para añadir:
- Código externo
- Descripción externa
- Precio unitario

> **Obligatorio:** Pulsar la cruz verde para añadirlo.

> **Nota:** Si solo se conoce el comienzo del código del artículo, escribirlo acompañado de un asterisco (*) para que el sistema abra una ventana de selección.

## Pestaña Comerciales adicionales

Se pueden añadir comerciales adicionales, a mayores del añadido en la cabecera del documento. Se puede seleccionar la comisión que aplica al documento.

## Pestaña Documentos asociados

Se mostrarán los documentos relacionados con el presupuesto:
- Pedidos
- Órdenes de preparación/carga
- Albaranes
- Facturas

## Pestaña Adicional

Se muestran datos adicionales como:
- Información de fechas
- Información del pedido
- Acceso directo al pedido

Para eliminar un presupuesto:
1. Pasarlo a estado **Anulado** (no se pueden eliminar directamente)
2. Ir a la pestaña **Adicional**
3. Meter una **fecha de anulación**
4. Guardar
5. Pasará a la pestaña "Anulados"

## Pestaña Ficheros

Se asocian documentos digitalizados. Se pueden:
- Capturar directamente desde un origen
- Arrastrar a la pestaña para adjuntar directamente
- Escanear directamente un documento

Para adjuntar un fichero pulsar el icono del clip azul y seleccionar el fichero del ordenador.

## Botones de acción (icono engranaje)

### Nueva versión

Una vez creado el cuerpo del presupuesto procede definir el contenido de este:

1. Entra en un presupuesto creado anteriormente haciendo clic sobre él
2. Pulsa el engranaje y haz clic en **"Nueva versión"**
3. La nueva versión ya está creada, ahora se puede modificar sin perder la traza de la versión anterior

### Generar pedido (F2)

Una vez elegido un presupuesto y una versión del mismo:

1. Selecciona un presupuesto
2. Pulsa en **Acciones** (icono engranaje) y selecciona **Generar Pedido (F2)**
3. Se abre una ventana preguntando si quieres acceder al pedido directamente
4. Se da de alta el nuevo documento en el formulario Pedidos
5. El presupuesto pasa automáticamente a la carpeta Cerrados

### Mandar líneas a pedido

Con esta acción se pueden enviar líneas concretas de un presupuesto a pedido. Útil cuando en un mismo presupuesto se oferta el mismo producto en intervalos de cantidad diferentes.

### Generar mantenimiento

Permite generar un mantenimiento asociado al presupuesto.

### Clonar un presupuesto

La operación de clonado consiste en generar uno nuevo exactamente igual al anterior:

1. Selecciona un presupuesto ya existente
2. Pulsa en **Acciones** (icono engranaje) y selecciona **Clonar**
3. Automáticamente se genera un nuevo presupuesto
4. Puedes modificar los datos (cliente, líneas, etc.)

### Imprimir versión

Para imprimir una versión del presupuesto:

1. Selecciona el presupuesto
2. Pulsa **Imprimir documento** (icono impresora)
3. En la ventana emergente selecciona el tipo de formulario a imprimir
4. Pulsa **Imprimir**

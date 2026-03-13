# Clientes

El cliente es la entidad en torno a la que gira todo el proceso de ventas. En esta entrada se crean los clientes y se gestionan sus datos generales.

**Ruta de acceso:** `Ventas >> Clientes`

---

## Estructura de la pantalla principal

En la pestaña principal se puede ver a la izquierda un desplegable con los clientes, dividido por **Listado** y **Empresa**.

En la zona central tenemos **6 pestañas** donde se dividen los clientes por su estado:

### Estados de clientes

- **Activos:** Clientes que actualmente tienen una relación comercial activa con la empresa. Están utilizando productos o servicios y pueden realizar operaciones sin restricciones.

- **Bloqueados:** Clientes cuya cuenta ha sido temporalmente restringida. Esto puede deberse a problemas de pago, verificaciones pendientes u otras razones administrativas.

- **De baja:** Clientes que han finalizado su relación con la empresa, ya sea por decisión propia o por parte de la empresa. No pueden acceder a servicios ni realizar operaciones.

- **Todos:** Vista que muestra el total de clientes registrados en el sistema, sin importar su estado (activos, bloqueados, de baja, etc.).

- **Potenciales:** Contactos o registros de personas o empresas que aún no son clientes, pero que podrían convertirse en uno. Suelen estar en proceso de seguimiento comercial o preventa.

- **Grupos:** Conjunto de clientes agrupados bajo una misma categoría, nombre o característica común. Puede utilizarse para gestión colectiva, promociones o reportes.

- **Grupos de baja:** Grupos en los que todos los clientes integrantes se encuentran dados de baja. Sirve para mantener un historial organizado o para análisis posteriores.

## Crear un nuevo cliente

Para crear un nuevo cliente se tiene que pulsar el icono **"Añadir registro"** (cruz verde). Se desplegará una ventana dividida en **8 pestañas**:

## Cabecera del cliente

Esta sección contiene los datos básicos que serán fijos una vez se creen.

| Campo | Descripción |
|-------|------------|
| **Código** | Asignado por la aplicación de forma secuencial según la configuración de contadores para los clientes |
| **NIF** | Número de identificación fiscal |
| **Razón social** | Se completa con la empresa |
| **Nombre comercial** | Nombre comercial del cliente |
| **Fecha creación** | Fecha en la que se da de alta el cliente |
| **Ult. modificación** | Fecha de la última modificación en cualquier campo del cliente |
| **Tipo de cliente** | Seleccionar el tipo de cliente (Nacional, Internacional, etc.) |

> **Nota:** Los tipos de clientes estarán creados en el arranque por el equipo de Elastic. Para revisar esta configuración: `Aplicación >> Configuración >> Configuración de clientes`. Solo accesible para administradores.

## Pestaña Resumen

Esta pestaña contiene los datos principales de contacto del cliente, la dirección del cliente, los datos administrativos referentes a las cuentas y formas de cobro, y otros datos adicionales.

### Bloques principales

#### CONTACTO
| Campo | Descripción |
|-------|------------|
| **Nombre** | Nombre completo del contacto principal del cliente |
| **Teléfono** | Número de teléfono del contacto principal |
| **Email** | Dirección de correo electrónico del contacto principal |

#### DIRECCIÓN FISCAL/DE ENVÍO
| Campo | Descripción |
|-------|------------|
| **Dirección** | Dirección fiscal/de envío del cliente |
| **Localidad** | Localidad de la dirección |
| **Provincia** | Provincia de la dirección |
| **Email** | Dirección de correo electrónico de la dirección |
| **C. Postal** | Código postal de la dirección |
| **País** | País de la dirección |
| **Teléfono** | Número de teléfono de la dirección |

#### ADMINISTRACIÓN
| Campo | Descripción |
|-------|------------|
| **Cuenta contable** | Se autocompleta con el tipo de cliente |
| **IVA** | Se autocompleta con el tipo de cliente |
| **Cuanta bancaria** | Cuenta bancaria del cliente |
| **Forma de cobro** | Se autocompleta con el tipo de cliente |
| **Cliente varios** | Permite cambiar el cliente del documento por otro con este mismo check marcado |
| **Bloqueado** | Check que indica si está bloqueado el cliente |
| **De baja** | Check que indica si está de baja el cliente |

#### ADICIONAL
| Campo | Descripción |
|-------|------------|
| **Idioma** | Idioma principal de comunicación con el cliente |
| **Zona** | Clasificación de cliente por zona |
| **Subzona** | Clasificación de cliente por subzona |
| **Sector** | Sector o mercado al que pertenece el cliente |
| **Transportista** | Transportista asociado al cliente |
| **ABC** | Clasificación ABC del cliente |
| **Clase** | Otra clasificación disponible para los clientes |

#### OBSERVACIONES
| Campo | Descripción |
|-------|------------|
| **Observaciones** | Observaciones de carácter externo, se muestran en las impresiones de los documentos |
| **Observaciones internas** | Observaciones de carácter interno, no se muestran en las impresiones de los documentos |

## Pestaña Agenda

Esta pestaña está dividida en dos **subpestañas**, que deben crearse para que la pestaña Resumen muestre sus datos correctamente:

> **Nota importante:** Estas pestañas se retroalimentan entre ellas. Es importante seguir un orden riguroso con lo que se completa.

### Subpestaña Contactos

En esta subpestaña va principalmente el contacto o contactos del cliente y cómo poder contactar con él. El contacto que metamos saldrá reflejado en la pestaña Resumen.

Se divide a su vez en otras cuatro subpestañas:
- Email
- Números
- Direcciones
- Redes sociales

#### Checks importantes
- **No enviar mails:** Sirve para no tener en cuenta los mails configurados cuando se quieran enviar mails masivamente en campañas (CRM)
- **Enviar facturación:** Precarga la dirección de correo electrónico por defecto cuando se quiera enviar una factura por mail
- **Enviar albaranes:** Precarga la dirección de correo electrónico por defecto cuando se quiera enviar un albarán por mail

### Subpestaña Direcciones

En esta subpestaña van principalmente las direcciones del cliente. La dirección que metamos saldrá reflejada en la pestaña Resumen.

Se divide a su vez en otras tres subpestañas:
- Números
- Emails
- Redes sociales

#### Notas sobre las direcciones
- **Si la dirección es marcada como Fiscal:** aparecerá en la pestaña Resumen
- **Si la dirección es marcada como Envío mercancía y Dirección de envío por defecto:** aparecerá en la pestaña Resumen
- **La configuración del check** de "Envío factura" o "Envío mercancía" depende del Tipo de dirección
- **Si un email tiene marcado** el check de "Envío factura", éste se precargará cuando se utilicen las herramientas automáticas de envío de facturas

## Pestaña Políticas

Esta pestaña engloba todo lo que tiene que ver con las relaciones comerciales con el cliente. Los datos obligatorios son la **moneda** y el **idioma**.

| Campo | Descripción |
|-------|------------|
| **Moneda** | Desplegable que muestra todas las monedas disponibles. Hace referencia a la moneda con la que trabajará el cliente |
| **Idioma** | Idioma predefinido de los documentos del cliente |
| **Dto. P.P.** | Porcentaje de descuento pronto pago si lo tiene el cliente |
| **Rappel** | Rappel por volumen de ventas |
| **Cliente varios** | Check que vendrá marcado si se puso en el tipo de cliente |
| **Múltiplo de ventas** | Se desglosan diferentes configuraciones para los avisos de los múltiplos de ventas configurados en los artículos |
| **Incoterm** | Desplegable que muestra los incoterms creados en las tablas maestras |
| **Punto de entrega** | Lugar donde se recibe la mercancía |

### Subpestañas de Políticas

Esta pestaña está formada por **5 subpestañas**:

#### Artículos
Se crea el catálogo de artículos de un cliente. Los artículos tienen código y descripción, interno y externo.

> **Nota:** El sistema da la posibilidad de importar masivamente artículos de cliente utilizando la opción **Importación de artículos**.

#### Tarifas
Se pueden asociar tarifas ya creadas en el sistema. Una vez creada, podemos añadir los artículos relacionando todos los artículos que hayamos asociado al cliente previamente.

#### Descuentos
Se pueden asociar descuentos ya configurados en el sistema.

#### Comerciales
Se pueden asociar comerciales ya configurados en el sistema.

#### Rappels
Permite añadir rappels en función del importe comprado al cliente durante un plazo definido, de forma escalonada.

## Pestaña Administración

Esta pestaña engloba los datos administrativos y está dividida en cuatro subpestañas.

### Subpestaña Configuración

Muestra los datos administrativos necesarios para la venta.

| Campo | Descripción |
|-------|------------|
| **Tipo de operación** | Tipo de operación del IVA por defecto del cliente |
| **IVA** | IVA que llevará por defecto en documentos de ventas |
| **Tipo de recibo** | Tipo de recibo que sirve para definir el modelo de apunte generado |
| **Importe mínimo venta** | Cantidad mínima que pagará el cliente por venta |
| **Rec. Equiv** | Recargo de equivalencia configurado por defecto para el cliente |
| **Tipo de venta** | Ventas que realiza el cliente. Se arrastra a facturas y albaranes por defecto |
| **De baja** | Habrá que completar el campo de fecha para darlo de baja |
| **Evaluable** | Entrará en el grupo de clientes sujetos a evaluación |
| **En cuarentena** | Habrá que completar el campo de fecha para que entre en cuarentena |
| **Criterio de caja** | La liquidación del IVA se hace solo cuando el cliente cobra |
| **Agrupar facturación** | Se agrupan los albaranes del cliente al hacer una facturación múltiple |
| **Cliente de consigna** | Cuando se compra su mercancía entra en consigna |
| **Albarán no facturable** | No se facturan los albaranes |
| **Nº Copias original** | Número de facturas que se imprimirá con el texto definido en "Texto copias original" |
| **Texto copias original** | Texto que se mostrará en las facturas impresas por primera vez |
| **Texto duplicado** | Texto que se mostrará en las facturas impresas después de las originales |
| **Ocasional** | Marca a este cliente como no habitual |
| **Interno** | Identifica al cliente como interno a la empresa |

### Subpestaña Finanzas

En esta subpestaña se añaden todas las cuentas bancarias y cuentas contables necesarias.

#### Cuentas bancarias
Para crear una nueva cuenta bancaria asociada a un cliente:
1. Clicar en la cruz verde
2. Cubrir el **IBAN** como el **SWIFT/BIC** del cliente
3. La moneda vendrá cubierta por defecto en euros

#### Mandatos
En esta pestaña se configurarán los mandatos de los bancos del cliente, necesarios para la gestión de remesas y la generación de ficheros SEPA CORE y SEPA B2B.

#### Cuentas contables
Por defecto aparecerán las diferentes cuentas contables del cliente.

### Subpestaña Políticas de cobro

En esta subpestaña se establecen los términos y condiciones para realizar los pagos a clientes/acreedores. Se divide en cuatro apartados:

#### Formas de cobro
Para asignar la forma de pago que tendrá el cliente:
1. Clicar en la cruz verde
2. Se mostrará una ventana con las formas de cobro configuradas
3. La forma de cobro por defecto aparecerá en albaranes y facturas

> **Nota:** Tanto en albaranes como en facturas se puede cambiar la forma de cobro.

#### Períodos de cobro
Para asignar el período de cobro:
1. Clicar en la cruz verde
2. Se mostrará una ventana con los períodos de cobro configurados
3. El período por defecto aparecerá en albaranes y facturas

#### Períodos de no cobro
Se puede poner una fecha de inicio y una final para que durante ese plazo no se cobre al cliente. Existe un check para marcar que se repita anualmente.

#### Riesgo
Se puede configurar el riesgo admitido para el cliente. En la aplicación saltará un aviso si nos pasamos de este.
- **Obligatorios:** código y límite
- **Límite:** importe de riesgo que concedemos al cliente
- **Código:** con quien gestiona el riesgo el cliente

## Pestaña Empresas y grupos

Esta entrada está formada por dos subpestañas:

- **Empresas:** Vendrá completada por defecto con la empresa donde se haya creado el cliente. Si hay multiempresa pueden añadirse las que se necesiten
- **Grupos:** Aparecerán los grupos de empresas a los que pertenezca el cliente

## Pestaña Adicional

Se muestran principalmente datos relacionados con la zona, sector y ámbito del cliente. El **tipo de identificación fiscal** es el dato obligatorio. También permite añadir una imagen.

> **Nota:** El usuario y la contraseña hacen referencia al acceso de la B2B (si está creada para la empresa)

## Pestaña Ficheros

Se asocian documentos digitalizados. Se pueden:
- Capturar directamente desde un origen
- Arrastrar a la pestaña para adjuntar directamente
- Escanear directamente un documento

Para adjuntar un fichero pulsar el icono del clip azul y seleccionar el fichero del ordenador.

## Pestaña Locales

Sirve para definir diferentes Locales del cliente si aplica para este (por ejemplo, diferentes tiendas si es un cliente con varias localizaciones).

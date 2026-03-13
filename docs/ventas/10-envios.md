# Envíos

Una vez generado el albarán, tenemos la posibilidad de generar el envío. El envío se crea con **doble funcionalidad**:

1. **Gestionar el envío real físico** del día
2. **Provocar la salida de almacén** del contenido del pedido a través del cierre del envío

**Ruta de acceso:** `Ventas >> Envíos`

> **Nota:** Existe la posibilidad de dar de baja la mercancía directamente desde el albarán dependiendo de una propiedad. Si la mercancía se ha dado de baja en el albarán directamente, la figura del envío solo sirve para gestionar las salidas del día.

## Estructura del formulario del envío

Se podrá ver en la parte superior la **cabecera** del envío, y en la parte inferior un conjunto de **tres pestañas**.

## Cabecera del envío

Aparecen los datos básicos de identificación del documento referentes al envío.

| Campo | Descripción |
|-------|------------|
| **Envío** | Nº del envío generado automáticamente a través del contador interno o configurado |
| **Nº de expedición** | Campo editable para personalizar el número con el código del proveedor de servicios |
| **Almacén** | Almacén por defecto de donde sale la mercancía. Se puede forzar cambiando la denominación |
| **Subalmacén** | Subalmacén por defecto. Se puede forzar cambiando la denominación |
| **Fecha prevista** | Fecha en la que se prevé que salga la mercancía |
| **Fecha real** | Fecha real en la que salió la mercancía |
| **Transportista** | Combo para seleccionar el transportista |

## Pestaña Albaranes

En esta pestaña se detallan todos los albaranes incluidos en ese envío.

| Campo | Descripción |
|-------|------------|
| **Albarán** | Nº de identificación del albarán incluido en el envío |
| **Fecha creación** | Fecha de creación del albarán |
| **Razón social** | Cliente al que pertenece el albarán |
| **Transportista** | Transporte asignado por defecto en el albarán |
| **Portes** | Tipo de portes del albarán |
| **Forma de cobro** | Forma de cobro asociada al albarán |
| **Observaciones** | Campo para comentarios al transportista |
| **Expedido** | Check que indica si el albarán ha sido expedido |

> **Nota:** Si la mercancía se dio de baja en el albarán directamente, este check estaría marcado.

## Pestaña Detalles

En esta pestaña se muestran los detalles de los artículos incluidos en el envío línea a línea.

| Campo | Descripción |
|-------|------------|
| **Albarán** | Nº de identificación del albarán |
| **Cod. artículo** | Código del artículo |
| **Descripción** | Descripción del artículo |
| **Cantidad** | Cantidad que sale en ese albarán |
| **Familia** | Familia a la que pertenece el artículo |
| **Cantidad total** | Cantidad total en todo el envío |
| **Unidad** | Unidad de gestión del artículo |
| **Almacén** | Almacén por defecto |
| **Subalmacén** | Subalmacén por defecto |
| **Lote asociado** | Check que indica si está asociado a lote de trazabilidad |

## Configurar envíos

Existen dos formas de configurar los envíos:

### Forma 1: Desde el albarán
Usar la funcionalidad **"Añadir a envío"** (ver apartado Albarán).

### Forma 2: Crear envío y añadir albaranes
Esta es la forma principal que se describe aquí.

#### Pasos a seguir:

1. **Situarse** en el formulario Envíos
2. **Limpiar campos** mediante "Borrar campos"
3. **Pulsar Insertar** para activar los campos
4. **Rellenar** los campos de la cabecera del formulario

> **Nota:** Por defecto se propondrá el almacén y subalmacén definido para salidas por defecto. Si deseas que la baja se realice de otro, modificar estos campos.

5. **Pulsar Insertar** para crear el envío
6. **Ir a Acciones** y seleccionar **"Configurar envío"**
7. **Seleccionar** en la ventana emergente los albaranes a insertar

## Cerrar envío

Una vez configurado el envío con todos los albaranes que lo componen, se debe cerrar. Con esto se provoca que todo el contenido del albarán se dé de baja del almacén.

> **Importante:** La baja se producirá desde el almacén y subalmacén definido en la cabecera del envío.

### Pasos a seguir:

1. **Seleccionar** en el árbol el envío a cerrar
2. **Pulsar Acciones** y seleccionar **"Cerrar envío"**

> **Advertencia:** Este proceso no tiene marcha atrás. En el momento del cierre se da de baja toda la mercancía del almacén. Si existe algún error en el contenido del envío, luego deberá ser regularizado manualmente.

## Impresión

Se da la posibilidad de asociar a los envíos impresiones, como, por ejemplo, una nota de carga.

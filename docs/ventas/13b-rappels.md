# Rappels

Los rappels (también llamados bonificaciones o descuentos por volumen) son reducciones de precio o devoluciones de dinero aplicadas en función del volumen de ventas alcanzado durante un período definido.

**Ruta de acceso:** `Ventas >> Configuración >> Rappels`

## Concepto

Un rappel es una bonificación que se otorga al cliente cuando sus compras alcanzan un volumen determinado durante un período establecido. A diferencia de los descuentos aplicados en el momento, los rappels se calculan y facturan posteriormente mediante una factura de abono o de descuento.

## Estados de rappels

Los rappels se muestran agrupados en función del estado en que se encuentren:

### Abiertos

Se muestran los rappels en uso en ese momento. Un rappel abierto es:
- Vigente durante su período de validez
- Susceptible de generar facturas de rappel
- Activo para la acumulación de ventas

### Cerrados

Se muestran los rappels que ya no están vigentes. Un rappel cerrado es:
- Finalizado su período de vigencia
- Ya no acumula nuevas ventas
- Registro histórico de rappels anteriores

## Crear un rappel

Para crear un nuevo rappel:

1. **Acceder** al formulario de Rappels
2. **Pulsar** en la cruz verde en la sección de cabecera para insertar un nuevo registro
3. **Se despliega** una ventana donde completar los datos

### Datos obligatorios

Para crear un rappel son imprescindibles:
- **Cliente:** El cliente al que va dirigido
- **Fecha de inicio:** Cuándo comienza el período del rappel
- **Fecha de fin:** Cuándo finaliza el período

### Estructura del formulario de rappel

El formulario posee dos secciones diferenciadas:

#### Parte superior - Cabecera del rappel

Contiene los datos principales:
- Cliente
- Período del rappel
- Datos generales

#### Parte inferior - Listado de facturas

Se muestra el listado de facturas asociadas al rappel seleccionado durante el período definido.

## Gestionar un rappel

### Localizar un rappel

Desde el formulario de búsqueda:
1. Seleccionar los filtros deseados (cliente, fechas, etc.)
2. Una vez localizado el rappel, hacer **doble clic** sobre el detalle

### Asociar facturas

Las facturas se asocian automáticamente o manualmente:

**Automáticamente:** El sistema relaciona todas las facturas del cliente dentro del período del rappel que cumplen las condiciones.

**Manualmente:** Se pueden añadir o quitar facturas específicas según sea necesario.

### Crear factura de rappel

Una vez que el período del rappel ha finalizado y se desean facturar los descuentos acumulados:

1. **Pulsar** el engranaje en la esquina superior derecha (botón Acciones)
2. **Seleccionar** "Crear factura de rappel"
3. El sistema genera una factura de crédito o descuento según configuración

#### Requisito previo

Para que sea posible crear una factura de rappel, es **imprescindible** que en la empresa se cree un **artículo de servicio específico para los rappels**.

**Para crear el artículo:**

1. Ir a: `Laboral >> Empresas y centros de trabajo >> Configuración`
2. Pestaña: **Adicional**
3. Sección: **Ventas**
4. Introducir el **servicio creado únicamente para ello** (ej: "Bonificación por Volumen", "Rappel")

## Cerrar un rappel

Cuando el período del rappel finaliza:

1. **Acceder** al rappel mediante doble clic
2. **Marcar** con un check la casilla **"Cerrado"**
3. **Guardar** los cambios
4. El rappel **pasará a la pestaña de "Cerrados"**

> **Nota:** Los rappels cerrados quedan como registro histórico pero ya no aceptan nuevas facturas ni pueden generar nuevas facturas de rappel.

---

## Configuracion de Rappels

La configuración de rappels permite definir escalas de bonificación que se aplicarán automáticamente según el volumen de compras.

**Ruta de acceso:** `Ventas >> Configuración >> Configuración rappels`

## Concepto

Una configuración de rappel es una plantilla que define:
- Los intervalos de importe
- El descuento a aplicar en cada intervalo
- Los clientes o grupos a los que se aplica

Permite configurar de forma centralizada y luego aplicar estas reglas a múltiples rappels.

## Estados de configuración

### Activas

Se muestran todas las configuraciones creadas que están en uso en ese momento. Una configuración activa:
- Se puede utilizar para crear rappels
- Se puede edutar si es necesario hacer cambios
- Pasará a "Inactivas" al marcar el check de "Inactivo" en el detalle

### Inactivas

Se muestran aquellas configuraciones de rappel que están marcadas como inactivas. Cuando una configuración es inactiva:
- No se puede utilizar para nuevos rappels
- Funciona como registro histórico
- Conserva los datos para referencia

## Crear una configuracion de rappel

Para crear una nueva configuración:

1. **Pulsar** en la cruz verde para añadir un nuevo registro
2. **Se despliega** una ventana donde aparece:
   - Cabecera (datos generales)
   - Dos subpestañas (Importes y Cliente/Grupo de empresas)

## Cabecera de la configuracion

Contiene los datos generales de la configuración:

| Campo | Descripción |
|-------|------------|
| **Descripción** | Nombre descriptivo de la configuración (obligatorio) |
| **Fecha inicio** | Fecha de inicio de validez de la configuración (obligatorio) |
| **Fecha fin** | Fecha de fin de validez de la configuración |
| **Empresa** | Campo que viene cubierto por defecto con la empresa activa |
| **Inactivo** | Check para marcar si queremos dejar de usar dicha configuración |

## Subpestaña Importes

En esta subpestaña se definen los rangos de importes y los descuentos correspondientes.

### Campos de configuracion

| Campo | Descripción |
|-------|------------|
| **Desde importe** | Importe mínimo donde empezará el rappel (mayor que) |
| **Hasta importe** | Importe máximo hasta donde llegará el rappel (menor o igual) |
| **Descuento** | Descuento en porcentaje aplicado si el volumen está entre el rango |

### Ejemplo de escalas

Una configuración típica podría ser:

| Desde | Hasta | Descuento |
|------|-------|-----------|
| 0 | 1000 | 0% |
| 1000 | 5000 | 2% |
| 5000 | 10000 | 5% |
| 10000 | - | 10% |

## Subpestaña Cliente y Grupo de empresas

En esta subpestaña se definen qué clientes o grupos de empresas aplican esta configuración de rappel.

### Información del cliente

Una vez se selecciona un cliente, se puede ver:
- **Código del cliente**
- **Nombre comercial**
- **Razón social**
- **NIF**

### Asociar clientes

Se pueden asociar:
- **Clientes individuales:** Aplicar la configuración a un cliente específico
- **Grupos de empresas:** Aplicar la configuración a todos los clientes de un grupo

## Aplicacion automatica

Una vez configurados los rappels:

1. **El sistema acumula** automáticamente el volumen de ventas del cliente
2. **Calcula** qué tramo de descuento le corresponde
3. **Genera** la factura de rappel al cerrar el período

## Gestion de multiples configuraciones

Se pueden tener varias configuraciones activas simultáneamente:
- Una por por tipo de cliente
- Una por región o zona
- Una por familia de productos
- Una por período de tiempo

El sistema aplica la configuración correspondiente según el cliente y período.

# Configuracion del Modulo

En este apartado se realiza la configuración general del Módulo de Ventas, incluyendo descuentos, tarifas, rappels y márgenes.

**Ruta de acceso:** `Ventas >> Configuración`

## Secciones de configuracion

El módulo de Ventas se divide en varias áreas de configuración:

### Descuentos

**Referencia:** [Descuentos](./13a-descuentos.md)

Configuración de descuentos generales, por línea y grupos de descuentos:
- Descuentos fijos y variables
- Descuentos por línea y generales
- Grupos de descuentos y combinaciones

### Rappels

**Referencia:** [Rappels](./13b-rappels.md)

Configuración de descuentos por volumen de ventas y bonificaciones:
- Creación de rappels (bonificaciones)
- Configuración de escalas de descuento
- Asociación de clientes a configuraciones

---

## Tarifas

Una tarifa de ventas es el listado estructurado de precios que una empresa establece para sus productos o servicios.

**Ruta específica:** `Ventas >> Configuración >> Tarifas`

### Estados de tarifas

En Elastic, las tarifas se distinguen en dos estados:

- **Vigentes:** Tarifas actualmente en uso
- **Obsoletas:** Tarifas desactivadas

### Estructura del formulario de tarifa

El formulario dispone de dos secciones diferenciadas:

#### Cabecera de la tarifa

| Campo | Descripción |
|-------|------------|
| **Código** | Identificador único de la tarifa (código alfanumérico) |
| **Descripción** | Nombre o detalle explicativo de la tarifa |
| **Fecha de alta** | Fecha en la que se creó la tarifa |
| **Ult. revisión** | Fecha de la última modificación o actualización |
| **Desde** | Fecha de inicio de vigencia de la tarifa |
| **Hasta** | Fecha de fin de vigencia (si aplica) |
| **Moneda** | Moneda en la que se expresan los precios (EUR, USD, etc.) |
| **Conversión** | Factor o método para convertir precios a otra moneda |
| **Tarifa neta** | Indica si los precios son netos (sin impuestos ni descuentos) |
| **Por defecto** | Señala si esta tarifa se aplica por defecto |
| **Obsoleta** | Marca si la tarifa está desactivada |

#### Pestañas de la tarifa

- **Artículos:** Se asignan a la tarifa los artículos a los que serán de aplicación sus condiciones de precio
- **Familias:** Muestra el listado de las familias de los artículos incluidos en la tarifa
- **Clientes:** Permite asociar la tarifa a clientes específicos (si no se asigna ninguno, es general)
- **Grupos de empresas:** Permite vincular la tarifa a uno o varios grupos empresariales
- **Comerciales:** Se pueden asociar los comerciales a los que aplica la tarifa
- **Tarifa paramétrica:** Permite configurar una tarifa basada en parámetros del artículo

### Aplicacion de tarifas

Las tarifas se aplican automáticamente en:
- Presupuestos de venta
- Pedidos
- Albaranes
- Facturas

La tarifa más específica tiene preferencia sobre tarifas generales.

---

## Configuracion Margen

En este acceso se permite configurar diferentes estilos de colores en función de los márgenes.

**Ruta específica:** `Ventas >> Configuración >> Configuración Margen`

### Funcionalidad

Esta herramienta permite:
- **Definir rangos de márgenes** de beneficio
- **Asignar colores** a diferentes tramos
- **Visualizar gráficamente** márgenes en pedidos y presupuestos
- **Establecer alertas visuales** basadas en márgenes configurados

### Visualizacion de márgenes

Los márgenes se pueden visualizar en los documentos de ventas mediante el código de colores establecido:

- Los presupuestos muestran el margen estimado
- Los pedidos reflejan el margen negociado
- Los albaranes y facturas muestran el margen final

### Control de márgenes

La configuración de márgenes permite:
- **Identificar rápidamente** operaciones con márgenes muy bajos
- **Asegurar rentabilidad** mínima en ventas
- **Alertar comerciales** sobre márgenes críticos
- **Gestionar políticas** de precios

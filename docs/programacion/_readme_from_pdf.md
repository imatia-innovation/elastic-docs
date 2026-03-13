# PROGRAMACION - Contenido extraído de PDF

> **Nota:** Esta es una extracción automática de PDF a Markdown. 
> Requiere revisión y reorganización manual según estructura deseada.

**Estadísticas:**
- Páginas procesadas: 20
- Tamaño del contenido: 19808 caracteres

## Contenido extraído

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 1 / 11 
www.imatia.com  
2.1 
Tabla de artículos/productos y familias  
................................
 .. 
2 
2.2 
Tabla de costes  
................................
 ......  
2 
2.3 
Tabla de stocks  
................................
 ......  
3 
2.4 
Diagrama de tablas de almacén, artículos y parámetros  
................................
 ........  
4 
3.1 
Tablas de componentes/materiales  
................................
 ........  
5 
3.2 
Tabla de operaciones de un artículo  
................................
 ......  
6 
4.1 
Tablas de tarifas/precios de los artículos  
................................
 ...............................  
7 
4.2 
Tabla de clientes  
................................
 .... 
8 
4.3 
Tabla de pedidos de ventas y líneas del pedido  
................................
 ....................  
8 
4.4 
Diagrama de ventas (presupuestos, pedidos, albaranes, facturas)  
........................  
9

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 1 / 9 
www.imatia.com  
3.1 
Modo “Desarrollador”  
................................
 .............................  
3 
3.1.1  
Configurar usuario en modo “Desarrollador”  
................................
 ..................  
3 
3.2 
Características  
................................
 ........  
4 
3.2.1  
Poder ver qué entidad, tabla y/o vista de base de datos usa un determinado 
formulario o tabla para consultar los datos.  
................................
 .............................  
5 
3.2.2  
Ver claves de una fila seleccionada.  
................................
 ...............................  
5 
3.2.3  
Ver claves del formulario.  
................................
 ...............  
6 
3.2.4  
Ver el nombre y valor que tiene un campo en base de datos.  
......................  
7 
4.1 
Activar la Consola Java  
................................
 ...........................  
8

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 2 / 11 
www.imatia.com  
A continuación, se detallan algunas de las principales tablas/vistas de la base de datos 
de Elastic Business.  
 
- 
Nombre de la tabla de artículos: 
 ALM_MAESTRO_ARTICULOS
 . 
 Vista 
ALM_VISTA_MAESTRO_ARTICULOS
 . 
Columnas  
principales:  
o 
ID_ARTICULO
 : identificador, clave primaria  
o 
CODIGO_INTERNO
 : 
código del artículo  
o 
DESC_ARTICULO
 : 
descripción del artículo  
o 
ean13  
o 
ean14  
- 
Nombre de la tabla de familias: 
 ALM_FAMILIAS_ARTICULOS
 . 
Columnas  
principales:  
o 
ID_FAMILIA
 : identificador, clave primaria  
o 
COD_FAMILIA
 : 
código de la familia  
o 
DESC_FAMILIA: 
 descripción de la familia  
- 
Relación artículos
 -
familias:  
o 
ALM_FAMILIAS_ARTICULOS.ID_FAMILIA  
o 
ALM_MAESTRO_ARTICULOS.ID_FAMILIA  
 
- 
Tabla de costes de los artículos: 
 alm_item_costs
 . 
Vista 
 valm_item_costs
 . 
- 
Relación costes
 -
articulos:  
SELECT  
  
ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO AS 'Codigo'  
  
,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO AS 'Descripcion'  
  
,ALM_MAESTRO_ARTICULOS.ean13  
  
,ALM_MAESTRO_ARTICULOS.ean14  
  
,ALM_FAMILIAS_ARTICULOS.COD_FAMILIA  
  
,ALM_FAMILIAS_ARTICULOS.DESC_FAMILIA AS 'Familia'  
FROM ALM_MAESTRO_ARTICULOS  
JOIN ALM_FAMILIAS_ARTICULOS ON ALM_FAMILIAS_ARTICULOS.ID_FAMILIA = ALM_MAESTRO_ARTICULOS.ID_FAMILIA

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 2 / 9 
www.imatia.com  
En este manual se detalla como configurar un usuario en modo “Desarrollador” y como 
obtener información de la base de datos. Se explican qué características tiene el modo 
desarrollador y cómo es posible obtener información del esquema de la base de datos.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 3 / 11 
www.imatia.com  
 
La table de stocks identifica cu
 al es el stock de un artículo para una empresa y en qué 
localización (almacén
 -
subalmacén
 -
ubicación). El stock total de un artículo es la suma de 
los stocks de las distintas localizaciones de la tabla de stocks del artículo.  
 
- 
Tabla de almacenes: 
 ALM_DEFINICION_ALMACENES
 . 
- 
Tabla de subalmacenes: 
 ALM_DEFINICION_SUBALMACENES  
- 
Tabla de ubicaciones: 
 ALM_DEFINICION_UBICACIONES  
- 
Tabla de stocks de l
 os artículos: 
 ALM_ARTICULOS_ALMACEN
 . Vista 
ALM_VISTA_STOCK_ALMACEN_DETALLADO  
o 
ID_ARTICULO_ALMACEN
 : clave primaria/identificador  
o 
STOCK_FISICO
 : stock  
 
select  
 
 alm_item_costs.item_cost_id  
 
 ,ALM_MAESTRO_ARTICULOS.ID_ARTICULO  
  
 ,ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO AS 'Codigo'  
  
 ,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO AS 'Descripcion'  
 
 ,PROD_ARTICULOS.ID_VERSION  
 
 ,PROD_VERSIONES.DESC_VERSION as 'Version'  
 
 ,alm_item_costs.raw_material_cost as 'Coste materia prima'  
 
 ,alm_item_costs.active 'Coste activo'  
 
 ,alm_cost_models.cost_model_description as 'Modelo de costes'  
from alm_item_costs  
join PROD_ARTICULOS on PROD_ARTICULOS.ID_ARTICULO = alm_item_costs.item_id  
join PROD_VERSIONES on PROD_VERSIONES.ID_VERSION = PROD_ARTICULOS.ID_VERSION  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = PROD_ARTICULOS.ID_ARTICULO  
left join alm_cost_models on alm_cost_models.cost_model_id = alm_cost_models.cost_model_id

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 3 / 9 
www.imatia.com  
Para crear un usuario debemos dirigirnos en la aplicación de Elastic Business a 
“Administración >> Usuarios “. Desde esta pantalla se muestran los usuarios existentes 
en una lista situada a la izquierda. Para crear un nuevo usuario debemos pinchar sobre 
el 
icono de “Limpiar campos” y a continuación pinchar sobre el icono de “Insertar”.  
 
Ahora la pantalla se mostrará en modo inserción y podremos indicar los datos del nuevo 
usuario.  
 
Para ver los perfiles de usuario existentes debemos dirigirnos a “Gestión módulos” >> 
Perfiles”. Desde aquí podremos ver, crear y modificar los distintos perfiles de usuario de 
la aplicación.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 4 / 11 
www.imatia.com  
 
select  
ALM_ARTICULOS_ALMACEN.ID_ARTICULO_ALMACEN  
,EMPRESAS.NOMBRE_EMPRESA as 'Empresa'  
,ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO as 'Codigo'  
,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO as 'Descripcion'  
,ALM_DEFINICION_ALMACENES.DESC_ALMACEN as 'Almacen'  
,ALM_DEFINICION_SUBALMACENES.DESC_SUBALMACEN as 'Subalmacen'  
,ALM_DEFINICION_UBICACIONES.COD_UBICACION as 'Ubicacion'  
,ALM_ARTICULOS_ALMACEN.STOCK_FISICO as 'Stock'  
from ALM_ARTICULOS_ALMACEN  
join EMPRESAS on EMPRESAS.ID_EMPRESA = ALM_ARTICULOS_ALMACEN.ID_EMPRESA  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = ALM_ARTICULOS_ALMACEN.ID_ARTICULO  
left join ALM_DEFINICION_ALMACENES on ALM_DEFINICION_ALMACENES.ID_ALMACEN = 
ALM_ARTICULOS_ALMACEN.ID_ALMACEN  
left join ALM_DEFINICION_SUBALMACENES on ALM_DEFINICION_SUBALMACENES.ID_SUBALMACEN = 
ALM_ARTICULOS_ALMACEN.ID_SUBALMACEN  
left join ALM_DEFINICION_UBICACIONES on ALM_DEFINICION_UBICACIONES.ID_UBICACION = 
ALM_ARTICULOS_ALMACEN.ID_UBICACION

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 4 / 9 
www.imatia.com  
Para configurar un usuario en modo desarrollador hay que asignarle un perfil que tenga 
marcado el check “Desarrollador”.  
 
Para asignarle el perfil a un usuario debemos seleccionar el usuario correspondiente y 
asignarle el perfil indicado.  
 
Si estamos conectados en la aplicación de Elastic Business con usuario configurado con 
un perfil de desarrollador tenemos algunas funcionalidades extras que otros usuarios no 
tienen. Se explican a continuación algunas de funcionalidades extras:

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 5 / 11 
www.imatia.com  
 
La configuración de los artículos de producción y componentes se realiza desglosando 
los artículos/familias en función de sus versiones. Una familia puede tener una o varias 
versiones y en cada una de esas versiones se asignan artículos. Por ejemplo, si un
 a familia 
tiene 2 versiones, un artículo de esa familia puede estar en una de esas versiones o en 
ambas.  
Respecto a los componentes que forman un artículo, estos también se configuran por 
artículo
 -
versión. Por ejemplo, en el caso anterior de que la familia de un artículo tenga 
2 versiones. La versión 1 del artículo tendrán una configuración de componentes dis
 tinta 
a la versión 2 del artículo.  
La relación entre artículos y sus componentes (que también son artículos) se realiza a 
través de la versión de cada artículo  
- 
Tabla de versiones: 
 PROD_VERSIONES  
o 
ID_VERSION
 : clave primaria

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 5 / 9 
www.imatia.com  
 
Pulsando con el botón derecho del ratón sobre el título de un formulario o sobre el 
contenido de una tabla, si seleccionamos “Ver información entidad asociada” nos 
muestra en el título del formulario el nombre de la entidad, tabla y vista.  
 
Seleccionando una o varias filas de una tabla y pulsando con el botón derecho del ratón 
se muestra una ventana con varias opciones, si seleccionamos “Ver clave de las filas 
seleccionadas” nos muestra las claves y sus valores de base de datos.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 6 / 11 
www.imatia.com  - 
Tabla de versiones de artículos: 
 PROD_ARTICULOS  
o 
ID_VERSION_ARTICULO
 : clave primaria  
- 
Tabla de componentes: 
 PROD_COMPOSICIONES  
o 
ID_COMPOSICION: 
 clave primaria  
o 
VER_ARTICULO_HIJO
 : identificador de la versión del componente  
o 
VER_ARTICULO_PADRE
 : identificador de la versión del artículo “padre”  
 
- 
Tabla de operaciones de la versión de un artículo: 
PROD_OPERACIONES_ARTICULOS  
o 
ID_OPERACION_ARTICULO
 : clave primaria  
- 
Tabla de operaciones: 
 PROD_OPERACIONES  
o 
ID_OPERACION
 : clave primaria  
o 
DESC_OPERACION
 : descripción de la operación  
 
SELECT  
ALM_MAESTRO_ARTICULOS.ID_ARTICULO  
,ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO as 'Codigo'  
,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO as 'Descripcion'  
,PROD_VERSIONES.DESC_VERSION as 'Version'  
,componentes.CODIGO_INTERNO as 'Codigo del componente'  
,componentes.DESC_ARTICULO as 'Descripcion del componente'  
,PROD_COMPOSICIONES.CANTIDAD  
from PROD_ARTICULOS  
join  
 PROD_COMPOSICIONES on PROD_COMPOSICIONES.VER_ARTICULO_PADRE = 
PROD_ARTICULOS.ID_VERSION_ARTICULO  
join PROD_VERSIONES on PROD_VERSIONES.ID_VERSION = PROD_ARTICULOS.ID_VERSION  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = PROD_ARTICULOS.ID_ARTICULO  
join PROD_ARTICULOS as version_componentes on version_componentes.ID_VERSION_ARTICULO = 
PROD_COMPOSICIONES.VER_ARTICULO_HIJO  
join ALM_MAESTRO_ARTICULOS as componentes on componentes.ID_ARTICULO = version_componentes.ID_ARTICULO

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 6 / 9 
www.imatia.com  
 
Pulsando con el botón derecho del ratón sobre el título de un formulario y seleccionando 
“Ver claves del formulario” nos muestra las claves y sus valores de base de datos para 
ese formulario.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 7 / 11 
www.imatia.com  
 
- 
Tabla de tarifas: 
 COM_TARIFAS  
o 
COD_TARIFA
 : clave primaria  
- 
Tabla de precios de tarifas
 -
artículos: 
 COM_TARIFAS_ARTICULOS  
o 
PRECIO_BASE_PVP
 : precio del artículo  
 
SELECT  
PROD_OPERACIONES_ARTICULOS.ID_OPERACION_ARTICULO  
,PROD_OPERACIONES.ID_OPERACION  
,PROD_OPERACIONES.DESC_OPERACION  
,PROD_ARTICULOS.ID_VERSION_ARTICULO  
,ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO  
,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO  
from PROD_OPERACIONES_ARTICULOS  
join PROD_OPERACIONES on PROD_OPERACIONES.ID_OPERACION = PROD_OPERACIONES_ARTICULOS.ID_OPERACION  
join  
 PROD_ARTICULOS on PROD_ARTICULOS.ID_VERSION_ARTICULO = 
PROD_OPERACIONES_ARTICULOS.ID_VERSION_ARTICULO  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = PROD_ARTICULOS.ID_ARTICULO  
SELECT  
COM_TARIFAS.COD_TARIFA  
,COM_TARIFAS.DESC_TARIFA  
,ALM_MAESTRO_ARTICULOS.CODIGO_INTERNO  
,ALM_MAESTRO_ARTICULOS.DESC_ARTICULO  
,COM_TARIFAS_ARTICULOS.PRECIO_BASE_PVP  
from COM_TARIFAS  
join COM_TARIFAS_ARTICULOS on COM_TARIFAS_ARTICULOS.COD_TARIFA = COM_TARIFAS.COD_TARIFA  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = COM_TARIFAS_ARTICULOS.ID_ARTICULO

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 7 / 9 
www.imatia.com  
 
Pulsando las teclas ALT + SHIFT + CTRL y pinchando con el botón izquierdo del ratón 
sobre un campo se muestra  
un aviso indicando  
el nombre y valor de ese campo en base 
de datos.  
 
Si la aplicación de Elastic se ha ejecutado con Java abriendo el fichero APPLICATION.jnlp. 
Entonces, en la consola de Java se muestra información del campo.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 8 / 11 
www.imatia.com  
 
- 
Tabla de clientes: 
 sales_customers  
o 
customer_id
 : clave primaria/identificado
 r 
 
- 
Tabla de pedidos de ventas: 
 sales_orders  
o 
order_id
 : identificador/clave  
- 
Tabla de líneas del pedido de ventas: 
 sales_order_details  
o 
order_detail_id
 : identificador  
o 
order_id
 : identificador del pedido  
o 
item_id
 : identificador del articulo  
 
select  
sales_customers.customer_id  
,sales_customers.customer_company_name  
,sales_customers.customer_trade_name  
,sales_
 customers.customer_cif_nif  
from sales_customers

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 8 / 9 
www.imatia.com  
 
El log del cliente se muestra en la Consola Java. Es una ventana en donde se muestra 
texto plano que registra información que va ocurriendo.  
 
Para activar la Consola de Java debemos abrir el panel de configuración de Java. Para 
ello, escribimos en el buscador de Windows la palabra “java” y seleccionamos la 
aplicación “Configurar Java”.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 9 / 11 
www.imatia.com  
 
select  
sales_orders.order_id  
,sales_orders.order_code as 'Numero pedido'  
,sales_orders.document_date as 'Fecha pedido'  
,sales_customers.customer_company_name  
as 'Razón social'  
,sales_orders.total_tax_base 'Base del pedido'  
,sales_orders.total_amount as 'Importe total del pedido'  
,sales_order_details.item_code as 'Codigo'  
,sales_order_details.item_description as 'Descripcion'  
,ALM_MAESTRO_ARTICULOS.ean13  
,sales_order_details.unit_price as 'Precio unitario'  
,sales_order_details.real_quantity as 'Cantidad real de la linea'  
,sales_order_details.taxable_amount as 'Base de la linea'  
,sales_order_details.total_amount as 'Importe total de la linea'  
from sales_orders  
join sales_customers on sales_customers.customer_id = sales_orders.customer_id  
left join sales_order_details on sales_order_details.order_id = sales_orders.order_id  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = sales_order_details.item_id

---

# Elastic_Business_Manual_obtener_información_BBDD  - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_obtener_información_BBDD .pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business©  
Bases de datos  
| 
2026  
 9 / 9 
www.imatia.com  
 
Una vez dentro del Panel de Control de Java, nos dirigimos a la pestaña de “Avanzado” 
y seleccionamos la opción “Ver consola”.

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 10 / 11 
www.imatia.com  
 
- 
Tabla de RMAs: 
 cal_rma  
o 
rma_id
 : identificador  
o 
rma_status
 : identificador del estado  
o 
rma_customer_id
 : identificador del cliente  
- 
Tabla de estados de RMAs: 
 cal_rma_
 status_config  
o 
rma_status_id
 : clave  
o 
status_description
 : descripción del estado

---

# Elastic_Business_Manual_explicación_tablas_BBDD - 

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion



## Texto extraído

Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 11 / 11 
www.imatia.com  
 
- 
Tablas de subcuentas: 
 ECOFIN_SUBCUENTAS  
- 
Tabla de asientos contables: 
 ECOFIN_ASIENTOS  
- 
Tablas de partidas contables: 
 ECOFIN_PARTIDAS  
select  
cal_rma.rma_id  
,cal_rma.rma_code  
,cal_rma_status_config.status_description  
,sales_customers.customer_company_name  
from cal_rma  
left join cal_rma_status_config on cal_rma_status_config.rma_status_id = cal_rma.rma_status  
left join sales_customers on sales_customers.customer_id = rma_customer_id

---

## Próximos pasos

1. ✓ Revisar y corriegir el texto
2. ⏳ Reorganizar en secciones temáticas
3. ⏳ Extraer tablas y formatear correctamente
4. ⏳ Agregar imágenes desde `docs/assets/pdf-images/programacion/`
5. ⏳ Crear estructura final con archivos temáticos
6. ⏳ Actualizar tabla de contenidos

## Módulo: programacion

**PDF original:** `build/sources/programacion/`
**Raw files:** `docs/_raw/programacion/`
**Assets:** `docs/assets/pdf-images/programacion/`

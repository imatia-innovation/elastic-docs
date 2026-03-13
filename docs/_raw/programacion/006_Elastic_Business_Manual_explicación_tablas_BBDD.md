# Elastic_Business_Manual_explicación_tablas_BBDD - Página 6

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

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


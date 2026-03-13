# Elastic_Business_Manual_explicación_tablas_BBDD - Página 2

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

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


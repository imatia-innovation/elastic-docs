# Elastic_Business_Manual_explicación_tablas_BBDD - Página 3

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

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


# Elastic_Business_Manual_explicación_tablas_BBDD - Página 5

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

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



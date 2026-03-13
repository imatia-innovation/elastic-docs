# 161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0 - Página 43

**Origen:** `build\sources\guia_de_uso\161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0.pdf`
**Módulo:** guia_de_uso

---

## Texto extraído

  
 
 
 
· 43 · 
 
www. elastic -business .com  
 
 
Guía rápida de iniciación  Configuración y parametrización  
▪ Contador Facturas abono normales -> FacturaSerie02  
▪ Contador Facturas atípicas -> FacturaSerie03  
▪ Contador Facturas abono atípicas -> FacturaSerie04  
▪ Contador Facturas mantenimiento -> FacturaSerie05  
▪ Contador Facturas abono mantenimiento -> FacturaSerie06  
 
2. Crear las series de facturas en la tabla maestras VENTAS. Series de facturas. 
Configuración. Siguiendo los pasos indicados, debería quedar configurado algo 
similar a lo que se muestra a continuación:  
 
Cód. serie  Descripción serie  Acrónimo  
F Serie normal  F 
AF Serie abono normal  AF 
A Serie atípica  A 
AA Serie abono atípica  A 
M Serie mantenimiento  AM 
AM Serie abono mantenimiento  AM 
 
3. Una vez has creado las series de facturas, Tienes que asociarlas a cada uno de sus 
contadores. Esto tienes que hacerlo indicado en cada serie, en el campo Entidad del 
contador de la tabla, cual es la entidad del contador que le corresponde, es decir 
FACTUR AS_SERIE_01, FACTURAS_SERIE_02, FACTURAS_SERIE_03,… de modo que la 
tabla quede, p.e.:  
 
 
 
 
 
 
 
Cód.  Descripción serie  Por def  Prefijo  Entidad del 
contador  Acrónimo  
F Serie normal  Sí Sí FACTURAS_SERIE_01  F 
AF Serie abono normal  No Sí FACTURAS_SERIE_02  AF 


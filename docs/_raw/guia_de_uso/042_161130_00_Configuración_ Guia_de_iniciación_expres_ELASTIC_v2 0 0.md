# 161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0 - Página 42

**Origen:** `build\sources\guia_de_uso\161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0.pdf`
**Módulo:** guia_de_uso

---

## Texto extraído

  
 
 
 
· 42 · 
 
www. elastic -business .com  
 
 
Guía rápida de iniciación  Configuración y parametrización  
▪ Los configurables.  La aplicación dispone de un configurador de contadores 
personalizado, donde el cliente puede además de números asociar prefijos 
y sufijos alfanuméricos para cada empresa y cada entidad (facturas, 
pedidos, clientes, albaranes,…)  
Para acceder a los contadores configurables:  
 
Menú Aplicación >>> Configuración >>> Configuración contadores >>> Crear contador >> 
Definirlo >>> Botón  Insertar (F9).  
 
VER VIDEO. Como crear y configurar un contador personalizado.  
 
 Nota: La aplicación detecta tanto si en el prefijo como del sufijo es numérico, por tanto 
en este caso, si se marca como reseteable el contador, automáticamente, se incrementará 
una unidad al llegar a la fecha de reseteo. Esto permite añadir el año en el prefijo o en el 
sufijo y este se actualizará automáticamente. Cada año que pase se creará una línea en la 
tabla Estado contador, por si fuese necesario editar el valor el contador.  
 Nota: La configuración de contadores de facturas de venta es un poco particular ya que 
además del contador se deben configurar las series de facturas.   
Crear contadores para series de facturas  
En caso de que la empresa usuario no trabaje con series de facturas, es decir, que todas 
sean de la misma tipología bastará con configurar un solo contador  que tendrá marcad o la 
entidad Facturas, en la tabla Entidades del formulario de configuración de contadores.  
En caso de que la empresa si desee trabajar con diferentes series de facturas, es 
importante tener en cuenta que la aplicación permite configurar hasta un máximo de 10 
series distintas. Además de crear cada uno de los contadores de las series, se tendrá qu e 
crear dichas series en la tabla maestra VENTAS. Series de facturas. Configuración y asociar 
cada serie a cada contador. El proceso que se tiene que seguir es el  siguiente:  
 
1. Crear un contador como en el punto anterior, pero a este se le asociará la entidad 
FacturaSerie01, FacturaSerie02,…  Un ejemplo de series de facturas sería: facturas 
normales, normales de abono, atípicas, atípicas de abono, de mantenimiento y de 
abono de mantenimiento. Se tiene, por tanto, que crear un contador para cada una 
de las series y asociarle una de las 10 entida des disponibles para las series de 
facturas, p.e:  
 
▪ Contador Facturas normales -> FacturaSerie01  


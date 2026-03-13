# Elastic_Business_Módulo de almacén - Página 11

**Origen:** `build\sources\almacen\Elastic_Business_Módulo de almacén.pdf`
**Módulo:** almacen

---

## Texto extraído

 
Manual de Usuario Módulo de Almacén  
   
 
 
elastic® B USINESS   Pág. 11 de 61 
 
 Sub. Salida  Subalmacén por defecto al que irán los artículos 
cuando vayan a salir del almacén , si el campo 
almacén tiene un subalmacén  configurado . 
Observaciones  Comentarios que se pueden guardar sobre una familia  CONFIGURACIÓN  
Código  Aquí se selecciona como se generarán los artículos 
que configuremos para la familia.  (identificador, 
código interno, contados, con tador configurable)  
Un. medida  Unidad de medida que tendrán por defecto los 
artículos  
 
 
 
En esta  se configuran los aspectos principales por los que se debe regir cada familia.  
Uno de los más importantes, es marcar si la familia es de servicios o no, entendiéndose como "De 
servicios" todas aquellas familias que no generan movimientos contra el almacén (por lo que la opción 
obligatoria de marcar almacén se desactiva).  
Las familias solamente se crean para tres ámbitos: ventas, compras y producción, por lo que se debe 
marcar a cuál o cuáles pertenece, pudiendo ser los tres. El uso principal de marcar el ámbito es filtrar la 
información cuando usas el correspondiente módul o, de forma que ves solo las familias necesarias.   
 
 
A la hora de crear y configurar la familia es muy importante decidir si el código se va a generar por 
parámetros o no. Únicamente se debe marca la opción "sin parámetros" en el caso de que se esté 
completamente seguro de que la familia ni lleva, ni llevará  en el futuro parámetros, si no se debe 
marcar  "Código por parámetros"  aunque no se configuren. Esto permitirá en un futuro parametrizar las 
familias reutilizando los artículos existentes y no perder los históricos de información.   
*Nota:  Si una familia se crea sin parámetros, pero se decide más adelante que sí debe llevar, hay que 
darla de baja y volver a crearla, ya que es una acción irreversible.  
*Nota:  La propia familia es un parámetro, lo que permite que, en el caso de haber dudas, (p.ej., en una 
implantación) en la que se sabe que los parámetros se van a usar, pero no en ese momento, el sistema 



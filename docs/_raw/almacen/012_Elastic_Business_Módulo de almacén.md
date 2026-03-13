# Elastic_Business_Módulo de almacén - Página 12

**Origen:** `build\sources\almacen\Elastic_Business_Módulo de almacén.pdf`
**Módulo:** almacen

---

## Texto extraído

 
Manual de Usuario Módulo de Almacén  
   
 
 
elastic® B USINESS   Pág. 12 de 61 
 
 la usa como parámetros y en "regenerar código y descripción", permite meter parámetros, aunque la 
familia se haya creado.  
 
El código del artículo se genera por los valores de los parámetros. Si se crea una familia por parámetros, 
no se crea un contador por lo que se desactivan los campos.  
Hay tres formas de crear el código del artículo:  
• Identificador:  el código es asignado por el usuario.  
• Código interno:  es el sistema el que le da un código a los artículos.  
• Contador:  es el sistema el que da los códigos, pero siguiendo la configuración del contador 
definido en  Aplicación >> Configuración >> Configuración de contadores.   
• Contador configurable:  se configuran contadores personalizados para cada familia para generar 
los artículos dentro de la familia si estos no se van a crear por parámetro, sino que serán 
artículos de código y descripción asignadas por el usuario. Se activan los campos de prefijo , 
sufijo y longitud, para que el usuario edite el contador.   
*Nota:  En el campo  "Valor"  se indica el próximo valor con el que se quiere que comience a dar de alta.  
Otro aspecto a tener en cuenta es la unidad o unidades con las que trabajarán los artículos de una familia. 
Este aspecto también determina la homogeneidad del grupo creado y si este tiene más de una unidad. 
En el campo obligatorio, "Un.  medida" se indica la unidad principal de la familia. Seleccionando "Propagar 
unidades" se consigue que cuando se añade un artículo nuevo, automáticamente se le asigna la unidad 
principal. Si no se selecciona, el usuario deberá seleccionar la unidad corresp ondiente manualment e. 
También se usa si se trabaja un mismo artículo,  pero en varias unidades.  
Si la familia es trazable se marca la casilla de  "Trazable" . Que la familia se marque como trazable implica 
que todos y cada uno de los artículos que la forman son trazables. Si alguno no lo fuese, la familia se 
considera  "No trazable"  y es dentro del propio artículo donde se marca que ese sí lo es.  La configuración 
de la trazabilidad se hará mediante Lote, Lote producto o Nº de serie.  
Si el usuario quiere que no se controlen los stocks de los artículos de una familia, debe seleccionar la 
opción de "Familia ficticia". Esta opción vincula la familia con producción por lo que, si se activa esta 
opción solo es posible que el ámbito seleccio nado sea el de producción.  
 
 
En esta pestaña vamos a ver como añadir artículos a la familia , tanto de forma paramétrica como de 
forma  genérica.   
 
Para crear un nuevo artículo tenemos que añadir un registro  y esto nos desplegará un a ventana. E sta 
ventana podemos verla de dos maneras diferentes  si la familia es paramétrica o no.  
El check de  Tarificado aparece marcado cuando le ponemos un precio o cuando asignamos una tarifa.  
Respecto a los artículos, lo hablaremos con más detalle en su correspondiente apartado.  
*Nota:  No puede existir un artículo si no pertenece a una familia.  



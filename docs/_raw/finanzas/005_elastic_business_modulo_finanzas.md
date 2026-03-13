# elastic_business_modulo_finanzas - Página 5

**Origen:** `docs\assets\source-pdfs\finanzas\elastic_business_modulo_finanzas.pdf`
**Módulo:** finanzas

---

## Texto extraído

 
 
 
 
 
 
 
 
 
Pág. 5/38 www.imatia.com   
Configuración de subcuentas  
La configuración de subcuenta puede estar complementada por la división. Esta configuración 
ampliada, permite a las empresas relacionar de manera automática la subcuenta con un centro de 
coste, siendo este el departamento o división. Este último pueda esta r asignado previamente a 
las facturas de venta  o facturas de compras  mediante el campo división, pudiendo así tener un grado 
más en el control de la distribución automática a través de la división asignada a la factura. Lo normal 
es que el porcentaje de distribución sea el 100% al valor que coincida con el de la propia div isión, pero 
el sistema es flexible porque  lo que permite hacer distribuciones porcentuales a los distintos valores de 
la dimensión independientemente de la división asociada.    
Nota:  En caso de que se quiera dejar de utilizar un valor de la dimensión, se puede dar de baja. Si ya ha sido 
utilizada no puede borrarse por integridad de datos.  
Nota:  Cuando se inserta valor en el porcentaje, el sistema sabe que esa es la parte del importe que debe llevar al 
valor de la dimensión cuando parece esa subcuenta en juego en los asientos. Automáticamente el check de visible 
parece marcado. Por el contrario, si se piensa en hacer una distribución manual entre ciertos valores fuera del 
estándar y según lo que quiera hacer el  usuario , se puede marcar el check de visible. Eso hará que, a pesar de no 
ponerle distribución porcentual, se visualizará el valor para asignarle manualmente porcentaje de importe en el 
asiento. Es un tema ergonómico.   
Nota:  El sistema de dimensiones es compatible con la inserción manual de asientos, los que se meten 
directamente desde  finanzas . Cada vez que se añade una partida al asiento comprueba si esa subcuenta está  
definida en alguna configuración y realiza la distribución igualmente.  Esto puede valer para cuentas de dotación, 
sueldos, etc. de las que nos e inserta factura.   
 
A la hora de contabilizar en una factura una subcuenta que tenga configurad a una dimensión con 
diferentes valores, automáticamente el sistema  hará el reparto dimensional.  



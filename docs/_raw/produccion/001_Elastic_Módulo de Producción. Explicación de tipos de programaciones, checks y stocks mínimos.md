# Elastic_Módulo de Producción. Explicación de tipos de programaciones, checks y stocks mínimos - Página 1

**Origen:** `build\sources\produccion\Elastic_Módulo de Producción. Explicación de tipos de programaciones, checks y stocks mínimos.pdf`
**Módulo:** produccion

---

## Texto extraído

 
 
 
 
 
 
 
 
 
Pág. 1/2 www.imatia.com   
 
Plan maestro:  A raíz de lo que esté añadido en la pestaña de Pedidos y Detalles de pedidos, se añadirán 
los artículos correspondientes en la pestaña de Plan Maestro, a raíz de estos el sistema calcula las 
necesidades.  
Necesidades parciales:  Este botón se utiliza para calcular únicamente las necesidades de ciertas 
familias, para ello se necesita una configuración previa indicando que solamente se quieren calcular 
necesidades de estas familias.  
Necesidades:  Calcula las necesidades (materiales) para la fabricación de los artículos que se encuentra 
en la pestaña de Plan Maestro.  
Plan Maestro + Necesidades:  Combinación de la primera opción y la segunda, se suele utilizar una vez 
se añadan los pedidos o detalles de pedidos a la programación.  
 
 
Previsión:  Este check hace que no aparezca en el listado de necesidades de compra . 
Ignorar stock : Si se marca este check , al añadir un artículo  al plan maestro, no tiene en cuenta las 
unidade s del almacén. El cálculo  de necesidades se realiza ignorando lo que hay en el almacén . (Ejemplo : 
si tenemos 50 unidades en stock y necesitamos 100, no tendrá en cuentas el stock del articulo y nos 
fabricará 100 ). 
Ignorar necesidades de stock : Al tener este check activado, el cálculo de necesidades no realizará un 
barrido en el almacén comprobando que artículos tengan un stock mínimo configurado . 
Preparad a: Si se marca este check, lo que hace es meterla en una cola en la que se van generando las 
necesidades y plan maestro automáticamente.  
Programación diaria : Si se marca este che ck, se c rea una programación  de forma diaria  donde meterá 
todas las órdenes.  
Reservar al generar : Al tener marcado el check, c uando se genere la programación , se reserva 
automáticamente el material para esta . 
Orden por operación : Al tener marcado el check, s e generará una orden por cada operación que 
tengamos en nuestros despieces y se incluirán en ella todos los artículos afectados por esa operación.  
Orden por línea:  Al tener marcado el check, s e generará una orden diferente por cada detalle de pedido 
que incluyamos en nuestra programación . 


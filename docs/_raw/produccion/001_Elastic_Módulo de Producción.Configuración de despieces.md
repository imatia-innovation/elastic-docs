# Elastic_Módulo de Producción.Configuración de despieces - Página 1

**Origen:** `build\sources\produccion\Elastic_Módulo de Producción.Configuración de despieces.pdf`
**Módulo:** produccion

---

## Texto extraído

 
 
 
 
 
 
 
 
 
Pág. 1/5 www.imatia.com   
En el presente documento se va a detallar el funcionamiento de los despieces  en Elastic, así como su 
configuración . 
 
 
En Elastic las familias de artículos se pueden diferenciar por su tipologiá, estas pueden ser de ventas, 
compras, producción o servicios. Una misma familia puede ser de varios tipos a la vez. En el caso de las 
familias de artículos que se van a utilizar en  producción, hay que especificar su comportamiento 
mediante los siguientes checks, estos se encuentran en Almacén >> Familias de artículos, dentro de una 
de ellas pestaña de Producción.  
• Planificab le: debe estar marcado si los artículos se van a fabricar , tanto bajo pedido como por 
stock . Permite que sean seleccionables en el Plan Maestro.  
• En programación:  debe estar marcado para que los artículos de esta familia se tengan en cuenta 
para el cálculo de necesidades, independientemente que estos sean materiales de otros 
artículos o son artículos que se fabrican propiamente.   
A mayores se distinguen los siguientes checks:  
• Ignorar stock:  cuando se calculan las necesidades se tiene siempre en cuenta el stock. Si lo que 
se quiere es que no se tenga en cuenta el mismo y se calculen las necesidades dando como 
resultado una compra o fabricación, se debe marcar esta casilla.   
• Necesidades parciales:  se selecciona para evitar que, al calcular las necesidades, se calcule de 
todo el material que compone el artículo a fabricar. De esta manera se permite reducir el cálculo 
de necesidades únicamente a las familias que se necesite.  
En Elastic se define dos niveles de versiones de despiece.  
Dentro de una familia existe n n versiones de despiece s, y dentro de esta, cada artículo puede tener 
únicamente una versi ón de despiece. Es decir,  para que un artículo tenga varias versiones de despieces, 
es necesario  que la familia tenga ese mismo número de versiones de despieces.  
Para crear una nueva versión de despiece para una familia esto se hace desde la pestaña de Producción, 
en Almacén >> Familias de artículos, al seleccionar una familia.  
 
 
Para configurar el despiece de un artículo, debemos ir a la siguiente ruta.  
Almacén >> Familias de artículo >> Artículo >> Producción.  
Dentro de la configuración del despiece del artículo se diferencia entra la cabecera y las pestañas 
inferiores.  


# elastic_business_modulo_ventas - Página 63

**Origen:** `docs\assets\source-pdfs\ventas\elastic_business_modulo_ventas.pdf`
**Módulo:** ventas

---

## Texto extraído

 
Manual de Usuario Módulo de Ventas  
   
 
 
elastic® B USINESS   Pág. 63 de 84 
 
  
El SII hace referencia a la obligación, por parte de las empresas que cumplen con las condiciones 
establecidas por parte de la Hacienda Pública, de enviar sistemáticamente la información sobre las 
operaciones comerciales de venta / compra, registrada media nte factura. Esto viene a sustituir a medio 
plazo, la necesidad de enviar cierta información contable mediante los modelos actuales, tal y como se 
venía haciendo hasta la fecha.  
Para facilitar dicha operación, elastic© BUSINESS incorpora una serie de funcionalidades que ayudan al 
envío de los ficheros correspondientes generados a partir en este caso de facturas  (venta y compra ) y 
pagos, y la posterior comprobación de que todo está correcto. Hacienda devuelve información para 
verificar que todo está bien.  
Para utilizar dicha funcionalidad:  
• En la aplicación,  tenemos que ir a Laboral >> Empresas >> Certificados  y añadir mediante el 
botón adjuntar, el certificado digital emitido por la FMNT u otros organismos autorizados. En 
principio solo se acepta certificado con extensión " .pf2". El formato ".pfx no es válido, pero se 
puede reconvertir.  
• El sistema nunca pedirá la clave del certificado digital. Dicha clave será solicitada cada vez que 
se genere un fichero desde la parte de ventas y ventas  para su envío al portal de Hacienda.   
*Nota:  Aunque es un tema que compete a la empresa, lo recomendable es que las personas que vayan 
a utilizar este sistema tengan un certificado digital propio en representación de la empresa, nunca 
personal, para no compartir las claves entre varios usuarios.  
 
 
El proceso es muy sencillo, se han automatizado al máximo los procesos para que al usuario no le 
resulte tediosa caracterizar las facturas. Se procede  de la siguiente manera:  
1. En la entrada del SII, se muestran todas las facturas emitidas, clasificadas en dos 
pestañas,  "No enviadas"  y "Enviadas"  
2. En la pantalla principal existe un código de colores:  
 
• Blanco:  emitidas en el día o con fecha posterior al día y, que todavía no han entrado en 
fecha de descuento de 4 días.  
• Naranja:  todas aquellas facturas que han entrado en los 3 primeros días del tiempo de 
descuento de 4 días (tiempo legal máximo permitido para enviar la información).  
• Rojo:  aquellas facturas que están en el último día en plazo del tiempo, y además, 
aquellas que han excedido el plazo máximo de envío.   
*Nota:  Los días de control de elastic© BUSINESS, son días naturales y no días laborales como 
recomienda Hacienda. Hemos establecido un control conservador para mayor seguridad. En el caso de 
ventas  la fecha se hace a partir de la la fecha contable, por lo que la factura debe estar contabilizada.    
3. Para enviar el fichero se procederá de la siguiente manera. Se seleccionan una o varias 
facturas, aquellas que se quieran enviar. Una vez seleccionadas, se le dará a enviar y el sistema 
creará automáticamente el fichero y lo enviará a la plataforma de Haci enda. Previamente 
solicitará la clave del certificado digital. Se establece la comunicación, y a medida que vayan 
entrando las facturas en el sistema y sean Ok, pasan automáticamente a la pestaña de 
enviadas con código CVS asociado. Si la factura no es cor recta devuelve un no OK con un 


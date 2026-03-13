# elastic_business_modulo_ventas - Página 73

**Origen:** `docs\assets\source-pdfs\ventas\elastic_business_modulo_ventas.pdf`
**Módulo:** ventas

---

## Texto extraído

 
Manual de Usuario Módulo de Ventas  
   
 
 
elastic® B USINESS   Pág. 73 de 84 
 
  
Esta funcionalidad permite llevar a cabo los cobros de recibos de manera masiva. Permite a su vez la 
gestión bancaria, y la emisión de los cuadernos correspondientes para su cobro por gestión telemática.  
Los cobros se muestran agrupados por estados:  
• Pendientes: se muestran las remesas de cobro que todavía no han sido enviadas al banco.  
• Enviadas: se muestran las remesas que ya sido han enviadas al banco.  
• Validadas: se muestran las remesas que ya han sido enviadas y cobradas.  
Hay que recordar que al ser una herramienta que permite gestionar el cobro y su contabilización de 
manera pasiva, puede ser utilizado como comodín para gestionar remesas temporales que no tiene por 
qué enviarse a gestión de cobro mediante cuaderno bancario . Ejem: generar una remesa de todos los 
recibos de contado para un representante comercial. Una vez recopilado el importe de toda la remesa 
se puede dar por cobrado de manera masiva y contabilizar el cobro también de forma masiva.  
Desde el formulario de búsqueda, una vez localizada la remesa se accede a ella mediante doble clic sobre 
el detalle. El formulario posee dos secciones perfectamente diferenciadas:  
En la parte superior se encuentra la cabecera de la remesa de cobro.  
En la parte inferior se sitúa un conjunto de pestañas, donde se muestran los datos e información 
referentes a la remesa.  
 
En la cabecera se encuentran los datos principales de la remesa. Los únicos datos obligatorios son la 
descripción y la forma de cobro. Se muestran otros datos como la fecha de envío al banco, la fecha de 
vencimiento y de validación, el importe de la remesa , el margen de días, etc. La forma de cobro determina 
el cómo se quieren gestionar los recibos de esa remesa y determina también el modelo del asiento a 
generar en la contabilización.  
 
Básico : hace referencia a los datos bancarios donde se ingresa el cobro y los datos del ordenante. 
También permite añadir observaciones para las impresiones.  
Nota : Por defecto, el sufijo bancario para los datos del ordenante es "000". Si se tiene otro código se 
selecciona el que corresponda. Para dar de alta este código y que se muestre para seleccionar se debe 
dar de alta en tablas maestras: GENERAL. Sufijo para l as remesas.  
Pendientes : en esta pestaña se añaden y quitan los recibos pendientes de cobro.  
Cobrados : se muestran los recibos que han sido cobrados. Si se da por cobrado, los asientos se generan 
automáticamente. Si se quiere que los asientos se generen manualmente, se debe desactivar la 
propiedad que lo permite.  
Devueltos : se muestran los recibos devueltos por el banco.  
Nota : Si se quiere volver a generar un recibo que ha sido devuelto, se debe seleccionar "Generar recibo 
hijo".  
Nota : Si una línea de un recibo se muestra en verde significa que es un recibo de una devolución.  
Apuntes : según los recibos se van poniendo como cobrados o devueltos, se van generando apuntes.  
Nota : La forma de cobro seleccionada determinará el modelo de apuntes. Se generarán una serie de 
apuntes vinculados a la forma de cobro. Por ejemplo, en la forma de pago es "A vencimiento: CO", se 
cobran directamente y si es "A descuento: CA", puede generarse una cuenta puente para gestionar el 
riesgo con el banco.  


# elastic_business_cambios_ley_antifraude - Página 25

**Origen:** `docs\assets\source-pdfs\antifraude\elastic_business_cambios_ley_antifraude.pdf`
**Módulo:** antifraude

---

## Texto extraído

 
  
 
 
Elastic Business
 © 
Cambios Ley Antifraude v3  
| 
2
026  
 25 / 57 
www.imatia.com   
Durante la emisión de una factura, el sistema comprueba que la fecha y la hora del 
equipo sean correctas. Si no lo son, la factura no podrá emitirse.  
Esta validación es necesaria porque, al enviar los registros de facturación a la AEAT, el 
sistema VERI*FACTU verifica que el registro haya sido generado en un plazo máximo de 
dos minutos. Si la AEAT recibe un registro cuya fecha u hora no coincide con ese 
 margen, 
lo rechazará.  
 
 
Antes de emitir una factura, el sistema comprueba que exista un certificado digital válido 
y vigente. Si no se encuentra un certificado adecuado, la emisión queda bloqueada.  
Esta validación es necesaria porque el registro de facturación debe firmarse 
correctamente para poder comunicarse a la AEAT mediante VERI*FACTU.  
 
 
Cuando una factura se envía al SII, este puede rechazarla si no supera sus validaciones. 
Dado que una factura emitida no puede modificarse, cualquier corrección debe realizarse 
mediante una nueva factura rectificativa. La factura original no vuelve a envia
 rse al SII.  
En el menú Ventas >> SII se incorpora la pestaña Rechazadas, donde se muestran las 
facturas que han sido rechazadas o aceptadas con errores por el SII. Esta vista permite 
identificar rápidamente los documentos que requieren rectificación.  
 
Ilustración 30 – SII Ventas. Rechazas.  



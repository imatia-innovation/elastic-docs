# elastic_business_modulo_produccion - Página 22

**Origen:** `docs\assets\source-pdfs\produccion\elastic_business_modulo_produccion.pdf`
**Módulo:** produccion

---

## Texto extraído

 
 
 
 
 
 
 
 
 
Pág. 22/35 www.imatia.com  • Programación:  Código de la programación, se puede editar durante la creación de la 
programación, si no se modifica, se establece por contador.  
• Estado:  Diferentes estados en los que se encuentra una programación. Estos se dividen en:  
o Generada: Estado estándar de la programación al crearse.  
o Completa: Estado que se marca automáticamente al completarse todas las órdenes de 
fabricación, o en su defecto al cubrir la F.  completa.  
o Cerrada: Estado que se marca automáticamente al cubrir la F. cierre.  
• Grupo:  Grupo de programación.  
• Creador:  usuario que crea la programación.  
 
• F. prev. inicio:  Fecha que se establece indicando un inicio de plan maestro.  
• F. hasta:  Fecha que se establece indicando una previsión de fin del plan maestro.  
• F. inicio plan maestro:  Fecha que se cubre automáticamente al calcular el plan maestro en el 
botón de acción.  
• F. fin plan maestro:  Fecha que se cubre automáticamente al finalizar el cálculo del plan maestro 
en el botón de acción.  
• F. inicio cálc . nec: Fecha que se cubre automáticamente al calcular las necesidades en el botón 
de acción.  
• F. fin cálc. nec:  Fecha que se cubre automáticamente al finalizar el cálculo de las necesidades 
en el botón de acción.  
• F. completa:  Fecha que se cubre automáticamente al completar tod as las órdenes. Se puede 
cubrir manualmente.  
• F. cierre:  Fecha que se cubre manualmente.  
• Ignorar stock:  Si se marca este check, al añadir un artículo al plan maestro, no tiene en cuenta 
las unidades del almacén. El cálculo de necesidades se realiza ignorando lo que hay en el 
almacén. (Ejemplo: si tenemos 50 unidades en stock y necesitamos 100, no tendrá en cuentas 
el stock del articulo y nos fabricará 100).  
• Ignorar necesidades de stock:  Al tener este check activado, el cálculo de necesidades no 
realizará un barrido en el almacén comprobando que artículos tengan un stock mínimo 
configurado.  
• Preparada: Si se marca este check, lo que hace es meterla en una cola en la que se van 
generando las necesidades y plan maestro automáticamente.  
• Programación diaria: Si se marca este check, se crea una programación de forma diaria donde 
meterá todas las órdenes.  
• Reservar al generar:  Al tener marcado el check, cuando se genere la programación, se reserva 
automáticamente el material para esta.  
• Orden por operación: Al tener marcado el check, s e generará una orden por cada operación que 
tengamos en nuestros despieces y se incluirán en ella todos los artículos afectados por esa 
operación.  
• Orden por línea:  Al tener marcado el check, s e generará una orden diferente por cada detalle de 
pedido que incluyamos en nuestra programación . 
• Orden por artículo:  Al tener marcado el check, s e generará una orden diferente por cada artículo 
añadido en el plan maestro.  
• Mono -articulo:  Al tener marcado el check, hará programaciones de un solo artículo.  


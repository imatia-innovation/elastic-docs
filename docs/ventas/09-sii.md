# SII - Suministro Inmediato de Información

El SII hace referencia a la obligación, por parte de las empresas que cumplen con las condiciones establecidas por Hacienda Pública, de enviar sistemáticamente la información sobre las operaciones comerciales de venta/compra registrada mediante factura.

**Ruta de acceso:** `Ventas >> SII`

## Configuración inicial

Para utilizar esta funcionalidad:

1. **Ir a:** `Laboral >> Empresas >> Certificados`
2. **Adjuntar el certificado digital** emitido por la FMNT u otros organismos autorizados
3. **Formato aceptado:** Solo se acepta certificado con extensión **".pf2"** (el formato ".pfx" no es válido, pero se puede reconvertir)

> **Importante:** El sistema nunca pedirá la clave del certificado digital. Dicha clave será solicitada cada vez que se genere un fichero para envío al portal de Hacienda.

> **Recomendación:** Las personas que vayan a utilizar this sistema deben tener un certificado digital propio en representación de la empresa, nunca personal, para no compartir claves entre varios usuarios.

## Facturas

### Pantalla principal

En la entrada del SII se muestran todas las facturas emitidas, clasificadas en **2 pestañas**:

- **No enviadas:** Facturas pendientes de envío a Hacienda
- **Enviadas:** Facturas ya comunicadas

### Código de colores de control

El sistema utiliza un código de colores para alertar sobre plazos:

- **Blanco:** Facturas emitidas en el día o con fecha posterior, que aún no han entrado en descuento de 4 días
- **Naranja:** Facturas en los 3 primeros días del tiempo de descuento de 4 días (plazo legal máximo)
- **Rojo:** Facturas en el último día de plazo o que han excedido el plazo máximo de envío

> **Nota:** Los dias de control de elastic BUSINESS son dias naturales, no dias laborales. Hemos establecido un control conservador. En el caso de ventas, la fecha se hace a partir de la fecha contable, por lo que la factura debe estar contabilizada.

### Procedimiento de envío

Para enviar facturas:

1. **Seleccionar** una o varias facturas a enviar
2. **Pulsar Enviar** → El sistema crea automáticamente el fichero y lo envía a Hacienda
3. **Introducir** la clave del certificado digital cuando se solicite
4. **Resultado:**
   - Si correctas: Pasan a pestaña "Enviadas" con código CVS asociado
   - Si incorrectas: Devuelve código de error y permanence en "No enviadas"
5. **Corregir** las facturas con error y reenviar

> **Nota:** No existe un proceso de cancelación de envío.

### Consideraciones importantes

#### Plazo de envío
- Hasta el 1 de enero de 2018, Hacienda ha dado un plazo de 8 días
- elastic BUSINESS considera fuera de plazo a partir del cuarto dia (lo marca en rojo)

#### Clasificación de facturas
- elastic BUSINESS establece clasificacion por defecto para facilitar usabilidad
- Tipo de factura: Se clasifica automáticamente por serie (normales o rectificativas)
- Otras casuísticas: Deben seleccionarse manualmente

#### Tipo de operación
- Se coge automáticamente del tipo de operación asociado al IVA
- **Excepción:** Si la factura es de arrendamiento con tipo "Régimen General", existe un tipo específico que obliga a indicar tipo de activo y referencia catastral

#### Descripción
- Es un campo **obligatorio**
- No existe posibilidad de preconfigurar por defecto
- Se esperará información para automatizar este campo

#### Mezcla de operaciones
- **No es posible:** Mezclar tipos de operaciones distintas en una factura
- **Excepción:** Se puede mezclar "Tipo Régimen General" con operaciones "No sujetas"

#### Acceso al portal de Hacienda
- Se puede acceder directamente al portal para consultar más información
- **Importante:** Bajo ningún concepto editar la información en el portal
- El sistema no devolvera informacion a elastic BUSINESS, dejando de existir correlacion

#### Primer semestre
- La información del primer semestre según tipología de empresa puede no ser necesaria
- El sistema reconoce automáticamente la fecha y reconvierte la información al enviar

#### Facturas de aduanas
- **Excepción:** Facturas de aduanas que incluyan IVA de exportaciones e IVA de servicios
- Los conceptos deben ir separados en distintas facturas y clasificadas como tales

## Pagos

Esta sección permite gestionar el envío de información sobre pagos realizados a Hacienda, de acuerdo con la obligación AEAT.

> Para configurar y gestionar los pagos, seguir procedimiento similar al de facturas.

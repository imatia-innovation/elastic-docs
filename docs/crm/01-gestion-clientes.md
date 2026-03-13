---
sidebar_position: 1
---

# Gestión de Clientes

## Introducción al CRM

El módulo **CRM** gestiona la relación completa con clientes: desde contactos iniciales hasta órdenes de venta y seguimiento.

Acceso: **CRM >> Clientes**

## Registro de Clientes

### Datos Principales

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador único |
| **Código cliente** | Código usado por cliente |
| **Razón social** | Nombre legal |
| **Nombre comercial** | Nombre habitual |
| **CIF/NIF** | Identificación fiscal |
| **Dirección** | Domicilio principal |
| **Localidad** | Municipio |
| **Provincia** | Región |
| **País** | País de residencia |
| **Código Postal** | CP del domicilio |
| **Teléfono** | Contacto telefónico |
| **Email** | Correo electrónico |
| **Web** | Sitio web cliente |

### Información Comercial

- **Grupo cliente**: Categoría/segmento
- **Comercial**: Vendedor responsable
- **Forma de pago**: Condiciones de pago
- **Plazo pago**: Días de crédito (30, 60, 90)
- **Moneda**: Divisa de transacción (EUR, USD, etc.)
- **Persona contacto**: Nombre del responsable
- **Observaciones**: Información adicional

## Categorización de Clientes

### Por Tipo

- **Empresa**: Persona jurídica
- **Particular**: Persona física
- **Administración**: Sector público
- **Distribuidor**: Cliente mayorista
- **Minorista**: Cliente detallista

### Por Segmento

- **Clientes A**: Mayor volumen de venta
- **Clientes B**: Volumen medio
- **Clientes C**: Bajo volumen
- **Clientes Premium**: Especial alto valor
- **Clientes Potenciales**: En desarrollo

## Direcciones Múltiples

Cada cliente puede tener varias direcciones:

| Tipo | Uso |
|------|-----|
| **Facturación** | Para facturas |
| **Entrega** | Almacén del cliente |
| **Instalación** | Lugar de uso |
| **Contacto** | Direcciones alternas |

## Contactos del Cliente

Personas de contacto en la organización:

- **Nombre completo**
- **Puesto/Departamento**
- **Email** personal
- **Teléfono** directo
- **Notas** sobre preferencias

## Tarifas de Venta

Precios específicos por cliente.

Acceso: **CRM >> Clientes >> [Cliente] >> Tarifas**

### Configuración de Tarifa

- **Artículo**: Qué se vende
- **Precio**: Coste para cliente
- **Descuento**: De catálogo (%)
- **Cantidad mínima**: Mínimo de compra
- **Vigencia**: Desde-hasta
- **Moneda**: Divisa de precio

### Escalas de Precio

Descuentos por cantidad:

```
Cantidad    Precio Unitario
1-99        100€
100-499     95€
500-999     90€
1000+       85€
```

## Límite de Crédito

Control de riesgo crediticio:

| Campo | Descripción |
|-------|-------------|
| **Límite** | Máximo de deuda permitida |
| **Deuda actual** | Facturas pendientes |
| **Disponible** | Límite - Deuda |
| **Vencida** | Facturas atrasadas |

**El sistema alerta cuando:**
- Se alcanza el 80% del límite
- Se vence el plazo de pago
- Hay facturas atrasadas

## Histórico de Ventas

Seguimiento de interacción:

- **Pedidos**: Órdenes emitidas
- **Presupuestos**: Propuestas enviadas
- **Facturas**: Documentos contables
- **Cobros**: Pagos recibidos
- **Devoluciones**: Mercancía rechazada

## Comerciales y Responsables

Asignación de personal:

- **Comercial principal**: Vendedor responsable
- **Comercial secundario**: Apoyo
- **Técnico**: Soporte especializado
- **Logística**: Responsable entregas

## Segmentación para Campañas

Marcar clientes para:
- Campañas comerciales específicas
- Contacto periódico
- Promociones especiales
- Nuevos lanzamientos

## Integración con Ventas

### Flujo de Venta

```
Cliente → Presupuesto → Pedido → Albarán → Factura → Cobro
```

**Cada fase:**
1. **Presupuesto**: Propuesta de precio/plazo
2. **Pedido**: Confirmación de compra
3. **Albarán**: Envío de mercancía
4. **Factura**: Documento contable
5. **Cobro**: Recepción de pago

### Datos que se Heredan

Al crear documento desde cliente:
- Dirección de envío
- Tarifa de precios
- Forma de pago
- Plazo de pago
- Moneda
- Cuentas contables

## Integración CRM-Finanzas

### Impacto en Contabilidad

**Por cada venta:**
- Asiento contable automático
- Cuenta de cliente creada/actualizada
- Movimiento de facturación
- Reserva de ingreso

**Datos vinculados:**
- Subcuenta cliente 40xx (cuentas a cobrar)
- Cuenta ingresos (70x - venta de mercancías)
- Impuestos (IVA repercutido)
- Descuentos cliente

## Análisis de Cliente

### Reportes Disponibles

- **Ventas acumuladas**: Total histórico
- **Ventas período**: Mes/trimestre/año
- **Ticket medio**: Venta promedio
- **Frecuencia compra**: Periodicidad
- **Productos preferidos**: Artículos más vendidos
- **Rentabilidad**: Beneficio marginal por cliente
- **Antigüedad cliente**: Años trabajando juntos

## Mejores Prácticas

✓ Datos de cliente siempre actualizados  
✓ Múltiples contactos por cliente  
✓ Límite de crédito acorde a solvencia  
✓ Revisar histórico antes de vender  
✓ Mantener tarifas competitivas  
✓ Seguimiento periódico  
✓ Documentar cambios de condiciones  

## Privacidad y Compliance

- LOPD: Protección de datos personales
- RGPD: Regulación europea aplicable
- Consentimiento explícito para contacto
- Derecho al olvido si se solicita

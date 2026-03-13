---
sidebar_position: 2
---

# Flujo de Órdenes de Compra

## Proceso de Compra

El flujo de compra en Elastic Business se estructura en las siguientes fases:

```
Presupuesto → Pedido → Albarán → Factura → Pago
```

## Crear Pedido de Compra

Acceso: **Compras >> Pedidos de Compra**

### Datos de Cabecera

| Campo | Descripción |
|-------|-------------|
| **Proveedor** | Seleccionar del archivo maestro |
| **Código proveedor** | Referencia en sistema del proveedor |
| **Fecha pedido** | Cuando se emite |
| **Plazo entrega** | Días para recepción |
| **Forma de pago** | Condiciones acordadas |
| **Almacén destino** | Dónde entra la mercancía |
| **Referencia proveedor** | Su número de pedido |
| **Observaciones** | Notas especiales |

### Líneas de Pedido

Cada línea contiene:

- **Artículo**: Código y descripción
- **Cantidad**: Unidades solicitadas
- **Unidad**: Medida (kg, ud, cajas, etc.)
- **Precio unitario**: Coste por unidad
- **Descuento**: % de rebaja en línea
- **Total línea**: Cantidad × Precio - Descuento

### Gestión de Líneas

**Acciones disponibles:**
- Agregar nuevas líneas
- Duplicar líneas existentes
- Eliminar líneas
- Copiar líneas de otro pedido
- Importar desde presupuesto

## Estados del Pedido

| Estado | Significado |
|--------|------------|
| **Borrador** | No enviado, editable |
| **Emitido** | Enviado al proveedor |
| **Confirmado** | Aceptado por proveedor |
| **Parcialmente recibido** | Parte del pedido ha llegado |
| **Recibido** | Mercancía completa en almacén |
| **Facturado** | Factura de compra recibida |
| **Pagado** | Pago realizado |
| **Cancelado** | Anulado o rechazado |

## Recepción de Albaranes

Cuando el proveedor entrega la mercancía:

1. **Crear Albarán de Entrada**
   - Referencia al pedido
   - Fecha de recepción
   - Cantidades recibidas

2. **Control de Calidad**
   - Verificar coincidencia de cantidades
   - Inspeccionar estado de empaques
   - Detectar daños o defectos

3. **Actualización de Stock**
   - Mercancía entra en la ubicación asignada
   - Sistema actualiza existencias automáticamente
   - Genera movimiento de almacén

## Recepción de Facturas

La factura de compra es el documento contable definitivo:

### Datos de Factura

- **Número de factura**: Del proveedor
- **Fecha factura**: Fecha de emisión
- **Fecha contabilización**: Cuándo afecta contabilidad
- **Base imponible**: Total sin impuestos
- **IVA**: Impuesto aplicable
- **Total factura**: Cantidad a pagar

### Conceptos Adicionales

**Gastos planificados:**
- Transporte
- Embalaje
- Seguros
- Manipulación

Se distribuyen entre:
- Líneas del pedido (imputación a artículos)
- Costes generales (gastos indirectos)

### Afectación a Costes

El sistema actualiza:
- **Coste de materia prima**: Del artículo
- **Coste en almacén**: Promedio o última entrada
- **Asientos contables**: Registro fiscal

## Pagos a Proveedores

### Generación de Remesas

Agrupa facturas para pago:

1. Seleccionar facturas pendientes
2. Generar remesa de pago
3. Definir forma de pago
4. Procesar transferencia/cheque

### Formas de Pago

- **Transferencia bancaria**: Directo a cuenta
- **Cheque**: Documento de pago
- **Efectivo**: Liquidación en metálico
- **Domiciliación**: Cargo automático
- **Tarjeta**: Si aplica

### Control de Pagos

Monitorea:
- Facturas pendientes
- Plazos de pago vencidos
- Descuentos por pronto pago
- Retenciones fiscales

## Órdenes de Compra Recurrentes

Para proveedores habituales:

- Crear plantilla de pedido
- Copiar configuración automáticamente
- Acelerar proceso
- Mantener consistencia

## Devoluciones a Proveedores

Si hay rechazo de mercancía:

```
Nota de Crédito → Albarán de Devolución → Abono
```

1. **Crear nota de crédito**: Especificar motivo
2. **Devolver mercancía**: Albarán de salida
3. **Recibir abono**: Del proveedor

## Integración Contable

### Asientos Generados

**En recepción de albarán:**
- Cuenta proveedores (acreedora)
- Cuentas de activo/gasto (deudoras)

**En factura de compra:**
- Ajustes por IVA
- Refinanciación de cuentas

**En pago:**
- Banco (deudor)
- Proveedores (acreedor)
- Retenciones (si aplica)

## Mejores Prácticas

✓ Comparar albarán con pedido antes de aceptar  
✓ Verificar factura antes de contabilizar  
✓ Mantener documentación ordenada  
✓ Registrar rechazos inmediatamente  
✓ Negociar plazos de pago óptimos  
✓ Usar características de descuento por pronto pago  
✓ Revisar desviaciones de precio respecto tarifa  

## Reportes de Control

- Pedidos pendientes de recepción
- Albaranes sin facturar
- Facturas pendientes de pago
- Análisis de desviaciones
- Proveedores con retrasos

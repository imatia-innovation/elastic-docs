---
sidebar_position: 1
---

# Gestión de Proveedores

## Introducción

El módulo de **Compras** gestiona todas las operaciones relacionadas con la adquisición de productos y servicios. Todo el flujo comienza con una correcta definición de proveedores.

## Registro de Proveedores

Para acceder a la gestión de proveedores:
**Compras >> Proveedores**

### Datos Principales

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador único del proveedor |
| **Código cliente** | Código del proveedor en su organización |
| **Razón social** | Nombre legal del proveedor |
| **Nombre comercial** | Nombre con el que se conoce |
| **CIF/NIF** | Identificación fiscal |
| **Dirección** | Domicilio principal |
| **Localidad** | Municipio |
| **Provincia** | Región administrativa |
| **País** | País de origen |
| **Código Postal** | Código postal |
| **Teléfono** | Contacto telefónico |
| **Email** | Correo electrónico |
| **Web** | Sitio web del proveedor |

### Información Adicional

- **Persona de contacto**: Responsable identificado
- **Forma de pago**: Condiciones acordadas
- **Plazo de entrega**: Días habituales de envío
- **Moneda**: Moneda de cotización
- **Incoterm**: Términos comerciales internacionales
- **Observaciones**: Notas relevantes

## Tarifas de Compra

Cada proveedor puede tener una o varias **tarifas de compra** que definen precios por artículo.

### Configuración de Tarifa

```
Compras >> Proveedores >> [Proveedor] >> Tarifas
```

**Elementos de una tarifa:**
- Artículo
- Cantidad mínima
- Precio unitario
- Descuentos por cantidad
- Plazo de entrega
- Exclusividad
- Fecha vigencia

### Gestión de Precios

- Actualizar tarifas según cambios de mercado
- Definir precios por cantidad (escalas de precio)
- Aplicar descuentos porcentuales
- Historizar cambios de precio para análisis

## Categorías de Proveedores

Clasifica proveedores por:
- **Materias primas**: Suministros básicos
- **Componentes**: Piezas para manufactura
- **Subcontratistas**: Servicios especializados
- **Servicios**: Proveedores de servicios internos
- **Logística**: Transporte y distribución

## Documentos de Compra

El flujo de compras sigue esta secuencia:

### 1. Presupuesto (Solicitud Precio)

- Solicitud de presupuesto a proveedor
- Recepción de propuesta con terminos
- Comparativa de opciones

### 2. Pedido de Compra

- Confirmación de compra con:
  - Cantidad exacta
  - Precio unitario
  - Condiciones de entrega
  - Forma de pago
- Referencia para proveedor y almacén

### 3. Albarán de Entrada

- Recepción física de mercancía
- Verificación de cantidades
- Control de calidad
- Ubicación en almacén

### 4. Factura de Compra

- Documento contable definitivo
- Base para pagos
- Registro de gastos
- Impacto fiscal (IVA)

## Características Especiales

### Compras por Licitación

Para grandes volúmenes o compras públicas:
- Solicitud de ofertas múltiples
- Comparación estructurada
- Selección por criterios (precio, plazo, calidad)
- Contratación del ganador

### Gastos Planificados

Gastos adicionales que se distribuyen:
- **Portes**: Costos de transporte
- **Seguros**: Cobertura de envío
- **Aranceles**: Derechos aduanales
- **Manipulación**: Costos de manejo

Distribución por:
- Importe fijo
- Porcentaje del total
- Por línea de compra
- Por cantidad/peso

### Subcontratación

Para servicios o procesos externos:
- Definir operaciones subcontratadas
- Material en consignación
- Control de almacén externo
- Órdenes de subcontratación

## Integración con Otros Módulos

| Módulo | Integración |
|--------|------------|
| **Almacén** | Entrada de mercancía, costes de materia prima |
| **Finanzas** | Cuentas por pagar, asientos contables |
| **Producción** | Compras de materias primas para fabricación |
| **CRM** | Información de proveedores clave |

## Mejores Prácticas

✓ Mantener datos de proveedores actualizados  
✓ Revisar periódicamente tarifas y plazos  
✓ Documentar cambios de condiciones  
✓ Establecer criterios de selección claros  
✓ Monitorear desempeño de proveedores  
✓ Negociar términos de pago sostenibles  
✓ Verificar documentación fiscal/legal  

## Reportes Disponibles

- Listado de proveedores
- Tarifas de compra activas
- Histórico de compras por proveedor
- Análisis de costes por proveedor
- Evaluación de desempeño

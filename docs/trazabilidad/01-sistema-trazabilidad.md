---
sidebar_position: 1
---

# Sistema de Trazabilidad

## Concepto de Trazabilidad

La **trazabilidad** permite rastrear el recorrido de un producto desde su origen (compra de materia prima) hasta su destino final (cliente).

## Normativa Aplicable

Obligatoria en sectores como:
- **Alimentación**: Control de lotes y fechas
- **Farmacéutico**: Medicamentos específicos
- **Automoción**: Componentes críticos
- **Químico**: Productos peligrosos

## Tipos de Identificación

### 1. Número de Lote

Agrupa múltiples unidades de mismo origen.

**Información de lote:**
- Número identificación
- Fecha de vencimiento
- Fecha de fabricación
- Proveedor (si se compró)
- Número de serie del proveedor
- Notas de lote

### 2. Número de Serie

Identifica unidad individual.

**Casos de uso:**
- Productos de alto valor
- Garantía individual
- Seguimiento exacto
- Devoluciones específicas

### 3. Lote Producto

Combinación lote + serie para productos compuestos.

## Configuración en Familia

### Activar Trazabilidad

Acceso: **Almacén >> Familias >> [Familia] >> Configuración**

- **Trazable**: Marcar si aplica
- **Tipo**: 
  - Lote
  - Lote producto
  - Número de serie

### Familias Trazables vs No Trazables

- Si familia es trazable: todos sus artículos llevan trazabilidad
- Si no está marcada: se puede activar por artículo específico
- Cambio posterior requiere migración de datos

## Entrada de Lotes en Almacén

### Recepción de Compra

Al recibir mercancía:

```
Almacén >> Albaranes >> [Albarán]
    Línea de artículo → Asignar lote
```

**Datos de lote entrada:**
- Número de lote (del proveedor o asignado)
- Cantidad recibida
- Fecha vencimiento
- Ubicación en almacén
- Observaciones

### Generación Manual de Lote

```
Almacén >> Gestión Stock >> Lotes
    Crear nuevo lote
```

Para producción propia o ajustes.

## Salida de Lotes por Venta

### Reserva de Lotes

En pedido de venta, el sistema:
1. Verifica stock disponible por lote
2. Reserva lotes específicos
3. Aplica FIFO (primero entra, primero sale)

### Confirmación en Albarán

Al generar albarán de salida:
- Se especifica qué lote sale
- Se imprime en documentos (albarán, factura)
- Cliente recibe trazabilidad

## Lotes en Producción

### Despiece de Entrada

Cuando se consume materia prima:
```
Orden de fabricación
  └── Línea: Artículo X (100 uds)
      └── Necesita: Lote 2024-001 (200g)
```

### Lotes de Salida

Producto terminado recibe:
- Lote propio de fabricación
- Fecha de fabricación
- Referencias de lotes entrada (trazabilidad inversa)

### Relaciones Lote→Lote

Sistema registra:
```
Lote producto terminado 2024-P01
  ├── Contiene: 50% Lote materia prima 2024-MP001
  ├── Contiene: 30% Lote materia prima 2024-MP002
  └── Operación: Sección pintura (2024-04-15)
```

## Consultas de Trazabilidad

### Trazabilidad Hacia Adelante

"¿Dónde fue a parar el lote 2024-MP001?"

```
Laboral >> Trazabilidad >> Lotes
    Búsqueda lote origen
    └── Órdenes producción
        └── Lotes resultado
            └── Albaranes envío
                └── Cliente final
```

### Trazabilidad Hacia Atrás

"¿De dónde vino el lote 2024-P01?"

```
Lote producto terminado 2024-P01
    ├← Lotes materias primas
    ├← Proveedores
    └← Documentos compra originales
```

## Gestión de Vencimientos

### Alertas de Caducidad

El sistema avisa cuando:
- Lote está por vencer (7 días)
- Lote ha vencido

```
Laboral >> Alertas >> Vencimientos
```

### Retira Preventiva

Ante riesgo:
1. Marcar lote como "retirado"
2. Generar aviso a clientes
3. Iniciar devoluciones
4. Registro del incidente

## Devoluciones Rastreadas

Cuando cliente devuelve artículo:

```
Devuelto lote 2024-P01
    ├── Fecha salida: 2024-04-10
    ├── Fecha entrada devolución: 2024-04-20
    ├── Motivo: Defecto de pintura
    └── Acción: Destruir / Reprocesar
```

## Reportes de Trazabilidad

### Disponibles en Sistema

- **Lotes activos**: Stock actual por lote
- **Lotes por vencer**: Riesgo de caducidad
- **Histórico lote**: Movimientos completos
- **Trazabilidad cruzada**: Relaciones lote→lote
- **Cumplimiento**: Evidencia de trazabilidad

## Cumplimiento Normativo

### Documentación Requerida

✓ Entrada de materias primas con lote  
✓ Registro de fabricación por lote  
✓ Salida a cliente con lote  
✓ Retención de muestra (si aplica)  
✓ Certificados de análisis  
✓ Decisiones de retira  

### Auditoría

Capacidad de demostrar:
- Origen de cada lote
- Procesos aplicados
- Personas responsables
- Fechas exactas
- Cambios en el sistema

## Ejemplos de Aplicación

### Caso Industria Alimentaria

```
Lote 2024-LECHE-001 (Leche pasteurizada)
    ├── Recibida: 2024-04-01
    ├── Vencimiento: 2024-04-15
    ├── Utilizada en: Yogurt lote 2024-YOGURT-042
    └── Vendida cliente: 2024-04-12 → Cliente ABC
        └── Si problema: Retira directa de cliente
```

### Caso Automoción

```
Lote 2024-MOTOR-V8-101 (Motores V8)
    ├── 5 unidades sin serie
    └── Serie 1-5 asignada en producción
        ├── Serie 1 → Auto modelo X
        ├── Serie 2 → Auto modelo Y
        └── etc.
```

## Mejores Prácticas

✓ Activar trazabilidad desde inicio  
✓ Códigos de lote claros y únicos  
✓ Registrar vencimientos exactamente  
✓ Revisar alertas diariamente  
✓ Documentación completa en retiras  
✓ Capacitación de personal  
✓ Auditorías periódicas  

## GDPR y Privacidad

Si lotes incluyan datos personales:
- Proteger información
- Acceso restringido
- Retención limitada
- Derecho al olvido

---
sidebar_position: 1
---

# Plan General Contable (PGC)

## Introducción

La **contabilidad** en Elastic Business se estructura sobre el Plan General Contable, que organiza la información según estándares fiscales y normas de contabilidad española.

## Acceso

**Finanzas >> Plan General Contable**

## Estructura del PGC

El PGC está organizado jerárquicamente:

```
Clases (1-9)
  └── Grupos (grupos de 2 dígitos)
      └── Subgrupos (3 dígitos)
          └── Cuentas (4 dígitos)
              └── Subcuentas (6 dígitos)
```

### Clases Principales

| Clase | Descripción | Ejemplos |
|-------|-------------|----------|
| **1** | ACTIVO NO CORRIENTE | Inmovilizado, activos fijos |
| **2** | ACTIVO CORRIENTE | Existencias, clientes, bancos |
| **3** | PASIVO NO CORRIENTE | Deudas a largo plazo |
| **4** | PASIVO CORRIENTE | Proveedores, deudas corto plazo |
| **5** | PATRIMONIO NETO | Capital, reservas |
| **6** | GASTOS | Compras, suministros, personal |
| **7** | INGRESOS | Ventas, servicios |
| **8** | CUENTAS DE CIERRE | Balances |
| **9** | CUENTAS ANALÍTICAS | Costes por secciones |

## Creación de Cuentas

### 1. Crear Grupo

Acceso: **Finanzas >> Grupos de Cuentas**

- Código grupo (2 dígitos)
- Descripción
- Clase (1-9)

### 2. Crear Cuenta

Acceso: **Finanzas >> Cuentas Contables**

| Campo | Descripción |
|-------|-------------|
| **Código** | 4 dígitos del PGC |
| **Descripción** | Nombre de la cuenta |
| **Grupo** | Seleccionar grupo padre |
| **Tipo cuenta** | Balance, ingresos, gastos |
| **Subcuentas** | Permitir desagregación |

### 3. Crear Subcuenta

Acceso: **Finanzas >> Subcuentas**

**Campos específicos:**

- **Código**: 6 dígitos (4 de cuenta + 2 de subcuenta)
- **Descripción**: Denominación
- **Cuenta padre**: Cuenta contenedora
- **Tipo operación**: Compra, venta, tesorería
- **Tipo subcuenta**: Cliente, proveedor, IVA, etc.
- **Datos beneficiario**: Para transferencias

## Estructura Balance

```
ACTIVO = PASIVO + PATRIMONIO

ACTIVO (Clases 1-2)
├── No corriente (inmovilizado)
└── Corriente (corto plazo)

PASIVO (Clases 3-4)
├── No corriente (largo plazo)
└── Corriente (corto plazo)

PATRIMONIO (Clase 5)
├── Capital
├── Reservas
└── Resultados
```

## Configuración por Tipo de Subcuenta

### Clientes

Cuentas de deuda de clientes:
- Facturación genérica
- Por cliente específico
- Descuentos cliente
- Devoluciones

### Proveedores

Cuentas de deuda hacia proveedores:
- Facturación genérica
- Por proveedor específico
- Descuentos obtenidos
- Devolu ciones

### IVA

Diferenciación entre:
- **IVA soportado**: Impuesto de compras (recuperable)
- **IVA repercutido**: Impuesto de ventas (pagadero)
- **IVA compensado**: Diferencia a pagar/cobrar

### Tesorería

- Bancos y cajas
- Cuentas de tránsito
- Diferencias de cambio

## Propiedades de Subcuentas

### Parámetro Moneda

- **Euro**: Transacciones en euros
- **Moneda extranjera**: Especificar divisa
- **Ambas**: Se permite divisa dual

### Parámetro Tipo Operación

Define qué operaciones impactan:
- Compra interna
- Compra importación
- Venta nacional
- Venta intracomunitaria
- Venta exportación

**Usado para:**
- Informes fiscales
- Declaraciones de IVA
- Reportes de intracomunitario

### Desglose Dimensional

Asignar valores de dimensiones:
- Centro de coste
- Proyecto
- Departamento
- División

## Importación de Cuentas

Para acelerar configuración:

1. Descargar plantilla del PGC
2. Rellenar datos específicos
3. Importar archivo
4. Validar datos importados

## Consultas Contables

### Libro Mayor

Movimientos de cada cuenta:
```
Saldo inicial + Movimientos = Saldo final
```

### Consulta de Saldos

Ver estado actual de cuentas:
- Deudor/Acreedor
- Movimientos del período
- Comparativa con períodos previos

### Balance de Comprobacion

Verifica:
- Total débitos = Total créditos
- Coherencia de registros

## Mejores Prácticas

✓ Crear estructura clara y consistente  
✓ No crear subcuentas innecesariamente  
✓ Documentar el propósito de cada cuenta  
✓ Respetar estándares fiscales  
✓ Revisión periódica (mensual/trimestral)  
✓ Mantener coherencia entre módulos  
✓ Usar dimensiones para análisis  

## Integración con Operaciones

**La contabilidad se alimenta de:**
- Ventas (facturas de clientes)
- Compras (facturas de proveedores)
- Nóminas (gastos de personal)
- Tesorería (pagos/cobros)
- Producción (costes registrados)

**Cada módulo genera asientos automáticamente:**
El sistema valida que cada operación afecte a cuentas configuradas correctamente.

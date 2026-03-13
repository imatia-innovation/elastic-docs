---
sidebar_position: 2
---

# Dimensiones de Análisis

## Concepto

Las **dimensiones** permiten analizar la contabilidad desde diferentes perspectivas más allá de la estructura traditional de cuentas.

Ejemplo: Una venta se puede analizar por:
- Producto/línea de negocio
- Centro de beneficio
- División geográfica
- Departamento
- Proyecto

## Acceso

**Finanzas >> Configuración >> Dimensiones**

## Tipos de Dimensiones

### 1. Centros de Coste

Distribuye costes por responsabilidad:
- Departamentos (RRHH, IT, Marketing)
- Divisiones (España, Extranjero)
- Líneas de negocio (Producto A, Producto B)

**Usar para:**
- Asignar gastos a departamentos
- Evaluar rentabilidad por centro
- Presupuestos analíticos

### 2. Proyectos/Órdenes

Agrupa gastos/ingresos por proyecto:
- Proyecto interno
- Contrato con cliente
- Iniciativa especial

**Usar para:**
- Rentabilidad del proyecto
- Control de costes por proyecto
- Facturación a cliente

### 3. Otras Dimensiones

Según necesidades:
- Producto/línea
- Zona geográfica
- Vendedor/responsable
- Cliente estratégico

## Creación de Dimensión

### Paso 1: Definir Dimensión

**Campos:**
- Código dimensión (ID)
- Descripción
- Tipo (coste, proyecto, otra)
- Permite múltiples valores por documento

### Paso 2: Valores de Dimensión

Para cada dimensión, crear valores:

| Código | Descripción |
|--------|-------------|
| CC001 | Dirección General |
| CC002 | Ventas |
| CC003 | Compras |
| CC004 | Producción |

### Paso 3: Asignar a Subcuentas

Configurar qué subcuentas aplican:
- Cuentas de gasto (dimensión obligatoria)
- Cuentas de ingresos (opcional)
- Cuentas de balance (generalmente no)

## División de Asientos

El sistema permite **dividir automáticamente** asientos:

Si un asiento es de 1.000€ en una cuenta de gasto y se divide entre 3 centros:

```
Asiento original:
    Cuenta gasto    1.000€  (CC general)

Se genera:
    CC001  333,33€
    CC002  333,33€
    CC003  333,34€
```

### Métodos de División

- **Fija**: Porcentajes predefinidos
- **Por artículo**: Según cantidad de líneas
- **Manual**: Especificar por línea

## Subcuentas con Dimensiones

Al crear/editar subcuenta:

```
Finanzas >> Subcuentas >> [Subcuenta]
    Pestaña: Dimensiones
```

**Configurar:**
- Qué dimensiones aplican
- Si es obligatoria o facultativa
- Valor por defecto

## Análisis con Dimensiones

### Consultas Analíticas

Ver resultados por dimensión:
- Gasto mensual por centro: CC001, CC002, CC003
- Rentabilidad por proyecto
- Costes por vendedor

### Reportes

**Mayor analítico:**
Movimientos agrupados por dimensión

**Comparativa períodos:**
Evolución del coste por centro en meses/trimestres

**Análisis de varianzas:**
Diferencia real vs presupuestado por centro

## Integración de Operaciones

Cuando se registra una operación:

1. **Venta**: Asignar proyecto/cliente
2. **Compra**: Asignar centro de coste
3. **Gasto**: Dimensionar automáticamente
4. **Nómina**: Distribuir salarios por departamento

Ejemplo - Implementación de presupuesto:
```
Presupuesto deptal. (CC002-Ventas):
    Gastos viaje: 5.000€
    Software: 2.000€

Asientos se registran:
    Gasto viaje    2.500€ → CC002
    Gasto software 2.000€ → CC002

Control de varian zas:
    Presupuesto: 7.000€
    Real: 4.500€
    Varianza: -2.500€ (favorable)
```

## Mejores Prácticas

✓ Definir dimensiones según estructura organizativa  
✓ Usar códigos mnemotécnicos (CC + número)  
✓ Mantener dimensiones consistentes  
✓ No crear dimensiones demás (complejidad)  
✓ Documentar cada dimensión  
✓ Revisar análisis regularmente  
✓ Capacitar usuarios en su uso  

## Nuevas Funcionalidades

###  Múltiples Dimensiones

Un asiento puede llevaretagos:
- Centro de coste CC002
- Proyecto PROY001
- Simultáneamente

Permite análisis cruzados más sofisticados.

## Vinculación con Presupuestos

Las dimensiones se usan para:
- Crear presupuestos por centro
- Comparar real vs presupuestado
- Identificar desviaciones
- Proyecciones presupuestarias

## Limitaciones y Consideraciones

- No todas las subcuentas pueden llevar dimensiones
- Performance: Demasiadas combinaciones ralentizan
- Consistencia: Nomenclatura clara evita errores
- Cambios posteriores: Requieren ajustes en históricos

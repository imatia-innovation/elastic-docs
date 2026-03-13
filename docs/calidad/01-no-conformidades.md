---
sidebar_position: 1
---

# Control de No Conformidades

## Concepto

Una **no conformidad** es cualquier desviación respecto a especificaciones, requisitos o expectativas.

**Ejemplos:**
- Producto recibido del proveedor con defecto
- Cliente rechaza mercancía por incumplimiento
- Rechazo en control de calidad interno
- Incumplimiento de plazo de entrega
- Documentación incompleta

## Clasificación

### Por Origen

| Tipo | Descripción |
|------|-------------|
| **Proveedor** | Compras que no cumplen especificaciones |
| **Interna** | Defectos en producción |
| **Cliente** | Reclamación del usuario final |
| **Proceso** | Incumplimiento de procedimiento |

### Por Severidad

- **Crítica**: Riesgo de seguridad
- **Mayor**: Afecta funcionalidad
- **Menor**: Aspecto cosmético

## Acceso al Sistema

**Calidad >> No Conformidades**

## Creación de No Conformidad

### Datos de Cabecera

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador único |
| **Fecha** | Cuándo se detecta |
| **Tipo** | Proveedor/Interna/Cliente/Proceso |
| **Proveedor** | Si es de compra |
| **Cliente** | Si es de venta |
| **Artículo** | Producto afectado |
| **Lote** | Número de lote (si aplica) |
| **Cantidad** | Unidades afectadas |
| **Descripción** | Qué no cumple |

### Categorización

- **Área responsable**: Dónde se detecta (almacén, producción, QA)
- **Responsable**: Persona que la abre
- **Prioridad**: Urgencia de resolución
- **Causa probable**: Hipótesis inicial (si se conoce)

## Análisis de Causa

### Investigación

Determinar por qué ocurrió:

```
Problema: Arruga en pintura

Causas potenciales:
  ├── Humedad en el aire (>80%)
  ├── Temperatura fuera de rango
  ├── Viscosidad de pintura incorrecta
  └── Superficie mal preparada
```

### Root Cause Analysis (RCA)

Técnica de "5 por qué":

```
1. ¿Por qué hay arruga?
   → Viscosidad incorrecta

2. ¿Por qué viscosidad incorrecta?
   → No se midió antes de aplicar

3. ¿Por qué no se midió?
   → No estaba en protocolo

4. ¿Por qué no en protocolo?
   → Cambio de proveedor sin actualizar

5. ¿Por qué no se actualizó?
   → Falta de comunicación
```

**Causa raíz**: Falta de comunicación en cambio de proveedor

## Soluciones Propuestas

### Acciones Correctivas

Cambios permanentes para evitar repetición:

- **Tipo**: Inmediata, preventiva, correctiva
- **Descripción**: Qué se va a cambiar
- **Responsable**: Quién ejecuta
- **Plazo**: Cuándo debe estar done
- **Evidencia**: Cómo se verifica

**Ejemplo:**
```
Acción: Crear especificación de viscosidad en procedimiento
Responsable: Jefe Calidad
Plazo: 2 semanas
Verificación: Protocolo firmado y training de staff
```

### Acciones Inmediatas

Si no se puede esperar:

- **Cuarentena**: Aislar producto
- **Reparación**: Reprocesar o reparar
- **Destrucción**: Si es irrecuperable
- **Comunicación**: Avisar a cliente si salió

## Seguimiento

### Estados de No Conformidad

```
Abierta
  ↓
Investigada
  ↓
Acción propuesta
  ↓
Acción implementada
  ↓
Verificada
  ↓
Cerrada
```

### Reoperturas

Si no se resuelve:
```
Cerrada
  ↓ (recurrencia detectada)
  ↓
Reabierta
  └── Nueva investigación
```

## Costes de No Conformidad

Registrar impacto económico:

| Concepto | Coste |
|----------|-------|
| **Rechazo** | 500€ |
| **Reelaboración** | 200€ |
| **Logística retorno** | 150€ |
| **Tiempo administrativo** | 100€ |
| **TOTAL** | 950€ |

### Análisis de Cartera ABC

Priorizar inversión en mejoras según:
- Cantidad de no conformidades
- Coste acumulado
- Clientes/proveedores afectados

## Comunicación Externa

### A Proveedores

Si es de compra:

```
Carta de no conformidad
├── Descripción del problema
├── Cantidad rechazada
├── Causa raíz identificada
├── Solución esperada
├── Plazo de respuesta
└── Acciones correctivas propuestas
```

### A Clientes

Si es de venta:

```
Comunicación cliente
├── Reconocer el problema
├── Acción inmediata (retira)
├── Investigación en curso
├── Prevención futura
└── Compensación (si aplica)
```

## Trazabilidad de Causa

Vinculación con:
- **Almacén**: Lotes afectados
- **Producción**: Órdenes y operaciones
- **Compras**: Pedidos al proveedor
- **Clientes**: Facturas donde llegó
- **Personal**: Quién ejecutó la operación

## Reportes Disponibles

### Gestión de Calidad

- **No conformidades abiertas**: Pendientes de cierre
- **Evolución temporal**: Tendencias
- **Por proveedor**: Análisis de desempeño
- **Por tipo**: Clasificación de problemas
- **Por coste**: Impacto económico
- **Efectividad de acciones**: % de cierre

### Métricas KPI

```
No conformidades / mes
Tiempo promedio resolución
% de recurrencias
Coste total / período
ROI de mejoras implementadas
```

## Mejores Prácticas

✓ Registrar inmediatamente al detectar  
✓ Investigar a fondo, evitar síntomas  
✓ Involucrar personal relevante  
✓ Comunicar abiertamente  
✓ Seguimiento hasta cierre  
✓ Documentación completa  
✓ Revisar tendencias regularmente  

## Integración con Otros Módulos

| Módulo | Impacto |
|--------|--------|
| **Almacén** | Cuarentena de lote |
| **Compras** | Reclamación a proveedor |
| **Producción** | Parada de línea |
| **Laboral** | Capacitación requerida |
| **Finanzas** | Coste de no conformidad |

## Normativas de Calidad

- **ISO 9001**: Sistema de gestión calidad
- **ISO 14001**: Gestión ambiental
- **Sector específico**: Alimentario, farmacéutico, automoción, etc.

Cada norma establece procedimientos para gestión de no conformidades.

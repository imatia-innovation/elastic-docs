---
sidebar_position: 1
---

# Estructura de Producción

## Introducción a la Fábrica

Para un control eficaz de la **producción**, es necesario definir la estructura organizativa de la fábrica, máquinas, secciones y empleados.

Acceso: **Producción >> Configuración >> Instalaciones**

## Jerarquía de Instalaciones

```
Organización
  └── Fábrica
      ├── Línea de Producción
      │   └── Sección
      │       └── Máquina/Puesto
      └── Empleado
      └── Operación
```

## 1. Fábrica

### Creación de Fábrica

**Campos principales:**

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador de fábrica |
| **Descripción** | Nombre/ubicación |
| **Localidad** | Dónde está ubicada |
| **Responsable** | Encargado de fábrica |
| **Horario** | Jornada laboral |

### Configuración

- Calendario laboral (turnos, festivos)
- Capacidad productiva
- Líneas disponibles
- Empleados asignados

## 2. Líneas de Producción

Agrupaciones de secciones por proceso.

**Ejemplo:**
```
Fábrica: Planta Principal
  ├── Línea 1: Preparación
  ├── Línea 2: Mecanizado
  ├── Línea 3: Pintura
  └── Línea 4: Ensamblado
```

### Propiedades

- Código única dentro de fábrica
- Descripción
- Orden de proceso
- Capacidad
- Personal asignado

## 3. Secciones

Unidades funcionales dentro de línea.

**Ejemplo - Línea Mecanizado:**
```
Sección Torno
Sección Fresadora
Sección Taladrador
```

### Configuración de Sección

- **Código**: Identificador
- **Descripción**: Nombre
- **Línea padre**: Línea contenedora
- **Empleados**: Asignación de personal
- **Máquinas**: Equipamiento
- **Operaciones**: Procesos ejecutados

## 4. Máquinas/Puestos

Equipamiento en secciones.

**Datos de máquina:**
- Código identificación
- Modelo
- Serial
- Fecha instalación
- Estado (activa/mantenimiento/baja)
- Coste hora máquina
- Coef. eficiencia

## 5. Operaciones

Actividades que transforma materiales.

Acceso: **Producción >> Operaciones**

### Creación de Operación

**Campos:**

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador |
| **Descripción** | Nombre de operación |
| **Tipo** | Mecanizado, pintura, ensamblado, etc. |
| **Sección** | Dónde se realiza |
| **Tiempo estándar** | Minutos previstos |
| **Coste hora hombre** | Salario/hora |
| **Coste hora máquina** | Amortización equipamiento |
| **Coef. eficiencia** | Multiplicador según operario |

### Configuración de Coste

```
Coste operación = 
    (Tiempo × Coste hora hombre × Coef. hombre) +
    (Tiempo × Coste hora máquina × Coef. máquina)
```

## 6. Empleados en Producción

Acceso: **Módulo Laboral >> Empleados**

### Asignación a Producción

Cada empleado puede tener:
- Sección asignada
- Máquinas que puede operar
- Coste hora personal
- Coeficiente eficiencia
- Turnos (mañana, tarde, noche)

## Flujo de Configuración

### Paso 1: Crear Fábrica
```
Código: FAB01
Descripción: Planta Principal Barcelona
```

### Paso 2: Crear Líneas
```
LIN01 → Preparación
LIN02 → Mecanizado
LIN03 → Pintura
```

### Paso 3: Crear Secciones
```
LIN02 Secciones:
  - SEC201: Torneado
  - SEC202: Fresado
```

### Paso 4: Crear Máquinas
```
SEC201 Máquinas:
  - MQ201A: Torno CNC 1
  - MQ201B: Torno CNC 2
```

### Paso 5: Crear Operaciones
```
OP0201: Torneado cilindro
  - Sección: SEC201
  - Tiempo: 15 minutos
  - Máquina: MQ201A
```

### Paso 6: Asignar Empleados
```
Empleado José García:
  - Sección: SEC201
  - Máquinas: MQ201A, MQ201B
  - Coste/hora: 15€
```

## Clasificación de Operaciones

### Por Tipo

- **Mecanizado**: Uso de máquinas
- **Mano de obra**: Trabajo manual
- **Ensamblado**: Montaje de componentes
- **Control calidad**: Inspección
- **Empaquetado**: Preparación para envío

### Por Naturaleza

- **De máquina**: Requieren equipamiento
- **Manual**: Solo personal
- **Mixta**: Máquina + operario

## Utillajes

Accesorios necesarios para operaciones.

Acceso: **Producción >> Utillajes**

### Configuración

- Código identificación
- Descripción
- Tipo de utillaje
- Compatible con máquinas
- Estado (activo/baja)
- Valor de adquisición
- Vida útil

### Gestión

- Registro de utillajes activos
- Histórico de utillajes dados de baja
- Mantenimiento programado
- Sustituciones

## Integración de Datos

### Desde Almacén

- Acceso a catálogo de artículos
- Stock disponible
- Costes de materiales

### Desde Laboral

- Empleados disponibles
- Calendarios y turnos
- Nómina y costes

### Desde Finanzas

- Costes por operación
- Presupuestos de producción
- Análisis de rentabilidad

## Mejores Prácticas

✓ Estructura clara y manejable  
✓ Códigos nemotécnicos (FAB + número)  
✓ Actualización de tiempos estándares  
✓ Mantener máquinas calibradas  
✓ Documentar cambios de proceso  
✓ Capacitación en nuevas operaciones  
✓ Revisión periódica de costes  

## Reportes Disponibles

- Estructura de fábrica
- Carga de máquinas
- Disponibilidad de personal
- Tiempos de operación
- Costes de operaciones

---
sidebar_position: 1
---

# Gestión de Empleados

## Introducción al Módulo Laboral

El módulo **Laboral** gestiona toda la información de recursos humanos: empleados, nóminas, vacaciones, y seguimiento de jornada.

Acceso: **Laboral >> Empleados**

## Registro de Empleados

### Datos Personales

| Campo | Descripción |
|-------|-------------|
| **Código** | Identificador empleado |
| **Nombre** | Nombre completo |
| **Apellidos** | Apellidos |
| **DNI/NIF** | Documento identificación |
| **Email personal** | Correo electrónico |
| **Teléfono** | Contacto personal |
| **Dirección** | Domicilio |
| **Localidad** | Municipio |
| **C.P.** | Código postal |
| **Estado civil** | Soltero, casado, etc. |
| **Fecha nacimiento** | Edad laboral |

### Datos Laborales

| Campo | Descripción |
|-------|-------------|
| **Fecha contratación** | Inicio de relación laboral |
| **Fecha fin contrato** | Fin (si es temporal) |
| **Tipo contrato** | Indefinido, temporal, etc. |
| **Puesto** | Cargo/función |
| **Departamento** | Área asignada |
| **Responsable** | jefe directo |
| **Sección (Producción)** | Si aplica a manufacturación |
| **Máquinas** | Equipamiento que opera |

### Datos Fiscales/Seguridad Social

| Campo | Descripción |
|-------|-------------|
| **Seguridad Social** | Número de afiliación |
| **Cuenta bancaria** | IBAN para nómina |
| **Retención IRPF** | % de impuesto |
| **Cotización SS** | % de aportación |
| **Grupo profesional** | Categoría laboral |

## Estructura de Organización

```
Empresa
  ├── Departamentos
  │   ├── Ventas
  │   ├── Operaciones
  │   ├── RRHH
  │   └── Finanzas
  │
  └── Centros de Trabajo
      ├── Oficina Central
      └── Fábrica
```

## Contratos

Cada empleado tiene uno o varios contratos:

### Tipos de Contrato

- **Indefinido**: Sin fecha fin
- **Temporal**: Con fecha de expiración
- **Prácticas**: En período de formación
- **Aprendizaje**: Combinado con formación
- **Parcial**: Jornada reducida

### Información del Contrato

- Fecha inicio
- Fecha fin (si aplica)
- Jornada (horas/semana)
- Salario base
- Complementos (si aplica)
- Categoría profesional

## Historiales

### Experiencia Laboral Previa

Registrar empleos anteriores:
- Empresa anterior
- Puesto desempeñado
- Fechas de trabajo
- Motivo de salida

### Formación Académica

- Títulos obtenidos
- Especialidades
- Idiomas
- Certificaciones

### Historial en la Empresa

- Cambios de puesto
- Traslados de departamento
- Cambios de salario
- Ascensos

## Calendarios y Jornadas

### Calendario Laboral

Define días no laborables:

- **Festivos nacionales**: 1 enero, Navidad
- **Festivos regionales**: Propios de comunidad
- **Festivos locales**: De la empresa
- **Parones**: Agosto, Semana Santa

Acceso: **Laboral >> Calendarios**

### Turnos de Trabajo

Para empresas con producción 24/7:

| Turno | Horario | Empleados |
|-------|---------|-----------|
| **Mañana** | 6:00-14:00 | 10 personas |
| **Tarde** | 14:00-22:00 | 10 personas |
| **Noche** | 22:00-6:00 | 5 personas |

## Vacaciones y Ausencias

### Solicitud de Vacaciones

Acceso: **Laboral >> Vacaciones**

- **Días disponibles**: Según contrato (30 días anuales en España)
- **Días solicitados**: Período deseado
- **Aprobación**: Por responsable
- **Anotación**: En histórico

### Control de Ausencias

- **Vacaciones**: Programadas y aprobadas
- **Enfermedades**: Con justificante médico
- **Asuntos propios**: Descuento de salario
- **Permisos**: Según ley laboral

## Nómina y Remuneración

### Componentes de Nómina

**Base imponible:**
- Salario base
- Complementos
- Antigüedad
- Horas extras

**Retenciones:**
- IRPF (aportación estatal)
- Seguridad Social empleado
- Otros (póliza, seguros)

**Cotizaciones a cargo empresa:**
- Seguridad Social patronal (28-30%)
- Fondo de garantía salarial

### Procesamiento de Nómina

```
Laboral >> Procesamiento >> Nóminas
```

1. Establecer período (mes/año)
2. Importar empleados activos
3. Ingresar variaciones (extras, faltas, ausencias)
4. Generar nóminas
5. Contabilizar asientos
6. Exportar a banco (remesa)

### Remesa de Pago

Agrupa nóminas para transferencia:
- Genera archivo de transferencia
- A cuenta bancaria de cada empleado
- Con referencia de período

## Hojas de Gasto

Empleados registran gastos:

Acceso: **Laboral >> Hojas de Gasto**

**Tipos:**
- Viajes (transporte, hotel, comidas)
- Equipamiento (material de trabajo)
- Representación (almuerzos clientes)

**Flujo:**
1. Empleado registra gasto con comprobante
2. Responsable aprueba
3. Sistema contabiliza
4. Reembolso a empleado

## Integración con Producción

### Asignación a Operaciones

Si empleado trabaja en producción:
- Assign to section
- Máquinas habilitadas
- Coste/hora operario
- Coeficiente eficiencia

### Registro de Tiempo

- Entrada/salida cuadrante
- Horas asignadas a órdenes
- Ausencias/permisos
- Horas extras

## Evaluación de Desempeño

### Métricas Disponibles

- Asistencia (% presencia)
- Productividad (órdenes completadas)
- Calidad (rechazos/defectos)
- Puntualidad (retrasos)
- Antigüedad (años en empresa)

## Mejores Prácticas

✓ Datos de empleado siempre actualizados  
✓ Contratos bien documentados  
✓ Calendarios de fiestas definidos anualmente  
✓ Aprobación de vacaciones a tiempo  
✓ Revisión de nóminas antes de procesar  
✓ Documentación de cambios laborales  
✓ Cumplimiento de normativa laboral vigente  

## Legales y Compliance

### Obligaciones

- Afiliación SS en plazo
- Estancia de nóminas 4 años
- Comunicación cambios SS
- Retenciones correctas IRPF

### Reportes Obligatorios

- Declaración mensual SS
- Trimestral IRPF (modelo 111, 115)
- Anual (modelo 190)
- Diarias tesorería (movs. banco)

## Integración Contable

Cada nómina genera asientos:

```
Gasto de personal       12.000€  (débito)
    Seguridad Social       3.600€  (crédito)
    IRPF retenido          1.800€  (crédito)
    Banco (pago neto)      6.600€  (crédito)
```

Automatización completa desde módulo a contabilidad.

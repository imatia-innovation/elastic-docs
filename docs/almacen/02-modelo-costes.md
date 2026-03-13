# Modelo de Costes

## Descripción

El módulo de Modelo de Costes permite definir estrategias flexibles de valoración de inventarios. Elastic Business soporta tres tipos de modelos adaptados a diferentes necesidades empresariales.

## Acceso

En Elastic Business se accede mediante:

**Almacén >> Modelo de costes**

## Tipos de modelos de costes

### 1. Modelo Básico

El modelo básico establece un coste estándar para cada uno de los artículos durante un periodo de tiempo determinado.

**Características:**
- Responsabilidad del cliente mantenerlo y actualizarlo
- El coste estándar se calcula basándose en:
  - Coste de materia prima
  - Coste de mano de obra
  - Coste de maquinaria
- El coste de materia prima puede configurarse como:
  - Coste concreto fijo
  - Media de las entradas recibidas
  - Tarifa de un proveedor específico (actualizable automáticamente)

**Ideal para:** Empresas con estructura de costes simple y relativamente estable.

### 2. Modelo con Sobrecostes

Para empresas que necesitan un modelo más completo que contemple costes más allá de los básicos, el sistema permite configurar un modelo de costes con la posibilidad de añadir **sobrecostes configurables**.

**Características:**
- Incluye los tres costes básicos (materia prima, mano de obra, maquinaria)
- Permite añadir partidas de costes adicionales
- Los sobrecostes pueden ser:
  - **Partidas fijas:** coste constante por unidad
  - **Partidas variables:** porcentaje sobre materia prima, mano de obra o maquinaria
- Flexible y adaptable a diferentes estructuras de costes

**Ideal para:** Empresas con costes indirectos o gastos de transformación adicionales.

### 3. Modelo Personalizado

Adaptación completa del sistema de costes según necesidades específicas de la empresa.

## Configuración del modelo de costes

### Creación de un nuevo modelo

1. Ir a **Almacén >> Modelo de costes**
2. Añadir un nuevo registro
3. Cubrir los campos de la cabecera

### Campos de la cabecera

| Campo | Descripción |
|-------|-------------|
| **Descripción** | Nombre identificativo del modelo |
| **Fecha inicio** | Fecha de inicio de vigencia del modelo |
| **Fecha fin** | Fecha hasta la que tendrá validez el modelo |

### Pestañas del modelo

**Partidas:** Aquí se añaden los costes que necesitemos para el modelo con sobrecostes
- Definición de cada partida de coste
- Configuración como fija o variable
- Base de cálculo (si es variable)

**Familias:** Se muestran todas las familias que usan este modelo de costes
- Permite activar el modelo como predeterminado

**Artículos:** Se muestran todos los artículos que usan este modelo de costes

## Aplicación del modelo

### A nivel de familia

Los modelos de costes se pueden asignar a nivel de **Familia de artículos**:

1. Ir a **Almacén >> Familia de artículos >> Activas**
2. Entrar en los detalles de la familia
3. Asignar el modelo de costes
4. Marcar como "Activo" para usar por defecto

### A nivel de artículo

También se puede aplicar directamente a artículos individuales dentro de una familia.

## Consideraciones

- Se pueden añadir múltiples modelos de costes a una misma familia
- Un artículo puede tener asignado un modelo específico diferentes al de su familia
- Es responsabilidad de la empresa mantener actualizado el modelo de costes básico

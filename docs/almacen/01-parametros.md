# Parámetros

## Descripción

Los parámetros se definen como identificadores que permiten generar configuraciones únicas en los artículos. La creación de artículos mediante parámetros sirve para generar automáticamente el código interno y descripción del artículo.

## Acceso

En Elastic Business se accede mediante la siguiente ruta:

**Almacén >> Parámetros**

Los parámetros se establecen por **FAMILIAS de artículos**.

## Configuración básica

Cada parámetro está formado por una serie de valores. Antes de añadir valores, primero hay que definir la configuración básica del parámetro.

En la cabecera del parámetro se muestran los siguientes campos:

### Campos principales

| Campo | Descripción |
|-------|-------------|
| **Código** | Codificación identificativa del parámetro |
| **Acrónimo** | Se utiliza como abreviatura de la descripción |
| **Descripción** | Descripción completa del parámetro |
| **Unidades** | Permite asociar una unidad de medida al parámetro |
| **Tipo** | Define cómo se comporta el parámetro |

## Tipos de parámetros

### Tipo Explícito
- El parámetro no está formado por una lista predefinida de valores
- Los valores son libres durante la creación del artículo
- Los valores solo pueden ser numéricos
- Útil para especificaciones variables (dimensiones, pesos, etc.)

### Tipo Implícito
- Uno de los valores del parámetro forma parte de la configuración del artículo
- Se habilitan los botones de inserción para añadir valores predefinidos
- Útil para características fijas de la familia (colores, materiales, etc.)

## Tabla de valores de parámetros

Cuando el parámetro es de tipo implícito, se pueden definir los valores posibles. Cada valor tiene tres columnas:

| Columna | Descripción |
|---------|-------------|
| **Valor** | Indica el valor del parámetro; este aparecerá en el código del artículo si así se configura |
| **Descripción** | Descripción del valor; aparecerá en la descripción del artículo |
| **Acrónimo** | Si el valor tiene acrónimo, este se usará en lugar de la descripción en el código |

## Grupos de parámetros

Se permite configurar **grupos de parámetros**, que es útil cuando existe un uso compartido de valores. Esto agiliza la creación de parámetros nuevos reutilizando configuraciones anteriores.

## Proceso de trabajo

1. Acceder a Almacén >> Parámetros
2. Seleccionar la familia donde se crearán los parámetros
3. Crear nuevo parámetro con código, acrónimo y descripción
4. Definir el tipo (Explícito o Implícito)
5. Si es implícito, añadir los valores posibles
6. Guardar la configuración

## Relación con familias de artículos

Los parámetros configurados se utilizan posteriormente en la definición de **Familias de artículos** para determinar cómo se generarán automáticamente los códigos de los artículos que pertenezcan a esa familia.

# Familias de Artículos

## Descripción

Las Familias de Artículos son conjuntos de productos que comparten características comunes. Permiten aplicar configuraciones de manera masiva a todos los artículos de una familia, facilitando la gestión centralizada de grupos de productos.

## Acceso

En Elastic Business se accede mediante:

**Almacén >> Familia de artículos**

## Concepto de familia

Una familia es una agrupación lógica de artículos que comparten:
- **Características técnicas similares**
- **Procesos de fabricación comunes**
- **Modelos de costes aplicables**
- **Parámetros de configuración**
- **Políticas de valoración**

## Configuración de familias

### Información básica de la familia

- **Código:** Identificador único de la familia
- **Descripción:** Nombre descriptivo de la familia
- **Tipo de familia:** Categoría o clasificación
- **Estado:** Activa/Inactiva

### Asociación de parámetros

Cada familia puede tener asociados parámetros que determinan:
- Cómo se generan automáticamente los códigos de los artículos
- Qué características variables pueden tener los productos

**Ejemplo:** Una familia "Tuberías de PVC" podría tener parámetros para:
- Diámetro (20mm, 25mm, 32mm, etc.)
- Presión (PN10, PN16, PN25)

### Asignación de modelo de costes

Cada familia debe tener asignado un modelo de costes que define:
- Cómo se valoran los artículos en inventario
- Qué estructura de costes se utiliza

Los artículos individuales pueden sobrescribir el modelo de la familia si lo requieren.

## Uso de familias

### Creación de artículos

Cuando creas un artículo:
1. Seleccionas la familia a la que pertenece
2. El sistema aplica automáticamente la configuración de esa familia
3. Los parámetros de la familia se usan para generar el código

### Gestión masiva

Las familias permiten:
- Cambiar la configuración común a múltiples artículos
- Aplicar nuevos parámetros a todos los artículos de una familia
- Modificar el modelo de costes para toda una familia

### Organización

Las familias facilitan:
- La búsqueda y clasificación de artículos
- La generación de reportes por categoría de producto
- La organización de procesos de fabricación
- La aplicación de políticas comunes

## Relación con otros elementos

```
Familia de Artículos
    ↓
    ├─→ Parámetros (generación de códigos)
    ├─→ Modelo de Costes (valoración)
    ├─→ Artículos (múltiples)
    └─→ Configuración compartida
```

## Beneficios de usar familias

✓ **Eficiencia:** Configuración masiva de múltiples artículos  
✓ **Coherencia:** Asegura que artículos similares se traten de igual forma  
✓ **Mantenibilidad:** Cambios en la familia se propagan a sus artículos  
✓ **Escalabilidad:** Facilita el crecimiento del catálogo de productos  
✓ **Organización:** Estructura clara del inventario  

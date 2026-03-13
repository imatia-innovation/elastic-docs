---
sidebar_position: 5
---

# Características de Markdown

Docusaurus soporta **Markdown estándar** y varias **características adicionales** que mejoran la presentación del contenido.

## Front Matter

Los documentos Markdown tienen metadatos al principio llamados **Front Matter**:

```text title="mi-doc.md"
// highlight-start
---
id: mi-id-doc
title: Título del documento
description: Descripción del documento
slug: /mi-url-personalizada
---
// highlight-end

## Encabezado Markdown

Texto Markdown con [enlaces](./hola.md)
```

El front matter debe estar al inicio del archivo, delimitado por `---`.

## Enlaces

Los enlaces Markdown regulares se soportan usando rutas URL o rutas relativas a archivos.

```md
Veamos cómo [Crear una página](/docs/guia-docusaurus/02-crear-pagina).
```

```md
Veamos cómo [Crear una página](./02-crear-pagina.md).
```

**Resultado:** Veamos cómo [Crear una página](./02-crear-pagina.md).

## Imágenes

Las imágenes Markdown regulares se soportan completamente.

Puedes usar rutas absolutas para referenciar imágenes en la carpeta `static`:

```md
![Logo de Docusaurus](/img/docusaurus.png)
```

También puedes referenciar imágenes relativas al archivo actual, lo que es especialmente útil para colocar imágenes cerca de los archivos Markdown que las usan:

```md
![Logo de Docusaurus](./img/docusaurus.png)
```

## Bloques de Código

Los bloques de código Markdown se soportan con **resaltado de sintaxis** automático.

````md
```jsx title="src/componentes/HolaMundo.js"
function HolaMundo() {
  return <h1>¡Hola, Mundo!</h1>;
}
```
````

```jsx title="src/componentes/HolaMundo.js"
function HolaMundo() {
  return <h1>¡Hola, Mundo!</h1>;
}
```

### Opciones de bloques de código

| Opción | Descripción |
|--------|-------------|
| `title` | Título que aparece en la esquina del código |
| `language` | Lenguaje de programación para resaltado |
| `showLineNumbers` | Mostrar números de línea |
| `highlight` | Resaltar líneas específicas |

## Admiciones (Callouts)

Docusaurus tiene sintaxis especial para crear adiciones y llamadas de atención:

```md
:::tip Mi consejo

Utiliza esta característica increíble

:::

:::info Información

Nota informativa importante

:::

:::warning Advertencia

Ten cuidado con esto

:::

:::danger Peligro

Esta acción es peligrosa

:::
```

:::tip Mi consejo

Utiliza esta característica increíble

:::

:::info Información

Nota informativa importante

:::

:::warning Advertencia

Ten cuidado con esto

:::

:::danger Peligro

Esta acción es peligrosa

:::

## Tablas

Las tablas Markdown se soportan completamente:

```md
| Izquierda | Centro | Derecha |
|-----------|--------|---------|
| a         | b      | c       |
| d         | e      | f       |
```

| Izquierda | Centro | Derecha |
|-----------|--------|---------|
| a         | b      | c       |
| d         | e      | f       |

## Listas

### Listas numeradas

```md
1. Primer elemento
2. Segundo elemento
3. Tercer elemento
```

1. Primer elemento
2. Segundo elemento
3. Tercer elemento

### Listas sin orden

```md
- Elemento A
- Elemento B
- Elemento C
```

- Elemento A
- Elemento B
- Elemento C

## Énfasis

```md
**Texto en negrita**
*Texto en cursiva*
***Texto en negrita y cursiva***
~~Texto tachado~~
```

**Texto en negrita**  
*Texto en cursiva*  
***Texto en negrita y cursiva***  
~~Texto tachado~~

## Encabezados

```md
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

Los encabezados generan automáticamente IDs para enlaces directos.

## Citas

```md
> Esta es una cita
> 
> Puede abarcar múltiples líneas
> 
> — Persona Famosa
```

> Esta es una cita
> 
> Puede abarcar múltiples líneas
> 
> — Persona Famosa

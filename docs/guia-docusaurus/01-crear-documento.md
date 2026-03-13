---
sidebar_position: 2
---

# Crear Documentos

Los **documentos** son grupos de páginas conectadas a través de:

- Un **panel lateral** automático
- Navegación de **página anterior/siguiente**
- Soporte de **versionado**

## Crear tu primer documento

Crea un archivo Markdown en `docs/hola.md`:

```md title="docs/hola.md"
# Hola

¡Este es mi **primer documento en Docusaurus**!
```

Tu nuevo documento ahora está disponible en [http://localhost:3000/docs/hola](http://localhost:3000/docs/hola).

## Configurar el panel lateral

Docusaurus **crea automáticamente un panel lateral** a partir de la carpeta `docs`.

Añade metadatos para personalizar la etiqueta y posición en el panel lateral:

```md title="docs/hola.md" {1-4}
---
sidebar_label: '¡Hola!'
sidebar_position: 3
---

# Hola

¡Este es mi **primer documento en Docusaurus**!
```

## Crear sidebar explícitamente

También es posible crear tu panel lateral de forma explícita en `sidebars.js`:

```js title="sidebars.js"
export default {
  tutorialSidebar: [
    'intro',
    // highlight-next-line
    'hola',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/crear-documento'],
    },
  ],
};
```

## Metadatos de documento

Puedes personalizar diversos aspectos del documento usando metadatos en el **front matter**:

| Campo | Descripción |
|-------|-------------|
| `sidebar_label` | Etiqueta que aparece en el panel lateral |
| `sidebar_position` | Posición en el panel lateral (número) |
| `id` | Identificador único del documento |
| `title` | Título del documento |
| `description` | Descripción meta del documento |
| `slug` | URL personalizada del documento |

## Organización de documentos

Docosaurus soporta la organización jerárquica de documentos usando carpetas:

```
docs/
├── intro.md
├── guia/
│   ├── introduccion.md
│   ├── conceptos.md
│   └── avanzado.md
└── referencias/
    └── api.md
```

Los documentos en subcarpetas aparecerán automáticamente como categorías en el panel lateral.

## Navegación entre documentos

Puedes crear enlaces entre documentos usando rutas relativas o absolutas:

```md
Ver [Crear una página](../02-crear-pagina.md) para más información.
```

El sistema automáticamente gestionará la navegación anterior/siguiente basándose en el sidebar.

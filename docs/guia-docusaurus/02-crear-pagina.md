---
sidebar_position: 3
---

# Crear Páginas

Añade **archivos Markdown o React** a la carpeta `src/pages` para crear **páginas autónomas**:

- `src/pages/index.js` → `localhost:3000/`
- `src/pages/foo.md` → `localhost:3000/foo`
- `src/pages/foo/barra.js` → `localhost:3000/foo/barra`

Las páginas no aparecen en el panel lateral y son contenidos independientes de la documentación principal.

## Crear tu primera página React

Crea un archivo en `src/pages/mi-pagina-react.js`:

```jsx title="src/pages/mi-pagina-react.js"
import React from 'react';
import Layout from '@theme/Layout';

export default function MiPaginaReact() {
  return (
    <Layout>
      <h1>Mi página React</h1>
      <p>Esta es una página React</p>
    </Layout>
  );
}
```

Tu nueva página ahora está disponible en [http://localhost:3000/mi-pagina-react](http://localhost:3000/mi-pagina-react).

## Crear tu primera página Markdown

Crea un archivo en `src/pages/mi-pagina-markdown.md`:

```mdx title="src/pages/mi-pagina-markdown.md"
# Mi página Markdown

Esta es una página Markdown
```

Tu nueva página ahora está disponible en [http://localhost:3000/mi-pagina-markdown](http://localhost:3000/mi-pagina-markdown).

## Componente Layout

El componente `Layout` proporciona la estructura completa de página con:
- Barra de navegación
- Pie de página
- Estilos consistentes con el resto del sitio

### Uso en React

```jsx
import Layout from '@theme/Layout';

export default function MiPagina() {
  return (
    <Layout title="Mi Página" description="Descripción de mi página">
      <h1>Contenido</h1>
    </Layout>
  );
}
```

## Diferencia entre Documentos y Páginas

| Aspecto | Documentos | Páginas |
|--------|-----------|--------|
| **Ubicación** | `docs/` | `src/pages/` |
| **Sidebar** | Sí, automático | No |
| **Navegación** | Anterior/Siguiente | Manual |
| **Versionado** | Soportado | No |
| **Uso** | Documentación estructurada | Contenido personalizado |

Usa **Documentos** para contenido de referencia y estructura jerárquica.  
Usa **Páginas** para contenido único como landing pages, políticas, etc.

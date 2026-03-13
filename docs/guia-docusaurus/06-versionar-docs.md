---
sidebar_position: 7
---

# Versionado de Documentación

Docusaurus puede gestionar **múltiples versiones** de tu documentación. Esto es especialmente útil para:

- Software con varias versiones activas
- Documentación de API que evoluciona
- Cambios significativos entre versiones

## Crear una versión de documentación

Libera la versión 1.0 de tu proyecto:

```bash
npm run docusaurus docs:version 1.0
```

Varios cambios suceden automáticamente:

1. La carpeta `docs` se copia en `versioned_docs/version-1.0`
2. Se crea un archivo `versions.json`
3. Tu documentación ahora tiene **2 versiones**

### Resultado

- `1.0` en `http://localhost:3000/docs/` - Documentación de la versión 1.0
- `current` en `http://localhost:3000/docs/next/` - Documentación en desarrollo (próxima versión)

## Archivo versions.json

Este archivo controla qué versiones están disponibles:

```json title="versions.json"
[
  "1.0",
  "0.9",
  "0.8"
]
```

Las versiones se mostrarán en el menú desplegable en orden descendente.

## Añadir menú desplegable de versiones

Modifica el archivo `docusaurus.config.js` para mostrar un menú de selección de versiones:

```js title="docusaurus.config.js"
export default {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'docsVersionDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

El menú desplegable aparecerá en tu barra de navegación.

## Editar una versión existente

Es posible editar la documentación versionada en su carpeta respectiva:

- `versioned_docs/version-1.0/hola.md` actualiza `http://localhost:3000/docs/hola`
- `docs/hola.md` actualiza `http://localhost:3000/docs/next/hola`

### Estructura de carpetas

```
versioned_docs/
├── version-1.0/
│   ├── intro.md
│   ├── guia/
│   │   ├── introduccion.md
│   │   └── avanzado.md
│   └── ...
├── version-0.9/
│   ├── intro.md
│   └── ...
└── version-0.8/
    └── ...

docs/  (versión actual/development)
├── intro.md
├── guia/
│   ├── introduccion.md
│   └── avanzado.md
└── ...
```

## Estructura de versioned_docs.sidebars.js

Para diferentes sidebars por versión, crea:

```js title="versioned_docs/version-1.0/sidebars.js"
export default {
  tutorialSidebar: [
    'intro',
    'getting-started',
    'advanced-usage',
  ],
};
```

## Proceso recomendado

1. **Desarrollo normal** en la rama `main` en la carpeta `docs`
2. **Releasing** - Cuando estés listo para liberar:
   ```bash
   npm run docusaurus docs:version X.Y.Z
   ```
3. **Mantenimiento** - Edita `versioned_docs/` solo para correcciones críticas
4. **Nuevas características** - Vuelve a la carpeta `docs` para la próxima versión

## Indicadores de versión

Puedes añadir indicadores visuales en el fronter matter:

```md
---
sidebar_position: 1
version: 1.0
versioned_at: 2024-01-15
---
```

## NOTAS sobre versionado

:::tip Buena práctica

Mantén `docs/` únicamente para la versión en desarrollo. Cuando liberes, siempre crea una versión usando el comando.

:::

:::warning Importante

Las versiones antiguas normalmente no deben actualizarse. Solo edita versiones antiguas para correcciones de seguridad o errores críticos.

:::

:::info Alternativa

Si no necesitas múltiples versiones, puedes ignorar completamente esta funcionalidad y documentar solo la versión actual.

:::

---
sidebar_position: 8
---

# Traducir tu Sitio

Docusaurus soporta **internacionalización (i18n)** integrada, permitiendo crear versiones en múltiples idiomas de tu sitio.

## Configurar i18n

Modifica `docusaurus.config.js` para añadir soporte de idiomas.

Ejemplo para añadir soporte para **Francés** además de Inglés:

```js title="docusaurus.config.js"
export default {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
  },
};
```

### Parámetros

| Parámetro | Descripción |
|-----------|-------------|
| `defaultLocale` | Idioma predeterminado del sitio |
| `locales` | Array de códigos de idioma soportados |

## Traducir un documento

Para traducir `docs/intro.md` al francés:

### Paso 1: Copiar el archivo

```bash
mkdir -p i18n/fr/docusaurus-plugin-content-docs/current/

cp docs/intro.md i18n/fr/docusaurus-plugin-content-docs/current/intro.md
```

### Paso 2: Editar la traducción

Edita `i18n/fr/docusaurus-plugin-content-docs/current/intro.md` con la versión en francés.

### Estructura de carpetas de traducción

```
i18n/
├── fr/  (Francés)
│   └── docusaurus-plugin-content-docs/
│       └── current/
│           ├── intro.md
│           ├── guia/
│           │   └── ...
│           └── sidebars.js
├── es/  (Español)
│   └── docusaurus-plugin-content-docs/
│       └── current/
│           └── ...
└── de/  (Alemán)
    └── docusaurus-plugin-content-docs/
        └── ...
```

## Probar tu sitio localizado

Inicia tu sitio en el idioma francés:

```bash
npm run start -- --locale fr
```

Tu sitio localizado está accesible en [http://localhost:3000/fr/](http://localhost:3000/fr/) y la página de inicio está traducida.

:::caution Limitación

En desarrollo, solo puedes usar un idioma a la vez. Para ver todos los idiomas juntos, debes compilar.

:::

## Añadir menú desplegable de idiomas

Para permitir navegación entre idiomas, añade un menú desplegable.

Modifica `docusaurus.config.js`:

```js title="docusaurus.config.js"
export default {
  themeConfig: {
    navbar: {
      items: [
        // highlight-start
        {
          type: 'localeDropdown',
        },
        // highlight-end
      ],
    },
  },
};
```

El menú desplegable de idiomas ahora aparecerá en tu barra de navegación.

## Compilar tu sitio localizado

Compila para un idioma específico:

```bash
npm run build -- --locale fr
```

O compila tu sitio para incluir **todos los idiomas** a la vez:

```bash
npm run build
```

## Traducir otros elementos

Además de documentos, también puedes traducir:

### Etiquetas de barra de navegación

```js title="docusaurus.config.js"
export default {
  themeConfig: {
    navbar: {
      items: [
        {
          type: 'doc',
          docId: 'intro',
          label: 'Documentos',  // Para el idioma por defecto
        },
      ],
    },
  },
};
```

### Blog

```bash
mkdir -p i18n/fr/docusaurus-plugin-content-blog/
cp -r blog/* i18n/fr/docusaurus-plugin-content-blog/
```

Edita las entradas de blog traducidas.

### Páginas personalizadas

```bash
mkdir -p i18n/fr/docusaurus-plugin-content-pages/
cp -r src/pages/* i18n/fr/docusaurus-plugin-content-pages/
```

## Códigos de idioma ISO

Algunos códigos comunes:

| Idioma | Código |
|--------|--------|
| Inglés | `en` |
| Español | `es` |
| Francés | `fr` |
| Alemán | `de` |
| Italiano | `it` |
| Portugués | `pt` |
| Ruso | `ru` |
| Chino Simplificado | `zh` |
| Japonés | `ja` |

## Flujo de trabajo recomendado

1. **Escribe en idioma predeterminado** - Desarrolla el contenido en tu idioma principal
2. **Libera versión** - Cuando el contenido esté listo, prepara la traducción
3. **Traduce secciones** - Copia archivos a carpetas i18n y tradúcelos
4. **Prueba localmente** - Verifica cada idioma funciona correctamente
5. **Compila todo** - Genera el sitio con todos los idiomas
6. **Mantén sincronizado** - Cuando actualices contenido, actualiza todas las traducciones

## Notas sobre internacionalización

:::info Importante

La traducción es responsabilidad tuya. Docusaurus solo gestiona la estructura y enrutamiento. Considera usar herramientas como:
- Google Translate (para borrador inicial)
- Herramientas profesionales de traducción
- Comunidad de contribuidores

:::

:::tip Consejo

No necesitas tener todas las páginas traducidas. Puedes traducir gradualmente, comenzando con las más importantes.

:::

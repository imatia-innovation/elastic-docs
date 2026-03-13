---
sidebar_position: 4
---

# Crear Entradas de Blog

Docusaurus crea automáticamente:
- Una **página para cada entrada de blog**
- Una **página de índice** del blog
- Un **sistema de etiquetas**
- Un feed **RSS**

## Crear tu primera entrada

Crea un archivo en `blog/2025-03-11-saludos.md`:

```md title="blog/2025-03-11-saludos.md"
---
slug: saludos
title: ¡Saludos!
authors:
  - name: Juan García
    title: Autor principal
    url: https://github.com/juangarcia
    image_url: https://github.com/juangarcia.png
  - name: María López
    title: Colaborador
    url: https://github.com/marialopez
    image_url: https://github.com/marialopez.png
tags: [saludos, bienvenida]
---

¡Felicitaciones, has creado tu primera entrada de blog!

Siéntete libre de jugar y editar esta entrada tanto como quieras.
```

Tu nueva entrada de blog ahora está disponible en [http://localhost:3000/blog/saludos](http://localhost:3000/blog/saludos).

## Estructura de metadatos

Cada entrada de blog debe incluir metadatos al principio del archivo:

| Campo | Descripción |
|-------|-------------|
| `slug` | URL de la entrada (sin fecha) |
| `title` | Título de la entrada |
| `authors` | Lista de autores con información |
| `tags` | Etiquetas para categorización |
| `date` | Fecha de publicación (opcional, se extrae del nombre) |

### Autores

Los autores permiten especificar:
```md
authors:
  - name: Nombre del autor
    title: Posición o rol
    url: Enlace al perfil
    image_url: URL de la foto de perfil
```

## Formato de nombre de archivo

El nombre del archivo determina la fecha de publicación:

```
blog/
├── 2025-01-15-primera-entrada.md     # 15 de enero de 2025
├── 2025-02-28-segunda-entrada.md     # 28 de febrero de 2025
└── 2025-03-11-tercera-entrada.md     # 11 de marzo de 2025
```

## Sistema de etiquetas

Las **etiquetas** permiten categorizar entradas:

```md
tags: [javascript, docusaurus, tutorial]
```

Docusaurus genera automáticamente:
- Página de índice de etiquetas
- Página individual para cada etiqueta
- Enlaces a todas las entradas con esa etiqueta

## Feed RSS

Docusaurus genera automáticamente un feed RSS en:
```
http://localhost:3000/blog/rss.xml
```

Este feed se actualiza automáticamente con cada nueva entrada.

## Página principal del blog

La página principal del blog en `http://localhost:3000/blog/` muestra:
- Últimas entradas
- Paginación
- Categorías y etiquetas
- Opción de suscripción al RSS

## Consejos para escribir entradas

✓ **Sé consistente** con las fechas en los nombres de archivo  
✓ **Usa etiquetas relevantes** para mejor descubribilidad  
✓ **Incluye autores** para attribution  
✓ **Escribe slug amigables** (sin espacios, usando guiones)  
✓ **Aprovecha el Markdown** para formato atractivo

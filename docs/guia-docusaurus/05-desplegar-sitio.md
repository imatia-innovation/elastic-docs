---
sidebar_position: 6
---

# Desplegar tu Sitio

Docusaurus es un **generador de sitios estáticos** (también llamado **[Jamstack](https://jamstack.org/)**).

Construye tu sitio como archivos **HTML, JavaScript y CSS estáticos** simples, listos para desplegarse casi en cualquier lugar.

## Compilar tu sitio

Compila tu sitio **para producción**:

```bash
npm run build
```

Los archivos estáticos se generan en la carpeta `build`.

## Probar localmente antes de desplegar

Prueba tu compilación de producción localmente:

```bash
npm run serve
```

La carpeta `build` ahora se sirve en [http://localhost:3000/](http://localhost:3000/).

## Desplegar tu sitio

Puedes desplegar la carpeta `build` **casi en cualquier lugar** fácilmente, **gratis** o con muy poco coste.

Algunas opciones populares:

### Hosting estático

- **GitHub Pages** - Gratis cuando se configura desde GitHub
- **Netlify** - Hosting gratuito con despliegue automático desde Git
- **Vercel** - Plataforma moderna para sitios estáticos y serverless
- **AWS Amplify** - Solución completa de AWS
- **Firebase Hosting** - Hosting de Google
- **Azure Static Web Apps** - Solución de Microsoft

### Servidores tradicionales

También puedes desplegar en cualquier servidor web tradicional (Apache, Nginx, etc.) copiando el contenido de la carpeta `build`.

## Guía de despliegue

Para instrucciones detalladas sobre cómo desplegar en tu plataforma específica, consulta:

**[Docusaurus Deployment Guide](https://docusaurus.io/docs/deployment)** 

Incluye pasos específicos para:
- GitHub Pages
- Netlify
- Vercel
- Heroku
- Y muchas más...

## Optimizaciones para producción

Docusaurus automáticamente optimiza tu sitio para producción con:

✓ **Minificación** de HTML, CSS y JavaScript  
✓ **Code splitting** para cargas más rápidas  
✓ **Lazy loading** de imágenes y componentes  
✓ **Preload** de recursos críticos  
✓ **Compresión** de activos  

## Monitoreo después del despliegue

Una vez en producción, considera:

- **Monitoreo de errores** - Usar herramientas como Sentry
- **Analytics** - Integrar Google Analytics u alternativa
- **Performance** - Monitorear Core Web Vitals
- **Backups** - Si usas base de datos o contenido dinámico
- **CDN** - Para servir contenido más rápido globalmente

## CI/CD Automático

La mayoría de plataformas modernas soportan **despliegue automático** cuando haces push a tu repositorio:

```yaml
# Ejemplo con GitHub Actions
name: Deploy
on: [push]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - run: npm run deploy
```

Esto permite actualizar tu sitio automáticamente cada vez que haces cambios.

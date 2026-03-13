import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

const config: Config = {
 title: "Wiki Elastic Business",
 tagline:
  "Documentación profesional del ERP Elastic Business - Guías completas, integrales y organizadas por módulo funcional",
 favicon: "img/favicon.ico",

 future: {
  v4: true,
 },

 url: "https://imatia-innovation.github.io",
 baseUrl: "/elastic-docs/",

 organizationName: "Imatia Innovation S.L.",
 projectName: "elastic-docs",

 onBrokenLinks: "throw",
 onBrokenMarkdownLinks: "warn",

 i18n: {
  defaultLocale: "es",
  locales: ["es"],
 },

 presets: [
  [
   "classic",
   {
    docs: {
     sidebarPath: "./sidebars.ts",
     showLastUpdateAuthor: false,
     showLastUpdateTime: false,
    },
    blog: false,
    theme: {
     customCss: "./src/css/custom.css",
    },
   } satisfies Preset.Options,
  ],
 ],

 themes: [
  [
   require.resolve("@easyops-cn/docusaurus-search-local"),
   {
    hashed: true,
    language: ["es"],
    indexDocs: true,
    indexBlog: false,
    indexPages: true,
    docsRouteBasePath: "/docs",
    highlightSearchTermsOnTargetPage: true,
    explicitSearchResultPath: true,
   },
  ],
 ],

 themeConfig: {
  image: "img/docusaurus-social-card.jpg",
  colorMode: {
   defaultMode: "light",
   respectPrefersColorScheme: true,
   disableSwitch: false,
  },
  navbar: {
   hideOnScroll: false,
   title: "Elastic Business",
   logo: {
    alt: "Elastic Business Logo",
    src: "img/logo.svg",
    width: 32,
    height: 32,
   },
   items: [
    {
     type: "docSidebar",
     sidebarId: "tutorialSidebar",
     position: "left",
     label: "📚 Documentación",
    },
   ],
  },
  footer: {
   style: "dark",
   links: [
    {
     title: "Módulos Principales",
     items: [
      {
       label: "Almacén",
       to: "/docs/almacen/intro",
      },
      {
       label: "Ventas",
       to: "/docs/ventas/intro",
      },
      {
       label: "Compras",
       to: "/docs/compras/intro",
      },
      {
       label: "Finanzas",
       to: "/docs/finanzas/intro",
      },
     ],
    },
    {
     title: "Gestión",
     items: [
      {
       label: "CRM",
       to: "/docs/crm/intro",
      },
      {
       label: "Laboral",
       to: "/docs/laboral/intro",
      },
      {
       label: "Producción",
       to: "/docs/produccion/intro",
      },
      {
       label: "Trazabilidad",
       to: "/docs/trazabilidad/intro",
      },
     ],
    },
    {
     title: "Recursos",
     items: [
      {
       label: "Guía de Uso",
       to: "/docs/guia_de_uso/intro",
      },
      {
       label: "Programación",
       to: "/docs/programacion/intro",
      },
      {
       label: "Calidad",
       to: "/docs/calidad/intro",
      },
      {
       label: "Inicio",
       to: "/docs/intro",
      },
     ],
    },
   ],
   copyright: `Copyright © ${new Date().getFullYear()} Elastic Business - Documentación Profesional del ERP`,
  },
  prism: {
   theme: prismThemes.github,
   darkTheme: prismThemes.dracula,
  },
  docs: {
   sidebar: {
    hideable: true,
    autoCollapseCategories: false,
   },
  },
 } satisfies Preset.ThemeConfig,
};

export default config;

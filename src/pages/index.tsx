import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';

import styles from './index.module.css';

/**
 * Module card configuration - displays the 12 main ERP modules
 */
const MODULE_CARDS: Array<{icon: string; title: string; description: string; link: string}> = [
  {
    icon: '📦',
    title: 'Almacén',
    description: 'Gestión de inventario, stock de seguridad, familias de artículos y control de costes.',
    link: '/docs/almacen/intro',
  },
  {
    icon: '🛍️',
    title: 'Ventas',
    description: 'Gestión de clientes, presupuestos, pedidos de venta y facturación.',
    link: '/docs/ventas/intro',
  },
  {
    icon: '🏪',
    title: 'Compras',
    description: 'Gestión de proveedores, órdenes de compra, recepción e integración logística.',
    link: '/docs/compras/intro',
  },
  {
    icon: '👥',
    title: 'CRM',
    description: 'Gestión integral de clientes, datos comerciales y relaciones empresariales.',
    link: '/docs/crm/intro',
  },
  {
    icon: '💰',
    title: 'Finanzas',
    description: 'Plan general de cuentas, dimensiones analíticas y gestión financiera.',
    link: '/docs/finanzas/intro',
  },
  {
    icon: '👨‍💼',
    title: 'Laboral',
    description: 'Gestión de empleados, nóminas, contratos y vacaciones.',
    link: '/docs/laboral/intro',
  },
  {
    icon: '🏭',
    title: 'Producción',
    description: 'Gestión de estructuras de fabricación, máquinas y operaciones productivas.',
    link: '/docs/produccion/intro',
  },
  {
    icon: '✓',
    title: 'Calidad',
    description: 'Control de calidad, no conformidades y acciones correctivas.',
    link: '/docs/calidad/intro',
  },
  {
    icon: '🔍',
    title: 'Trazabilidad',
    description: 'Sistema de trazabilidad, lotes y gestión de trazas.',
    link: '/docs/trazabilidad/intro',
  },
  {
    icon: '📖',
    title: 'Guía de Uso',
    description: 'Instalación, configuración y guía de uso del sistema.',
    link: '/docs/guia_de_uso/intro',
  },
  {
    icon: '⚙️',
    title: 'Programación',
    description: 'API REST, webhooks, extensiones y desarrollo personalizado.',
    link: '/docs/programacion/intro',
  },
  {
    icon: '📚',
    title: 'Resources',
    description: 'Documentación adicional, ejemplos y recursos técnicos.',
    link: '/docs/intro',
  },
];

/**
 * Homepage Header - Hero section with gradient background
 */
function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.heroBanner}>
      <div className={styles.heroContentWrapper}>
        <div className="container">
          <Heading as="h1" className={styles.heroTitle}>
            {siteConfig.title}
          </Heading>
          <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className="button button--primary button--lg"
              to="/docs/intro">
              📚 Ir a la Documentación
            </Link>
            <Link
              className="button button--primary button--lg"
              to="/docs/guia_de_uso/intro">
              🚀 Guía de Instalación
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

/**
 * Feature card component for displaying module information
 */
function FeatureCard({
  icon,
  title,
  description,
  link,
}: {
  icon: string;
  title: string;
  description: string;
  link: string;
}) {
  return (
    <Link to={link} className={styles.featureCard}>
      <div className={styles.featureIcon}>{icon}</div>
      <Heading as="h3" className={styles.featureTitle}>
        {title}
      </Heading>
      <p className={styles.featureDescription}>{description}</p>
      <span className={styles.featureLink}>
        Explorar módulo →
      </span>
    </Link>
  );
}







/**
 * Main homepage component
 */
export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title} - Documentación Profesional del ERP`}
      description="Documentación completa, profesional y moderna de Elastic Business. Accede a todos los módulos del ERP: Almacén, Ventas, Compras, CRM, Finanzas, Laboral, Producción, Trazabilidad, Calidad y más.">
      <HomepageHeader />
      <main>
        <section className={styles.modulesSection}>
          <div className="container">
            <div className={styles.modulesHeader}>
              <Heading as="h2">Módulos Principales</Heading>
              <p className={styles.modulesSubtitle}>
                Accede a la documentación completa de cada módulo funcional del ERP Elastic Business
              </p>
            </div>
            <div className={styles.featuresGrid}>
              {MODULE_CARDS.map((card, idx) => (
                <FeatureCard key={idx} {...card} />
              ))}
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

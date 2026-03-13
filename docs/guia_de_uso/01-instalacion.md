---
sidebar_position: 1
---

# Instalación y Configuración

## Requisitos del Sistema

### Hardware

| Componente | Mínimo | Recomendado |
|-----------|--------|------------|
| **CPU** | Intel i5 / AMD Ryzen 5 | Intel i7 / AMD Ryzen 7 |
| **RAM** | 8 GB | 16+ GB |
| **Disco** | 250 GB SSD | 500+ GB SSD |
| **Pantalla** | 1366x768 | 1920x1080 |

### Software

- **Java JDK**: 11 LTS o superior
- **Base datos**: SQL Server 2016+
- **Navegador**: Chrome 90+, Firefox 88+, Edge 90+
- **Sistema**: Windows Server 2016+ o Linux

## Descarga e Instalación

### 1. Descargar Componentes

Acceso: www.imatia.com (área cliente)

**Componentes:**
- Java JDK
- SQL Server Express o Full
- Elastic Business (archivo WAR)
- Tomcat 9+

### 2. Instalar Java JDK

```bash
# Windows
1. Descargar JDK desde Oracle
2. Ejecutar instalador
3. Establecer variable JAVA_HOME
   Sistema > Variables entorno > Nueva
   Variable: JAVA_HOME
   Valor: C:\Program Files\Java\jdk-11

# Verificar instalación
java -version
javac -version
```

### 3. Instalar SQL Server

```
1. Descargar SQL Server Express (o Full)
2. Ejecutar instalación
3. Crear base de datos "elastic_business"
4. Crear usuario con permisos
   Usuario: elastic_user
   Contraseña: [segura]
   Permisos: db_owner en elastic_business
```

### 4. Instalar Tomcat

```bash
# Windows
1. Descargar Tomcat 9
2. Descomprimir en C:\tomcat9
3. Copiar elastic_business.war en:
   C:\tomcat9\webapps\

# Iniciar Tomcat
cd C:\tomcat9\bin
catalina run
```

## Configuración Inicial

### Acceso a la Aplicación

```
URL: http://localhost:8080/elastic_business

# Si Tomcat en servidor:
URL: http://[IP_servidor]:8080/elastic_business
```

### Credenciales Por Defecto

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| admin | admin123 | Administrador |
| demo | demo | Demostración |

**IMPORTANTE**: Cambiar contraseña admin en primera sesión.

### Configuración de Base de Datos

**Archivo: tomcat/webapps/elastic_business/WEB-INF/classes/config.properties**

```properties
# SQL Server
db.driver=com.microsoft.sqlserver.jdbc.SQLServerDriver
db.url=jdbc:sqlserver://localhost:1433;databaseName=elastic_business
db.user=elastic_user
db.password=[tu_contraseña]
db.pool.size=20

# Puerto Tomcat
server.port=8080

# Idioma
app.language=es_ES
```

## Configuración de Empresa

Al iniciar por primera vez:

### 1. Datos Básicos

**Gestión >> Configuración >> Empresa**

| Campo | Ejemplo |
|-------|---------|
| **Código** | EMP001 |
| **Nombre** | Mi Empresa S.L. |
| **CIF** | A12345678 |
| **Dirección** | Calle Principal 123 |
| **Localidad** | Madrid |
| **Código Postal** | 28001 |
| **País** | España |

### 2. Ejercicio Fiscal

**Configuración >> Ejercicios**

```
Año fiscal 2024:
├── Inicio: 01/01/2024
├── Fin: 31/12/2024
└── Cerrado: No
```

### 3. Calendario Laboral

**Laboral >> Calendarios**

Definir días festivos, parones, etc.

### 4. Series Documentales

**Configuración >> Series >> [Tipo documento]**

```
Facturas venta:
├── Prefijo: FAC
├── Año: 2024
├── Próximo: 001
└── Formato: FAC2024001
```

## Carga de Datos

### Importación Masiva

#### Artículos

```
Almacén >> Importar >> Artículos
    └── Seleccionar archivo Excel
        ├── Código artículo ← Obligatorio
        ├── Descripción ← Obligatorio
        ├── Familia ← Obligatorio
        ├── Precio coste
        └── Stock inicial
```

#### Clientes

```
CRM >> Importar >> Clientes
    ├── Código ← Obligatorio
    ├── Razón social ← Obligatorio
    ├── CIF
    ├── Email
    └── Forma de pago
```

#### Proveedores

```
Compras >> Importar >> Proveedores
    ├── Código ← Obligatorio
    ├── Razón social ← Obligatorio
    ├── CIF
    └── Forma de pago
```

### Validación de Datos

Después de importar:

```
1. Revisar registros importados
2. Ejecutar validación
   Gestión >> Utilidades >> Validar datos
3. Revisar reportes de error
4. Corregir datos problemáticos
5. Reimportar si es necesario
```

## Usuarios y Permisos

### Crear Usuario

**Gestión >> Usuarios**

```
Usuario: jgarcia
Contraseña: [segura]
Email: jgarcia@empresa.com
Puesto: Comercial
Menú: Menú Ventas
Permiso: Solo lectura artículos
```

### Roles Predefinidos

| Rol | Acceso |
|-----|--------|
| **Admin** | Todo sistema |
| **Director** | Todos módulos |
| **Comercial** | Ventas, CRM, consulta almacén |
| **Comprador** | Compras, proveedores |
| **Almacenero** | Almacén solamente |
| **Contable** | Finanzas, controlable |
| **Producción** | Producción, órdenes |

## Respaldo y Recuperación

### Copia Seguridad Diaria

```powershell
# Script SQL Server
sqlcmd -S localhost -U elastic_user -P [contraseña] -Q "
BACKUP DATABASE elastic_business 
TO DISK = 'C:\backups\elastic_2024-03-10.bak'
"
```

### Restauración

Si se corrompe Base de datos:

```powershell
sqlcmd -S localhost -U elastic_user -P [contraseña] -Q "
RESTORE DATABASE elastic_business 
FROM DISK = 'C:\backups\elastic_2024-03-10.bak'
"
```

## Mantenimiento

### Tareas Programadas

**Mensual:**
- Validar datos
- Revisar logs de error
- Archivar documentos antiguos

**Trimestral:**
- Revisar permisos de usuario
- Actualizar contraseñas
- Análisis de performance

**Anual:**
- Cierre fiscal
- Archivar históricos
- Planificación upgrades

## Solución de Problemas

### Error: "No puede conectarse a BD"

```
1. Verificar SQL Server activo
   Services.msc → SQL Server running
2. Verificar credenciales en config.properties
3. Verificar base de datos existe
4. Revisar logs: tomcat/logs/catalina.out
```

### Performance Lento

```
1. Aumentar RAM Tomcat:
   catalina.bat set JAVA_OPTS=-Xmx2048m
2. Optimizar índices BD:
   SQL Server Management Studio
3. Revisar queries lentas en logs
```

### Usuario Bloqueado

```
Desbloquear: UPDATE USUARIOS SET bloqueado=0 
WHERE login='usuario'
```

## Soporte Técnico

- **Email**: soporte@imatia.com
- **Teléfono**: +34 986 123 456
- **Portal**: help.imatia.com
- **Comunidad**: forum.imatia.com

## Documentación Adicional

- Manual del usuario completo (PDF)
- Vídeos tutoriales
- Webinars de capacitación
- API documentation

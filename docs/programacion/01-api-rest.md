---
sidebar_position: 1
---

# Guía de Desarrollador

## Introducción

Elastic Business expone **APIs REST** para integración con sistemas externos y customización.

## Arquitectura Técnica

### Stack Tecnológico

```
Frontend
├── HTML5 / CSS3
├── JavaScript
└── AJAX

Backend
├── Java EE 11+
├── Spring Framework
├── Hibernate ORM
└── RESTful APIs

Base de Datos
└── SQL Server 2016+

Servidor Aplicaciones
└── Apache Tomcat 9+
```

### Capas de Aplicación

```
Presentation Layer
    ↓
Business Logic Layer
    ↓
Data Access Layer (DAO)
    ↓
Database
```

## Acceso a APIs

### Documentación OpenAPI/Swagger

```
URL: http://localhost:8080/elastic_business/swagger-ui.html
```

Visualiza todas las APIs disponibles con:
- Endpoints disponibles
- Parámetros requeridos
- Respuestas esperadas
- Códigos de error

### Autenticación

```http
POST /elastic_business/api/auth/login
Content-Type: application/json

{
  "username": "usuario",
  "password": "contraseña"
}

Response:
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 3600
}
```

Usar token en subsecuentes requests:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

## Principales APIs

### Gestión de Artículos

```http
GET /api/v1/articulos
GET /api/v1/articulos/{codigo}
POST /api/v1/articulos
PUT /api/v1/articulos/{codigo}
DELETE /api/v1/articulos/{codigo}
```

**Ejemplo - Obtener artículo:**

```bash
curl -H "Authorization: Bearer [TOKEN]" \
  http://localhost:8080/elastic_business/api/v1/articulos/ART001
```

**Response:**

```json
{
  "codigo": "ART001",
  "descripcion": "Producto A",
  "familia": "FAM001",
  "precio_coste": 15.50,
  "precio_venta": 25.00,
  "stock": 150,
  "unidad": "ud"
}
```

### Gestión de Clientes

```http
GET /api/v1/clientes
GET /api/v1/clientes/{codigo}
POST /api/v1/clientes
PUT /api/v1/clientes/{codigo}
```

### Gestión de Pedidos

```http
GET /api/v1/pedidos
GET /api/v1/pedidos/{numero}
POST /api/v1/pedidos
PUT /api/v1/pedidos/{numero}
```

**Crear pedido:**

```json
POST /api/v1/pedidos
{
  "cliente": "CLI001",
  "fecha": "2024-03-10",
  "almacen": "ALM001",
  "lineas": [
    {
      "articulo": "ART001",
      "cantidad": 100,
      "precio_unitario": 25.00
    }
  ]
}
```

### Gestión de Facturas

```http
GET /api/v1/facturas
POST /api/v1/facturas/{pedido}/facturar
```

### Reportes

```http
GET /api/v1/reportes/ventas?desde=2024-01-01&hasta=2024-03-31
GET /api/v1/reportes/costes?producto={codigo}
GET /api/v1/reportes/inventario
```

## Validación de Datos

### Campos Obligatorios

**Al crear artículo:**
- codigo ← Requerido
- descripcion ← Requerido
- familia ← Requerido

El sistema retorna error si faltan:

```json
HTTP 400 Bad Request
{
  "error": "Validation failed",
  "fields": [
    {
      "field": "codigo",
      "message": "Field is required"
    }
  ]
}
```

## Códigos de Error HTTP

| Código | Significado |
|--------|------------|
| **200** | OK - Éxito |
| **201** | Created - Recurso creado |
| **400** | Bad Request - Datos inválidos |
| **401** | Unauthorized - Sin autenticación |
| **403** | Forbidden - Sin permiso |
| **404** | Not Found - Recurso no existe |
| **500** | Server Error - Error interno |

## Integración de Ejemplo

### Sincronizar inventario desde ERP externo

```python
import requests
import json

# 1. Autenticar
auth_url = "http://elastic:8080/elastic_business/api/auth/login"
auth_payload = {"username": "admin", "password": "admin123"}
response = requests.post(auth_url, json=auth_payload)
token = response.json()["token"]

headers = {"Authorization": f"Bearer {token}"}

# 2. Obtener artículos
articulos_url = "http://elastic:8080/elastic_business/api/v1/articulos"
response = requests.get(articulos_url, headers=headers)
articulos = response.json()

# 3. Sincronizar con sistema externo
for art in articulos:
    try:
        # Enviar a sistema externo
        requests.post(
            "https://mi-erp.com/api/productos",
            json={
                "codigo": art["codigo"],
                "nombre": art["descripcion"],
                "precio": art["precio_venta"],
                "stock": art["stock"]
            }
        )
        print(f"✓ {art['codigo']} sincronizado")
    except Exception as e:
        print(f"✗ Error sincronizando {art['codigo']}: {e}")
```

## Webhooks

Recibir notificaciones en tiempo real.

### Configurar Webhook

**Sistema >> Webhooks**

```
Evento: Pedido creado
URL: https://mi-sistema.com/webhook/pedido
Activo: Sí
```

### Payload de Webhook

Cuando se crea pedido:

```json
POST https://mi-sistema.com/webhook/pedido
{
  "evento": "pedido.creado",
  "timestamp": "2024-03-10T10:30:00Z",
  "data": {
    "numero": "PED001",
    "cliente": "CLI001",
    "total": 2500.00
  }
}
```

## Extensiones y Plugins

### Estructura de Plugin

```
mi-plugin/
├── plugin.xml                 # Definición
├── lib/                       # Dependencias
├── src/
│   └── com/miempresa/
│       └── plugin/Plugin.java # Código
└── config/
    └── configuracion.properties
```

### Ejemplo - Plugin de Validación

```java
package com.miempresa.plugin;

import com.imatia.elastic.api.Plugin;
import com.imatia.elastic.model.Articulo;

public class ValidadorCostes implements Plugin {
    
    public void onArticuloCreated(Articulo articulo) {
        // Validación personalizada
        if (articulo.getPrecioCoste() > articulo.getPrecioVenta()) {
            throw new RuntimeException(
                "Coste no puede ser mayor que venta"
            );
        }
    }
}
```

## Base de Datos - Esquema

### Tabla ARTICULOS

```sql
CREATE TABLE ARTICULOS (
    id_articulo INT PRIMARY KEY IDENTITY(1,1),
    codigo VARCHAR(50) UNIQUE NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    id_familia INT NOT NULL,
    precio_coste DECIMAL(10,2),
    precio_venta DECIMAL(10,2),
    stock INT DEFAULT 0,
    fecha_alta DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_familia) REFERENCES FAMILIAS(id_familia)
);
```

### Tabla PEDIDOS

```sql
CREATE TABLE PEDIDOS (
    id_pedido INT PRIMARY KEY IDENTITY(1,1),
    numero VARCHAR(50) UNIQUE NOT NULL,
    id_cliente INT NOT NULL,
    fecha_pedido DATETIME NOT NULL,
    total DECIMAL(12,2),
    estado VARCHAR(20),
    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);
```

### Relaciones ERD

```
CLIENTES 1 ←  → n PEDIDOS
FAMILIAS 1 ← → n ARTICULOS
PEDIDOS 1 ← → n LINEAS_PEDIDO
ARTICULOS 1 ← n LINEAS_PEDIDO
PROVEEDORES 1 ← → n PEDIDOS_COMPRA
```

## Performance y Mejores Prácticas

### Consultas Optimizadas

❌ Evitar N+1 queries:
```java
// MAL - N+1
for (Cliente c : clientes) {
    Pedidos p = db.query("SELECT * FROM PEDIDOS WHERE cliente=" + c.getId());
}
```

✅ Usar JOIN:
```java
// BIEN - Una sola query
SELECT c.*, p.* FROM CLIENTES c 
LEFT JOIN PEDIDOS p ON c.id = p.id_cliente
```

### Caché y Índices

- Índice en campos de búsqueda frecuente
- Cachear datos estáticos
- Limpiar caché después de cambios

### Rate Limiting

```
Límite: 1000 requests/hora por token
Exceder: HTTP 429 Too Many Requests
```

## Seguridad

### HTTPS Obligatorio

```
Configurar certificado SSL en Tomcat
connector protocol="org.apache.coyote.http11.Http11NioProtocol"
connectionTimeout="20000"
scheme="https" secure="true"
```

### Validación de Entrada

```java
// Prevenir SQL Injection
String query = "SELECT * FROM ARTICULOS WHERE codigo = ?";
PreparedStatement ps = conn.prepareStatement(query);
ps.setString(1, codigo);  // Parametrizado
```

### Encriptación de Contraseñas

```java
// Usar bcrypt, no MD5
passwordEncoder.encode("contraseña");
```

## Documentación Adicional

- OpenAPI Specification: `/swagger-ui.html`
- JavaDoc: `/apidocs/`
- Ejemplos de código: `https://github.com/imatia/elastic-samples`
- Comunidad: `forum.imatia.com/developers`

## Soporte Técnico Desarrolladores

- Email: dev-support@imatia.com
- Slack: developer-channel
- Documentación: docs.imatia.com

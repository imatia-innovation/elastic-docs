# Elastic_Business_Manual_explicación_tablas_BBDD - Página 8

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

## Texto extraído

 
  
 
 
Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 8 / 11 
www.imatia.com   
 
- 
Tabla de clientes: 
 sales_customers  
o 
customer_id
 : clave primaria/identificado
 r 
 
 
 
 
 
- 
Tabla de pedidos de ventas: 
 sales_orders  
o 
order_id
 : identificador/clave  
- 
Tabla de líneas del pedido de ventas: 
 sales_order_details  
o 
order_detail_id
 : identificador  
o 
order_id
 : identificador del pedido  
o 
item_id
 : identificador del articulo  
 
select  
sales_customers.customer_id  
,sales_customers.customer_company_name  
,sales_customers.customer_trade_name  
,sales_
 customers.customer_cif_nif  
from sales_customers  


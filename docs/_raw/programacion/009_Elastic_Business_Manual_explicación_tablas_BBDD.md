# Elastic_Business_Manual_explicación_tablas_BBDD - Página 9

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

## Texto extraído

 
  
 
 
Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 9 / 11 
www.imatia.com   
 
 
 
 
select  
sales_orders.order_id  
,sales_orders.order_code as 'Numero pedido'  
,sales_orders.document_date as 'Fecha pedido'  
,sales_customers.customer_company_name  
as 'Razón social'  
,sales_orders.total_tax_base 'Base del pedido'  
,sales_orders.total_amount as 'Importe total del pedido'  
,sales_order_details.item_code as 'Codigo'  
,sales_order_details.item_description as 'Descripcion'  
,ALM_MAESTRO_ARTICULOS.ean13  
,sales_order_details.unit_price as 'Precio unitario'  
,sales_order_details.real_quantity as 'Cantidad real de la linea'  
,sales_order_details.taxable_amount as 'Base de la linea'  
,sales_order_details.total_amount as 'Importe total de la linea'  
from sales_orders  
join sales_customers on sales_customers.customer_id = sales_orders.customer_id  
left join sales_order_details on sales_order_details.order_id = sales_orders.order_id  
join ALM_MAESTRO_ARTICULOS on ALM_MAESTRO_ARTICULOS.ID_ARTICULO = sales_order_details.item_id  


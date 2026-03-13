# Elastic_Business_Manual_explicación_tablas_BBDD - Página 11

**Origen:** `build\sources\programacion\Elastic_Business_Manual_explicación_tablas_BBDD.pdf`
**Módulo:** programacion

---

## Texto extraído

 
  
 
 
Elastic Business  
Tablas Elastic Business©  
| 
2
026  
 11 / 11 
www.imatia.com   
 
 
 
- 
Tablas de subcuentas: 
 ECOFIN_SUBCUENTAS  
- 
Tabla de asientos contables: 
 ECOFIN_ASIENTOS  
- 
Tablas de partidas contables: 
 ECOFIN_PARTIDAS  
select  
cal_rma.rma_id  
,cal_rma.rma_code  
,cal_rma_status_config.status_description  
,sales_customers.customer_company_name  
from cal_rma  
left join cal_rma_status_config on cal_rma_status_config.rma_status_id = cal_rma.rma_status  
left join sales_customers on sales_customers.customer_id = rma_customer_id  


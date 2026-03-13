# 161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0 - Página 30

**Origen:** `build\sources\guia_de_uso\161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0.pdf`
**Módulo:** guia_de_uso

---

## Texto extraído

 
 
· 30 · 
 
www. elastic -business .com  
 
 
Guía rápida de iniciación  Despliegue  
 
var  url=”http://127.0.0.1:8080/elastic/webstart/index.jsp”  
var jnlp=”http://127.0.0.1:8080/elastic/webstart/start.jnlp”  
 
11. Por último se copia la licencia license.dat  suministrada  en el directorio 
C:\Tomcat7 \webapps \elastic \WEB-INF\classes  
 
12. Para configurar el servidor de correo para el envío de mails desde la aplicación se 
debe editar el fichero C:\Tomcat7 \webapps \elastic \WEB-
INF\classes \com\imatia \elastic \servidor \avisos \mail.conf  
 
 Los parámetros a configurar son:  
  
▪ mailserver : Servidor de correo  
▪ username : Usuario para el servidor de correo  
▪ password : Contraseña para el servidor de correo  
▪ auth : Indica si necesita autenticación.  
▪ from : E -mail que figurará como remitente.  
 
13. Por último se debe reiniciar el servicio del Apache Tomcat. Una vez reiniciado para 
comprobar que la aplicación está instalada correctamente, se accede al navegador 
y se ingresa la ruta con la IP del servidor el puerto y el nombre de la aplicación. En 
este ejemplo sería http://127.0.0.1:8080/elastic . Desde la página web que aparece 
se puede descargar la aplicación cliente.  
 
 
 
 
 
 
 
 
 
 
 


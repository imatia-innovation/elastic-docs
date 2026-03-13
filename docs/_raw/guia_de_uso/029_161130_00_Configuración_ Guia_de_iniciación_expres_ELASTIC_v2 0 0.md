# 161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0 - Página 29

**Origen:** `build\sources\guia_de_uso\161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0.pdf`
**Módulo:** guia_de_uso

---

## Texto extraído

 
 
· 29 · 
 
www. elastic -business .com  
 
 
Guía rápida de iniciación  Despliegue  
 
7. A continuación se debe editar el archivo database.properties  en el que se deben 
modificar los siguientes puntos:  
 
URL: Se debe establecer la URL de conexión a la base de datos, en este caso es 
URL=jdbc:sqlserver://127.0.0.1:42008;databaseName=elastic . La URL está formada por la 
IP del equipo donde se encuentra instalado el servidor de base de datos (en nuestro caso 
es local), el puerto del servidor de base de datos y el nombre de la base de datos.  
 
User:  Se establece el usuario sa. También existe la posibilidad de crear un usuario 
específico para la base de datos desde el SQL Server Management Studio  
 
Password:  Se establece la contraseña que pusimos en el proceso de instalación del servidor 
de bases de datos.  
 
8. Ahora se debe modificar el fichero locator.properties que se encuentra en la misma 
ubicación que los anteriores.  
 
ReportStorePath:  Se cambia por la ruta en la que se encuentra la carpeta 
InformesResearch , en este caso por C:/Tomcat7/webapps/elastic/WEB -
INF/classes/InformesResearch  
 
LogFile:  Se establece la ruta en la que la aplicación va a escribir el registro de eventos. En 
este caso se pone en C:/Tomcat7/webapps/elastic/serverlog.txt  
 
9. El siguiente paso es configurar la parte del cliente. Para ello hay que ir a la carpeta 
situada en C:\Tomcat7 \webapps \elastic \webstart y abrir el archivo start.jnlp  
 
Es necesario modificar la línea superior del archivo, estableciendo el parámetro codebase,  
en él se debe establecer la IP del servidor (interna o externa) y el puerto. La ruta debe 
tener un aspecto como lo siguiente: http://127.0.0.1:8080/elastic/webstart  
 
También es necesario modificar la propiedad 
com.ontimize.locator.ReferenceLocator.Hostname  con el valor de la IP interna o externa, 
debe ser la misma que la que va en el codebase.  
 
10. También se deben hacer modificaciones en el archivo 
parametrosPatronResearch.jsp . Se debe cambiar el valor de las variables url y jnlp 
por la ruta correcta. Deberían quedar como sigue, el puerto y la ip deben ser las 
mismas que las configuradas en el archivo start.jnlp:  


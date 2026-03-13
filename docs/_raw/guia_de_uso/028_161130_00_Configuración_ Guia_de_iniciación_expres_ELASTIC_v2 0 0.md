# 161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0 - Página 28

**Origen:** `build\sources\guia_de_uso\161130_00_Configuración_ Guia_de_iniciación_expres_ELASTIC_v2 0 0.pdf`
**Módulo:** guia_de_uso

---

## Texto extraído

 
 
· 28 · 
 
www. elastic -business .com  
 
 
Guía rápida de iniciación  Despliegue  
(From device), se selecciona la ruta en la que se encuentra la base de datos en 
formato .bak y se marca Restaura (Restore). En opciones, se marca la opción 
remplazar base de datos existente (Overwrite the existing database). Por último se 
pulsa el botón “Aceptar”. 
 
 
 
3. Una vez restaurada la base de datos, el siguiente paso es instalar la aplicación. Se 
coge el fichero de la aplicación que puede estar en formato .war o en algún formato 
comprimido.  
 
4. Se copia el archivo al directorio de instalación del Apache Tomcat , en este caso 
C:\Tomcat7 \webapps \. La aplicación se debe descomprimir en un directorio con el 
nombre de la aplicación. Este directorio en su interior debe contener a su vez otros 
dos directorios llamados WEB-INF y webstart.  
 
5. Una vez descomprimida la aplicación, el siguiente paso es configurar el servidor de 
la aplicación. Para ello hay que editar el archivo server.properties  que se encuentra 
en la dirección C:\Tomcat7 \webapps \elastic \WEB-
INF\classes \com\imatia \elastic \servidor \prop.  
 
6. Se debe eliminar la línea Hostname  y guardar el archivo.  



***Luz Robotica***

    Es un programa, que realiza una serie de secuencias demostrativas para el manejo del servomotor y led rgb.
    
    Las dependencias que tiene el programa son las siguientes:
    
>     python.
>     bash.
    
***Instalación***

    En la carpeta luzrobotica, encontramos los archivos necesarios para ejecutar el programa.
    
>     Copiar el archivo **luzrobotica.py** a la siguinte ruta **/usr/local/bin**, dar permisos de ejecución con **chmod +x /usr/local/bin/luzrobotica.py**.
> 
>     Crear la carpeta luzrobotica en la siguiente ruta **/usr/local/etc**, copiar los sigientes archivos **configuracion.py**, **rgb.py** y **servo.py** a la siguiente ruta **/usr/local/etc/luzrobotica**.
>     
>     Copiar el archivo **zdemonio.sh** a la siguiente ruta **/etc/init.d**.
>     
>     Ir a la siguiente ruta **/etc/rc3.d** y crear el siguiente enlace simbolico **ln -sf /etc/init.d/zdemon.sh S04demonio**.
>     
>     Ejecutar la siguiente sentencia **systemctl daemon-reload**.
    
***Uso***

    Probar nuestra instalación:
        **sudo service zdemonio start** inicia servicio
        **sudo service zdemonio stop** detiene servicio
        **sudo service zdemonio restart** restaura servicio
    
    Ahora se puede reiniciar el sistema y seguira corriendo el programa luzrobotica
    

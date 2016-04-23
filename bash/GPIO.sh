#Añadir Licencia

#!/bin/sh

#Definimos una funcion que terminara el script
#en caso de error
function salir
{
	exit 0
}

#Valida que este el parametro del pin
if [ $# -lt 1 ]; then
	echo "No se encontro parametro" >> error.log
	exit;
fi

#Se definen las variables de inicio
PIN=$1

#configura el GPIO
echo $PIN > /sys/class/gpio/export 2>> error.log || salir
echo "out" > /sys/class/gpio/"gpio$PIN"/direction 2>> error.log || salir

#envia el tren de pulsos al GPIO
while true
do
        echo 1 > /sys/class/gpio/gpio4/value 2>> error.log || salir
		sleep 0.016
        echo 0 > /sys/class/gpio/gpio4/value 2>> error.log || salir
		sleep 0.016
done

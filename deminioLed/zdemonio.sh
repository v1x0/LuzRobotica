#!/bin/bash
#Manejo de opciones para el demonio

#Salir del programa
function salir
{
	echo "Error favor de ver el archivo error.log"
	exit 0
}

#Inicia demonio
function start
{
	if [ -f /var/run/zdemonio.pid ]; then
		echo "El proceso esta iniciado ..."
	else
		/sbin/start-stop-daemon \
		--start \
		--pidfile /var/run/zdemonio.pid  \
		--user root \
		--group root \
		-b \
		--make-pidfile \
		--chuid root \
		--exec /usr/bin/python /usr/local/bin/led.py 2>> error.log || salir 
	fi
}

#Detiene demonio
function stop
{
	if [ -f /var/run/zdemonio.pid ]; then
		/sbin/start-stop-daemon \
		--stop \
		--pidfile /var/run/zdemonio.pid \
		--remove-pidfile 2>> error.log || salir 
	else
		echo "El proceso esta detenido ..."
	fi
}

#Restaura demonio
function restart
{
	echo "Restaurando demonio ..."
	stop
	start
}

case $1 in
	start)
		start
	;;
	stop)
		stop
	;;
	restart)
		restart
	;;
	*)
		echo "Usa service zdemonio.sh {start|stop|restart}"
	;;
esac
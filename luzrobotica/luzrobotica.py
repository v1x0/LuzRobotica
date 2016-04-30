#!/bin/python
# -*- coding: utf-8 -*-
#****************************************************************************************
#  Derechos de autor (c) 2016 
#  Autores: 	Cesar Israel Gonzalez Perez	(kaetzer)
#				Jose Abel Ochoa Ortiz		(sibik)
#				David				(v1x0)
#				Alberto				(alberto)
#
#  Se concede permiso, de forma gratuita y sin garantia, a cualquier persona que obtenga
#  una copia de este software y archivos de documentación asociados (el
#  "Software"), para trabajar con el Software sin restricciones, incluidos
#  sin limitación, los derechos para usar, copiar, modificar, fusionar, publicar,
#  distribuir, sublicenciar y / o vender copias del Software.
#  
#  Programa para controlar una luz robotica RBG con Raspberry Pi B+
#  Usando las salidas GPIO emulando PWM por software para 
#  controlar la intensidad de cada color y generar las mezclas.
#  Asi tambien para posicionar dos servomotores y obteber los 
#  movimientos Pan y Tilt.
#    
#  Materiales:
#  1 RaspberryPi B+
#  1 LED RGB 3w
#  2 Servomotores 3001HB
#  cables de conexion
#  
#
#  Fecha: Lun 25 Abril 2016		
#****************************************************************************************
try:
	import threading
	import time
	import RPi.GPIO as GPIO
	import sys
	sys.path.append('/usr/local/etc/luzrobotica')
	import configuracion
	import servo
	import rgb

	#Definicion de los parametros iniciales
	#lista_pout_pwm definira las pines de salida para la salida del pwm
	#lista_pout_frec define la frecuencia a la que va trabajar cada pwm
	#lista_pwm almacena los pwm creados en el programa
	#ini_duty define donde comenzara a operar el servomotor
	#continuar variable que se usara para el ciclo de los hilos
	#lista_acciones contiene los metodos que define la secuencia del servomotor y led rgb
	#lista_hilos_acciones almacena los hilos creados por los metodos que definen las acciones del servomotor y ledrgb
	lista_pout_pwm = {0:11,1:13,2:15,3:19,4:21}

	lista_pout_frec = {0:50,1:50,2:50,3:50,4:50}

	lista_pwm = []
		
	ini_duty = 0
		
	continuar = 1
		
	lista_acciones =  {0:servo.ini_accion, 1:rgb.ini_accion}
		
	lista_hilos_acciones = []
	
	#Se inicializa la parte principal del programa a ejecutar
	configuracion.ini_con(GPIO,lista_pout_pwm,lista_pwm,lista_pout_frec, ini_duty)
	for hilo in lista_acciones:
		lista_hilos_acciones.insert(hilo, threading.Thread(target=lista_acciones[hilo], args=(hilo, continuar, lista_pwm, time,  )))
		lista_hilos_acciones[hilo].start()
		
except KeyboardInterrupt:
	continuar = 0
	file = open("error.log","a")
	file.write("Error al ejecutar el programa ...")
	file.close()
	for pwm in lista_pwm:
		pwm.stop()
	GPIO.cleanup()

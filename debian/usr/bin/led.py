#!/bin/python
try:
	#librerias
	import threading
	import time
	import RPi.GPIO as GPIO
	import sys

	#Definir la lista pwm de pinout
	lista_pout_pwm = {0:11,1:13,2:15,3:19,4:21}

	#Definir la lista frecuencia de pinout
	lista_pout_frec = {0:50,1:50,2:50,3:50,4:50}

	#Definir lista PWM
	lista_pwm = []
	
	#Definir el duty inicial
	ini_duty = 0
	
	#Definir bandera de paro de hilo
	continuar = 1
	
	#Definir retardo servos
	retardo_servo = 2
	
	#Definir retardo led
	retardo_led = 0.1
	
	#inicia la configuracion del sistema
	def configuracion():
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		for indice in lista_pout_pwm:
			GPIO.setup(lista_pout_pwm[indice], GPIO.OUT)
			lista_pwm.insert(indice,GPIO.PWM(lista_pout_pwm[indice], lista_pout_frec[indice]))
			lista_pwm[indice].start(ini_duty)
	
	#Definir movimientos del servo
	def accion_servo(hilo):
		j = hilo + 1
		while continuar:
			lista_pwm[hilo].ChangeDutyCycle(12)
			time.sleep(retardo_servo)
			lista_pwm[j].ChangeDutyCycle(12)
			time.sleep(retardo_servo)
			lista_pwm[hilo].ChangeDutyCycle(1)
			time.sleep(retardo_servo)
			lista_pwm[j].ChangeDutyCycle(1)
			time.sleep(retardo_servo)
		
	#Definir brillo del led
	def accion_led(hilo):
		i = hilo + 1
		k = i + 1
		l = k + 1
		while continuar:
			for dc in range(0, 105, 5):
				lista_pwm[i].ChangeDutyCycle(dc)
				lista_pwm[k].ChangeDutyCycle(dc)
				lista_pwm[l].ChangeDutyCycle(dc)
				time.sleep(retardo_led)
			for dc in range(100, -5, -5):
				lista_pwm[i].ChangeDutyCycle(dc)
				lista_pwm[k].ChangeDutyCycle(dc)
				lista_pwm[l].ChangeDutyCycle(dc)
				time.sleep(retardo_led)
	
	#Definir lista de acciones
	lista_acciones =  {0:accion_servo, 1:accion_led}
	
	#Definir lista de hilos pwm
	lista_hilos_acciones = []
	
	
	#Inica el programa
	configuracion()
	for hilo in lista_acciones:
		lista_hilos_acciones.insert(hilo, threading.Thread(target=lista_acciones[hilo], args=(hilo, )))
		lista_hilos_acciones[hilo].start()
		

except KeyboardInterrupt:
	continuar = 0
	for pwm in lista_pwm:
		pwm.stop()
	GPIO.cleanup()
	file = open("error.log","a")
	file.write("Error al ejecutar el programa ...")
	file.close()

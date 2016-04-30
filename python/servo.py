#Metodo que define la secuencia que va tener el servomotor
#si se requiere modificar la secuencia del servomotor 
#agregar las sentencias necesarias
retardo = 2
def ini_accion(hilo,continuar,lista_pwm, time):
	j = hilo + 1
	while continuar:
		lista_pwm[hilo].ChangeDutyCycle(12)
		time.sleep(retardo)
		lista_pwm[j].ChangeDutyCycle(12)
		time.sleep(retardo)
		lista_pwm[hilo].ChangeDutyCycle(1)
		time.sleep(retardo)
		lista_pwm[j].ChangeDutyCycle(1)
		time.sleep(retardo)
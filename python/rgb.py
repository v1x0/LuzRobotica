#Metodo que define la secuencia que va tener el led
#si se requiere modificar la secuencia del led 
#agregar las sentencias necesarias
retardo = 0.1
def ini_accion(hilo,continuar,lista_pwm,time):
	i = hilo + 1
	k = i + 1
	l = k + 1
	while continuar:
		for dc in range(0, 105, 5):
			lista_pwm[i].ChangeDutyCycle(dc)
			lista_pwm[k].ChangeDutyCycle(dc)
			lista_pwm[l].ChangeDutyCycle(dc)
			time.sleep(retardo)
		for dc in range(100, -5, -5):
			lista_pwm[i].ChangeDutyCycle(dc)
			lista_pwm[k].ChangeDutyCycle(dc)
			lista_pwm[l].ChangeDutyCycle(dc)
			time.sleep(retardo)
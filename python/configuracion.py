#Metodo que inicializa las salidas de los gpio
def ini_con(GPIO,lista_pout_pwm,lista_pwm,lista_pout_frec,ini_duty):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	for indice in lista_pout_pwm:
		GPIO.setup(lista_pout_pwm[indice], GPIO.OUT)
		lista_pwm.insert(indice,GPIO.PWM(lista_pout_pwm[indice], lista_pout_frec[indice]))
		lista_pwm[indice].start(ini_duty)
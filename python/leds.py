import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

p = GPIO.PWM(11, 50)  # channel=12 frequency=50Hz
p1 = GPIO.PWM(13, 50)  # channel=12 frequency=50Hz
p2 = GPIO.PWM(15, 30)  # channel=12 frequency=50Hz
p.start(0)
p1.start(0)
p2.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
p1.stop()
p2.stop()
GPIO.cleanup()

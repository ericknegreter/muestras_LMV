import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT) ## GPIO 17 como salida
GPIO.setup(12, GPIO.OUT) ## GPIO 27 como salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
def blink():
    print ("Ejecucion iniciada...")
    iteracion = 0
    while iteracion < 15: ## Segundos que durara la funcion
        GPIO.output(16, True) ## Enciendo el 17
        GPIO.output(12, False) ## Apago el 27
        GPIO.output(21, True)
        time.sleep(1) ## Esperamos 1 segundo
        GPIO.output(16, False) ## Apago el 17
        GPIO.output(12, True) ## Enciendo el 27
        GPIO.output(21, False)
        time.sleep(1) ## Esperamos 1 segundo
        iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
    print ("Ejecucion finalizada")
    GPIO.cleanup() ## Hago una limpieza de los GPIO

blink()

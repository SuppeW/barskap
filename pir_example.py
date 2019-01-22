import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(11, GPIO.IN)


while True:
    signal = GPIO.input(11)
    if signal == 1:
        print("motion detected")

import RPi.GPIO as GPIO
import time
import espeak

reedSwitchPin = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Hvilke nummer system du bruker til pins.
GPIO.setup(reedSwitchPin, GPIO.IN)

while True:
    if i == 0:
        print("Door Closed")
    else:
        print("Door Opened")

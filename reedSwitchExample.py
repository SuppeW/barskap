#Grå er -
#Rød er +
#HVis er Signal


import RPi.GPIO as GPIO
import time
import espeak
import pygame

reedSwitchPin = 11
choirsound = "heavenly_choir.mp3"

pygame.mixer.init()
pygame.mixer.music.load(choirsound)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Hvilke nummer system du bruker til pins.
GPIO.setup(reedSwitchPin, GPIO.IN)

while True:
    if i == 0:
        print("Door Closed")
        ans = input("play sound: y or n: ")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print("Door Opened")

import pygame

choirsound = "heavenly_choir.mp3"


ans = input("play sound: y or n: ")
if ans == "y":
    pygame.mixer.init()
    pygame.mixer.music.load(choirsound)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
else:
    print("dickhead")

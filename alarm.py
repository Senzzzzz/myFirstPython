import time
import datetime
import pygame

pygame.mixer.init()
pygame.init()
wakeup_sfx = pygame.mixer.Sound("wakeup.mp3")

is_running = True
user = input("Enter the alarm time (HH:MM:SS): ")

while is_running:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time.sleep(1)
    print(current_time)

    if current_time == user:
        print("WAKE UP!")
        wakeup_sfx.play()
        pygame.mixer.get_busy()
        while pygame.mixer.get_busy():
            time.sleep(0.1)
        is_running = False

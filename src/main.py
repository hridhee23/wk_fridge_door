from gpiozero import DigitalInputDevice
import pygame
import time

sensor1 = DigitalInputDevice(27, pull_up=True, bounce_time=0.1)
sensor2 = DigitalInputDevice(17, pull_up=True, bounce_time=0.1)

pygame.mixer.init()
pygame.mixer.music.load("../audio/test.mp3")


def update():
    s1 = sensor1.value
    s2 = sensor2.value

    magnet1_away = (s1 == 0)
    magnet2_away = (s2 == 0)

    if magnet1_away or magnet2_away:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()


print("Running...")

while True:
    update()
    time.sleep(0.1)
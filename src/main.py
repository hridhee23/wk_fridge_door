import os
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["AUDIODEV"] = "hw:1,0"

from gpiozero import DigitalInputDevice
import pygame
import time

AUDIO_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "audio")

sensor1 = DigitalInputDevice(27, pull_up=True, bounce_time=0.1)
sensor2 = DigitalInputDevice(17, pull_up=True, bounce_time=0.1)
time.sleep(5)

pygame.mixer.init()

startup = pygame.mixer.Sound(os.path.join(AUDIO_DIR, "startup.mp3"))
startup.play()
pygame.time.wait(int(startup.get_length() * 1000))

pygame.mixer.music.load(os.path.join(AUDIO_DIR, "main_audio.mp3"))


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
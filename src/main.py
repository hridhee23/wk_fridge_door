from gpiozero import DigitalInputDevice
from signal import pause
import pygame

# GPIO 27
hall_sensor = DigitalInputDevice(27, pull_up=True)

# Initialize pygame mixer
pygame.mixer.init()

# Load audio file
pygame.mixer.music.load("../audio/test.mp3")

def magnet_removed():
    print("Magnet removed -> play audio")

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

def magnet_present():
    print("Magnet detected -> stop audio")

    pygame.mixer.music.stop()

# Most hall sensors:
# LOW  = magnet present
# HIGH = magnet removed

hall_sensor.when_activated = magnet_present
hall_sensor.when_deactivated = magnet_removed

print("Waiting for magnet events...")
pause()
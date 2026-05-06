from gpiozero import Button, LED, DigitalInputDevice
from time import sleep
from signal import pause
import subprocess

with open("../videos/demo.mp4", "rb") as f:
    f.read()

#button = Button(17)
led = LED(18)
hall = DigitalInputDevice(27, pull_up=True, bounce_time=0.2)

busy = False
browser_process = None

def run_all():
    global busy, browser_process
    
    if busy:
        return
    
    busy = True
    led.on()
    
    # open website
    #browser_process = subprocess.Popen(["chromium", "--kiosk", "https://www.google.com"])
    
    # play video
    video = subprocess.Popen(["cvlc", "--fullscreen", "--play-and-exit", "--no-video-title-show",
                              "../videos/demo.mp4"])
    
    video.wait()
    
    led.off()
    busy = False

#button.when_pressed = run_all
hall.when_activated = run_all
pause()
from gpiozero import Button, LED
from signal import pause

button = Button(17)
led = LED(18)

button.when_pressed = led.on
button.when_released = led.off

pause()
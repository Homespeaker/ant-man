import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)
led = 26
rg.setup(led, rg.OUT)
button = 13
state = 0

rg.setup(button, rg.IN)
while True:
    if rg.input(button):
        state = int(not(bool(state)))
        rg.output(led, state)
        time.sleep(0.2)
    
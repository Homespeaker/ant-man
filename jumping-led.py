import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)
leds = [24, 23, 17, 12, 16, 25, 27, 22]
rg.setup(leds, rg.OUT)
rg.output(leds, 0)
state = 0
ltime = 0.3

while True:
    for led in leds:
        rg.output(led, 1)
        time.sleep(ltime)
        rg.output(led, 0)
    


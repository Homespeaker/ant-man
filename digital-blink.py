import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)
led = 26
rg.setup(led, rg.OUT)
state = 0
period = 1.0

while True:
    rg.output(led, state)
    state = int(not(bool(state)))
    time.sleep(period)
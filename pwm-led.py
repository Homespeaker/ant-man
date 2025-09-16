import RPi.GPIO as rg
import time

rg.setmode(rg.BCM)
led = 26
rg.setup(led, rg.OUT)
pwm = rg.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    
    duty += 1.0
    if duty > 100.0:
        duty = 0.0

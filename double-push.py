import RPi.GPIO as rg
import time

leds = [16, 12, 25, 17, 27, 23, 22, 24]
rg.setmode(rg.BCM)
rg.setup(leds, rg.OUT)
rg.output(leds, 0)

up = 9
down = 10
rg.setup(up, rg.IN)
rg.setup(down, rg.IN)

reboot = 13
rg.setup(reboot, rg.IN)

num = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

def printled(m):
    leds = [16, 12, 25, 17, 27, 23, 22, 24]
    for i in range(len(m)):
        rg.output(leds[i], m[i])
        

while True:
    if rg.input(reboot):
        num = 0
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif rg.input(up) and rg.input(down):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif rg.input(up):
        if num == 255:
            rg.output(leds, 0)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            time.sleep(0.3)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            time.sleep(0.3)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            continue
        num += 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    elif rg.input(down):
        if num == 0:
            rg.output(leds, 0)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            time.sleep(0.3)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            time.sleep(0.3)
            rg.output(leds, 1)
            time.sleep(0.3)
            rg.output(leds, 0)
            continue
        num -= 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    printled(dec2bin(num))
    
    
    
    
    
    
    
    
    
    
    
    
    

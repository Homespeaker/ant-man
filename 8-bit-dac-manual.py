import RPi.GPIO as rp

dac_pins = [16, 20, 21, 25, 26, 17, 27, 22]
rp.setmode(rp.BCM)
rp.setup(dac_pins, rp.OUT)
dac_range = 3.3

def voltage_to_number(v):
    if not(0.0 <= v <= dac_range):
        print(f"Что-то мы перенапряглись, явно сильнее чем {dac_range:.2f} В")
        print("Пора разрядить обстановочку")
        return 0
    return int(v / dac_range * 255) 

def number_to_dac(n):
    print(n)
    s = bin(n)[2:].zfill(8)
    s = [int(i) for i in s]
    for i in range(len(dac_pins)):
        rp.output(dac_pins[i], s[i])
    
try:
    while True:
        try:
            v = float(input("Введите уровень напряги в вольтусах: "))
            n = voltage_to_number(v)
            number_to_dac(n)
        
        except ValueError:
            print("Атата, мы используем только числа, ну-ка введи что требуется\n")
finally:
    rp.output(dac_pins, 0)
    rp.cleanup()
        
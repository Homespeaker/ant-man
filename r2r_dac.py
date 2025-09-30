import RPi.GPIO as rp


class r2r_dac:
    def __init__(self, gpio_bits, dac_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dac_range = dac_range
        self.verbose = verbose
        
        rp.setmode(rp.BCM)
        rp.setup(self.gpio_bits, rp.OUT, initial=0)
        
    def deinit(self):
        rp.output(self.gpio_bits, 0)
        rp.cleanup()
        
    def number_to_dac(self, n):
        s = bin(n)[2:].zfill(8)
        s = [int(i) for i in s]
        for i in range(len(self.gpio_bits)):
            rp.output(self.gpio_bits[i], s[i])
    
    def voltage_to_number(self, v):
        if not(0.0 <= v <= self.dac_range):
            print(f"Что-то мы перенапряглись, явно сильнее чем {dac_range:.2f} В")
            print("Пора разрядить обстановочку")
            return dac.number_to_dac(0)
        return dac.number_to_dac(int(v / self.dac_range * 255))
    
if __name__ == "__main__":
    try:
        dac = r2r_dac([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
        
        while True:
            try:
                v = float(input("Введите напряжение в вольтусах: "))
                dac.voltage_to_number(v)
                
            except ValueError:
                print("Атата, мы используем только числа, ну-ка введи что требуется\n")
    finally:
        dac.deinit()
                
                
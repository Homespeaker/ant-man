import RPi.GPIO as rp

rp.setmode(rp.BCM)
class r2r_dac:
    def __init__(self, gpio_pin, pwm_freak, dac_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_freak = pwm_freak
        self.dac_range = dac_range
        self.verbose = verbose
        
        rp.setmode(rp.BCM)
        rp.setup(self.gpio_pin, rp.OUT)
        global pwm
        pwm = rp.PWM(self.gpio_pin, self.pwm_freak)
        duty = 0.0
        pwm.start(duty)
        
        
    def deinit(self):
        rp.output(self.gpio_pin, 0)
        rp.cleanup()
    
    def voltage_to_number(self, v):
        if (0.0 <= v <= self.dac_range):
            pwm.ChangeDutyCycle(v / self.dac_range * 100)
        else:
            print(f"Что-то мы перенапряглись, явно сильнее чем {self.dac_range:.2f} В")
            print("Пора разрядить обстановочку")
                       
    
    
if __name__ == "__main__":
    try:
        dac = r2r_dac(12, 500, 3.3, True)
        
        while True:
            try:
                v = float(input("Введите напряжение в вольтусах: "))
                dac.voltage_to_number(v)
                
            except ValueError:
                print("Атата, мы используем только числа, ну-ка введи что требуется\n")
    finally:
        dac.deinit()
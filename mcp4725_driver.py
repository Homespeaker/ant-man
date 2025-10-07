import smbus
import RPi.GPIO as rp

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        
    
    def deinit(self):
        self.bus.close()
         
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            print(number)
        
        if not (0 <= number <= 4095):
         print("Чмсло выходит за разрядность MCP4752 (12 бит)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)
        
        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Напряжение не долнжно выходить за границы")
        else:
            dac_value = min(int((voltage / self.dynamic_range) * 4095), 4095)
            dac.set_number(int(dac_value))
           
if __name__ == "__main__":
    
        dac = MCP4725(5.0)
        
        while True:
            try:
                v = float(input("Введите напряжение в вольтусах: "))
                dac.set_voltage(v)
                
            except ValueError:
                print("Атата, мы используем только числа, ну-ка введи что требуется\n")
        
        
        
            
        
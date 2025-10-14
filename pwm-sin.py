import signal_generetor as sg
import pwm_dac as pd
import time as t

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pd.r2r_dac(12, 500, 3.3, True)
        
        while True:
            try:
                i = sg.get_sin_wave_amplitude(signal_frequency, t.time())
                sv = i * amplitude
                dac.voltage_to_number(sv)
                sg.wait_for_sampling_period(sampling_frequency)
                
            except ValueError:
                print("Атата, мы используем только числа, ну-ка введи что требуется\n")
    finally:
        dac.deinit()
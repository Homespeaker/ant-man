import r2r_dac as r2r
import signal_generetor_t as sg
import time as t

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.r2r_dac([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
    while True:
        i = sg.get_sin_wave_amplitude(signal_frequency, t.time())    
        sv = i * amplitude
        dac.voltage_to_number(sv)
        sg.wait_for_sampling_period(sampling_frequency)
    

import mcp4725_driver as md
import signal_generetor_t as sg
import time as t

amplitude = 4
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    
        dac = md.MCP4725(5.0)
        
        while True:
            i = sg.get_sin_wave_amplitude(signal_frequency, t.time())
            sv = i * amplitude
            dac.set_voltage(sv)
            sg.wait_for_sampling_period(sampling_frequency)
                
                

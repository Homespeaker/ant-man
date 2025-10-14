import numpy as np, time as t

def get_sin_wave_amplitude(freq, time):
    period = 1 /freq
    phase = time % period
    if phase <= period / 2:
        return (2/period)*phase
    else:
        return 1 - (2/period)*(phase - period/2)
    

def wait_for_sampling_period(sampling_frequency):
    t.sleep(1/sampling_frequency)

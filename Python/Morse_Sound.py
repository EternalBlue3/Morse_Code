import numpy as np
import struct 
import wave

def sine_samples(freq, duration, framerate, amplitude=0.5):
    X = (2*np.pi*freq/framerate) * np.arange(framerate*duration)

    S = (amplitude*32767*np.sin(X)).astype(int)

    as_packed_bytes = (map(lambda v:struct.pack('h',v), S))
    return as_packed_bytes

def output_wave(path, frames, framerate):
    with wave.open(path,'w') as output:
        output.setparams((1,2,framerate,0,'NONE','not compressed'))
        output.writeframes(frames)

def output_sound(path, freq, dur, framerate):
    frames = b''.join(sine_samples(freq,dur, framerate))
    output_wave(path, frames, framerate)

framerate = 60000 # framerate
beep_freq = 550 # Hz
beep_duration = 0.05 # seconds

output_sound('dot.wav', beep_freq, beep_duration, framerate)
output_sound('dash.wav', beep_freq, beep_duration*3, framerate)

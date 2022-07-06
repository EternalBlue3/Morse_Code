import numpy as np
import struct 
import wave

# Code based off of this answer http://stackoverflow.com/a/33246354/2574639
def sine_samples(freq, duration, framerate, amplitude=0.5):
    # Get (sample rate * duration) samples on X axis 
    # (between freq oscillations of 2pi)
    X = (2*np.pi*freq/framerate) * np.arange(framerate*duration)

    # Get sine values for these X axis samples (as integers)
    S = (amplitude*32767*np.sin(X)).astype(int)

    # Pack integers as signed "short" integers (-32767 to 32767)
    as_packed_bytes = (map(lambda v:struct.pack('h',v), S))
    return as_packed_bytes

def output_wave(path, frames, framerate):
    with wave.open(path,'w') as output:
        # Set parameters for output WAV file
        # (1 channel, 2 bytes per sample, framerate, num frames, no compression, no compression)
        output.setparams((1,2,framerate,0,'NONE','not compressed'))
        output.writeframes(frames)

def output_sound(path, freq, dur, framerate):
    # join the packed bytes into a single bytes frame
    frames = b''.join(sine_samples(freq,dur, framerate))

    # output frames to file
    output_wave(path, frames, framerate)


# We'll use a low 4.41khz framerate for our audio to reduce the string length
framerate = 700000
beep_freq = 550 # Hz
beep_duration = 0.1 # seconds

# # We could just write a wav file directly
output_sound('dot.wav', beep_freq, beep_duration, framerate)
output_sound('dash.wav', beep_freq, beep_duration*3, framerate)
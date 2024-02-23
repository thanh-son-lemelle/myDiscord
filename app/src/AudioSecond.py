# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: $(filename)

@project: Colibri
@licence: GPLv3
"""
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write


# Sampling frequency
freq = 44100

# Recording duration
duration = 10

# Start recorder with the given values
# of duration and sample frequency
print("Sampling rate:", freq, "Hz")
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()
print("fin")

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
import wave
import numpy as np
from typing import Any

#partially written by ChatGPT, edited by me

# Parameters
sample_rate = 44100  # samples per second
duration = 2.0      # seconds

base_frequency= 440.0

#np.exp2(np.around(np.log2(np.arange(1,31+1))*41)/41)
#np.arange(1,31)

#note: the val includes the 1st harmonic
val = np.around(np.log2(np.arange(1,31+1))*15)
print(val)
relative_frequency_list = np.exp2(val/15)
frequency_list = base_frequency*relative_frequency_list

amp_list: np.ndarray[Any, np.float64] = np.array([1/(x**2) for x in range(1,31+1)])   # amps

# Generate the sine wave

t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
amplitude = np.iinfo(np.int16).max
added_amp = 0
added_sample=np.repeat(0,int(sample_rate * duration))
for frequency, amp in zip(np.nditer(frequency_list),amp_list,strict=True):
    solo_sample = (np.sin(2 * np.pi * frequency * t) * amp)
    added_sample = added_sample + solo_sample
    added_amp += amp
print(added_amp)

sample_normalized = (added_sample/added_amp*amplitude).astype(np.int16)

# Write to a WAV file
with wave.open('chord15edo.wav', 'w') as wf:
    wf.setnchannels(1)           # mono
    wf.setsampwidth(2)           # 2 bytes per sample
    wf.setframerate(sample_rate) # samples per second
    wf.writeframes(sample_normalized.tobytes())
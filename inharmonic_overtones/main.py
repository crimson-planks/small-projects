import wave, array, numpy as np

sample_rate = 44100  # samples per second
duration = 2.0      # seconds
frequency = 440.0   # sine frequency, Hz

audio_file = wave.open("audio.wav","wb")
audio_file.setnchannels(1)
audio_file.setsampwidth(2)
audio_file.setframerate(44100)
na= np.array(np.round(np.sin(np.arange(0,16,2**-8))*(2**16)),np.int16)
print(array.array("i",np.repeat(255,10)))
audio_file.writeframes(array.array("i",np.repeat(2**14+2**7,10)))
audio_file.close()
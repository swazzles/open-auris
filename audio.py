
import math
from pyaudio import PyAudio

def sine_tone(frequency, volume, sample_rate, duration):
    n_samples = int(sample_rate * duration)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))
    return bytearray(samples)

def play_audio(sampleset, sample_rate):
    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    for samples in sampleset:
        stream.write(bytes(samples))

    stream.stop_stream()
    stream.close()
    p.terminate()
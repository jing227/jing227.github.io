import matplotlib.pyplot as plt
import numpy as np
from thinkdsp import Chirp
from thinkdsp import normalize, unbias
from thinkdsp import decorate
from thinkdsp import read_wave
PI2 = 2 * np.pi
class SawtoothChirp(Chirp):
   

    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = PI2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / PI2
        frac, _ = np.modf(cycles)
        ys =  normalize(unbias(frac), self.amp)
        return ys
signal = SawtoothChirp(start=2500, end=3000)
wave =read_wave('1.wav')
wave.make_audio()
sp = wave.make_spectrogram(256)
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()

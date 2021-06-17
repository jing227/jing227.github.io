from thinkdsp import SawtoothSignal, Signal, Spectrum
import matplotlib.pyplot as plt
from thinkdsp import decorate

Signal = SawtoothSignal(200)
duration = Signal.period*3
segment = Signal.make_wave(duration,framerate=20000)
segment.plot()
decorate(xlabel='Time(s)')
plt.show()

plt.show()
wave = Signal.make_wave(duration = 0.5,framerate=10000)
wave.apodize()
wave.make_audio()
wave.write(filename='2-2.wav')

Spectrum = wave.make_spectrum()
Spectrum.plot()
decorate(xlabel='频谱(Hz)')
plt.show()

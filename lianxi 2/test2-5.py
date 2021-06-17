from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal
import os
import numpy as np
import matplotlib.pyplot as plt

def filter_spectrum(spectrum):

    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

#三角波  频率440HZ  波长0.5秒
wave = TriangleSignal(freq=440).make_wave(duration=0.1)

spectrum = wave.make_spectrum()
spectrum.plot(high=10000, color='red')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)

filtered = spectrum.make_wave()
filtered.make_audio()

filtered.write(filename='output2-5.wav')
plt.show()
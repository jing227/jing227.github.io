from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal
import os
import numpy as np
import matplotlib.pyplot as plt

#三角波
signal = TriangleSignal(amp=0.79)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=40000)
#三角波频谱  采样40000hz
spectrum = signal.make_wave(duration=0.5, framerate=40000)

#方波
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
square.make_spectrum().plot()

#生成锯齿波
class SawtoothSignal(Sinusoid):

    def evaluate(self, ts):
        cycles = self.freq * ts + self.offset / np.pi / 2
        frac, _ = np.modf(cycles)
        ys = normalize(unbias(frac), self.amp)
        return ys
#锯齿波频谱
sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)

#正常显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.subplot(311)
sawtooth.make_spectrum().plot()
plt.ylabel('幅度(锯齿波频谱)')
plt.xlabel('频率（HZ）')
plt.subplot(312)
spectrum.make_spectrum().plot()
plt.ylabel('幅度(三角波频谱)')
plt.xlabel('频率（HZ）')
plt.subplot(313)
square.make_spectrum().plot()
plt.ylabel('幅度(方波频谱)')
plt.xlabel('频率（HZ）')

plt.show()
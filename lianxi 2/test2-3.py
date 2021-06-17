from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal
import os
import numpy as np
import matplotlib.pyplot as plt

#方波频率1100HZ   采样10000HZ   波长0.5秒
square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)


square.write(filename='output2-3.wav')
#显示中文
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
square.make_spectrum().plot()
plt.ylabel('方波频谱幅度')
plt.xlabel('频率（HZ）')

plt.show()
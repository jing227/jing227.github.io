from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SquareSignal
import os
import numpy as np
import matplotlib.pyplot as plt

#三角波  频率440HZ  波长0.01秒
triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()

#  振幅为2v  相位为0
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])  #频率分量0

#  振幅为2v  垂直偏移1v
#spectrum.hs[0] = 100   #在频率为0处加上100分量  等于叠加一个100*（duration=0.01）==1v的直流信号
#triangle.plot(color='gray')
#spectrum.make_wave().plot()    

plt.show()
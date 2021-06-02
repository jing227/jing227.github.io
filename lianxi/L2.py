import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
plt.rcParams['font.sans-serif'] = ['KaiTi']# 指定默认字体楷体
plt.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
sin = thinkdsp.SinSignal(freq=400, amp=1.0)
cos = thinkdsp.CosSignal(freq=1200, amp=0.8)
signal = cos+sin
plt.subplot(121)
plt.title("复合信号")
signal.plot()
wave = signal.make_wave(duration=1)
spectrum = wave.make_spectrum()
plt.subplot(122)
plt.title("复合信号频谱")
spectrum.plot(high=2000)
wave.normalize()
wave.write("复合信号.wav")
play("复合信号.wav", flags=1)
plt.show()

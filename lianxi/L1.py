import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import time
def play(file, flags):
    print('Now play '+file)
    PlaySound(file, flags)
    print('end')
plt.rcParams['font.sans-serif'] = ['KaiTi']# 指定默认字体
plt.rcParams['axes.unicode_minus'] = False# 解决保存图像是负号'-'显示为方块的问题
wave = thinkdsp.read_wave('92002__jcveliz__violin-origional.wav')# 导入音频
plt.subplot(231)
plt.title("原音频")
wave.plot()

segment = wave.segment(start=1.5, duration=0.5)# 截取一段持续0.5s的音频
plt.subplot(232)
plt.title("截取的0.5s音频")
segment.plot()

# 绘制频谱
spectrum = segment.make_spectrum()
plt.subplot(233)
plt.title("截取的音频频谱")
plt.ylim(0, 1000)
spectrum.plot(high=8000)

# 低通
spectrum.low_pass(1000)
wave_lp = spectrum.make_wave()
wave_lp.write(filename='lowpass.wav')
plt.subplot(234)
plt.title("低通滤波1khz后的音频")
plt.ylim(0, 1000)
spectrum.plot(high=8000)
play('lowpass.wav', flags=1)
time.sleep(5)# 等待5s运行下一条语句

#高通
spectrum = segment.make_spectrum()
spectrum.high_pass(4000)
wave_hp = spectrum.make_wave()
wave_hp.write(filename='highpass.wav')
plt.subplot(235)
plt.title("高通滤波4khz音频")
plt.ylim(0, 1000)
spectrum.plot(high=8000)
play('wave_hp.wav', flags=1)
time.sleep(5)# 等待5s运行下一条语句

#带通
spectrum = segment.make_spectrum()
spectrum.band_stop(low_cutoff=1000 ,high_cutoff=4000)
wave_bp = spectrum.make_wave()
wave_bp.write(filename='bandstop.wav')
plt.subplot(236)
plt.title("带阻滤波1khz~4khz音频")
plt.ylim(0, 1000)
spectrum.plot(high=8000)
play('bandstop.wav', flags=1)
plt.show()
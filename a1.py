# -*- coding: UTF-8 -*- 
#coding=utf-8
 
import matplotlib.pyplot as plt #调用matplotlib的库并命名为plt
import numpy as np #导入nunpy并命名为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #0到3π区间100等分为x轴坐标
y = np.sin(x) #y轴的正弦函数

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #在第一行第二两列第一个位置显示图像
plt.title(r'$f(x)=sin(x)$')  #左侧图像的标题
plt.plot(x, y) #通过x,y描点画图
#plt.show() 

x1 = [t*0.375*np.pi for t in x] #循环把x坐标每个点*0.375π运算，形成新的x坐标
y1 = np.sin(x1) #y轴的正弦函数
plt.subplot(1,2,2)#在第一行第二两列第二个位置显示图像
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #右侧图像的标题
plt.plot(x, y1) #通过x,y1描点画图
plt.show()

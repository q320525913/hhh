import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()            #fig存放动画，ax是子图

x = np.arange(0,np.pi*2,0.1)        #获取0-6.28中间隔为0.1的所有数
y = np.tan(x)                       #正切函数
line, = ax.plot(x,y)                #在子图绘制出折线图

def init():
    line.set_ydata(np.tan(x))       #迭代x的成员饼返回正切值
    return line,

def animate(i):
    line.set_ydata(np.tan(x + i/10))#让增值尽量少的浮动
    return line,

ani = animation.FuncAnimation(fig=fig, func=animate,init_func=init, interval=20)
#init会传递成员数据给animate
plt.show()

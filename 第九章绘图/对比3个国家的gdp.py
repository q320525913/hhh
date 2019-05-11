import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('3个国家的gdp.csv')
list1 = []
list2 = []
list3 = []
list4 = []

for i in range(20):
    list1.append(float(data['美国'][i].split('亿')[0]))
    list2.append(float(data['中国'][i].split('亿')[0]))
    list3.append(float(data['日本'][i].split('亿')[0]))
    list4.append(int(data['gdp年份'][i].split('年')[0]))

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   #用来正常显示符号

plt.ylim(0,1400000)                        #定义y轴坐标范围
#marker坐标点的样式，mec是样式的颜色，mfc表示空心，ms是大小，label是图例
plt.plot(list4, list1, marker='o', mec='r', mfc='w',label='美国经济')
plt.plot(list4, list2, marker='*', ms=10,label='中国经济')
plt.plot(list4, list3, marker='*', ms=10,label='日本经济')
plt.legend()                               #生成图例
plt.show()








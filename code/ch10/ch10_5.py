# ch10_5.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([22, 26, 23, 28, 27, 32, 30])      # 温度
y = np.array([15, 35, 21, 62, 48, 101, 86])     # 饮料销售数量

a, b = np.polyfit(x, y, 1)                      # 回归直线
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))

y2 = a*x + b
plt.scatter(x, y)                               # 绘制散布图
plt.plot(x, y2)                                 # 绘制回归直线

sold = a*31 + b
print('气温31度时的销量 = {}'.format(int(sold)))
plt.plot(31, int(sold), '-o') 
plt.show()         
                  


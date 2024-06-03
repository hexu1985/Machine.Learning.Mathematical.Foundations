# ch10_3.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([1, 2, 3])                 # 拜访次数, 单位是100
y = np.array([5, 10, 20])               # 销售考卷数, 单位是100

a, b = np.polyfit(x, y, 1)              # 回归直线
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))

y2 = a*x + b
plt.scatter(x, y)                       # 绘制散布图
plt.plot(x, y2)                         # 绘制回归直线
plt.show()    


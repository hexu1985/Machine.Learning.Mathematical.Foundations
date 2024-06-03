# ch1_28.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 5, 500)                            # 建立含500个元素的数组
ypt = 1 - 0.5*np.abs(xpt-2)                             # y数组的变化
 
plt.scatter(xpt, ypt, s=50, c=xpt, cmap='hsv')          # 色彩随x轴值变化
plt.show()






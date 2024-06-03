# ch1_23.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 5, 500)                        # 建立含500个元素的数组
ypt = 1 - 0.5*np.abs(xpt-2)                         # y数组的变化
lwidths = (1+xpt)**2                                # 宽度数组  
plt.scatter(xpt, ypt, s=lwidths, color=(0, 1, 0))   # 绿色
plt.show()






# ch1_21.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)           # 建立含500个元素的数组
ypt1 = np.sin(xpt)                      # y数组的变化
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1, color=(0, 1, 0)) # 绿色
plt.scatter(xpt, ypt2)                  # 预设颜色
plt.show()






# ch2_7.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)           # 建立含500个元素的数组
ypt1 = np.sin(xpt)                      # y数组的变化
ypt2 = np.cos(xpt)

plt.plot(xpt, ypt1, label='sin')        # 预设颜色
plt.plot(xpt, ypt2, label='cos')        # 预设颜色
plt.xlabel('rad')
plt.ylabel('value')
plt.title('Sin and Cos function')
plt.grid()
plt.legend(loc='best')

plt.show()






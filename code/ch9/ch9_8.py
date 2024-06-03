# ch9_8.py
import matplotlib.pyplot as plt
import numpy as np

# 绘制此函数图形
x = np.linspace(-1, 1, 100)
y = x**3 - x
plt.plot(x, y)
plt.grid()
plt.show()














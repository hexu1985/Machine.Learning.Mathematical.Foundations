# ch17_2.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 1000, 100000)          # 建立含100000个元素的数组
y = [(1+1/x)**x for x in x]
#plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立图例
plt.grid()
plt.show()





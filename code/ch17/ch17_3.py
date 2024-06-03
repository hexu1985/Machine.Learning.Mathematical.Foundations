# ch17_3.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 10000)               # 建立含10000个元素的数组
y = [1/(1+np.e**-x) for x in x]
plt.axis([-5, 5, 0, 1])
plt.plot(x, y, label="Logistic function")

plt.legend(loc="best")                      # 建立图例
plt.grid()
plt.show()






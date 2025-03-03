# ch17_4.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 0.99, 100)               # 建立含1000个元素的数组
y = [np.log(x/(1-x)) for x in x]
plt.axis([0, 1, -5, 5])
plt.plot(x, y, label="Logit function")
plt.plot(0.5, np.log(0.5/(1-0.5)),'-o')

plt.legend(loc="best")                          # 建立图例
plt.grid()
plt.show()






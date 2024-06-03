# ch1_1.py
import matplotlib.pyplot as plt

x = [x for x in range(9)]       # 产生0, 1, ... 8列表
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(x, squares)            # 列表squares数据是y轴的值
plt.show()





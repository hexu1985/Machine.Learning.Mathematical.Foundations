# ch1_6.py
import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares, lw=10)       # 列表squares数据是y轴的值, 线条宽度是10
plt.title('Test Chart', fontsize=24)
plt.xlabel('Value', fontsize=16)
plt.ylabel('Square', fontsize=16)
plt.show()




# ch1_3.py
import matplotlib.pyplot as plt

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)           # 列表squares数据是y轴的值
plt.axis([0, 8, 0, 70])     # x轴刻度0-8, y轴刻度0-70
plt.show()		




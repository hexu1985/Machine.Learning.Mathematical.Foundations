# ch5_2.py
import matplotlib.pyplot as plt                                 
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.xticks(x)                           # 标记每个单一x数字
plt.axis([0, 10, -20, 15])              # 标记刻度范围
plt.plot(x, y, '-*')   
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加网格线
plt.show()




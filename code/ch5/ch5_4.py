# ch5_4.py
import matplotlib.pyplot as plt
                                
x = [x for x in range(0, 11)]
y = [2 * y for y in x]
plt.xticks(x)
plt.axis([0, 10, 0, 20])                # 标记刻度范围
plt.plot(x, y)   
plt.grid()                              # 加网格线
plt.show()




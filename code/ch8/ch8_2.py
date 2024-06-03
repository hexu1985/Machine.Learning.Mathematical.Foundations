# ch8_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.plot([0, 0], [20, 0])              # 绘函数直线公式 1
plt.plot([0, 0], [0, 20])              # 绘函数直线公式 2
                                
line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * y) for y in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * y) for y in line4_x]

lineobj_x = np.linspace(0, 20, 20)
lineobj_y = [10 - y for y in lineobj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)              # 绘函数直线公式 3
plt.plot(line4_x, line4_y)              # 绘函数直线公式 4
plt.plot(lineobj_x, lineobj_y)          # 绘目标函数直线公式

plt.plot(5, 5, '-o')                    # 绘交叉点
plt.text(4.5, 5.5, '(5, 5)')            # 输出(5, 5)
plt.xlabel("Research")
plt.ylabel("UI")
plt.grid()                              # 加网格线
plt.show()








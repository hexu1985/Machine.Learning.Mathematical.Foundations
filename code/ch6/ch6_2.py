# ch6_2.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
a = Symbol('a')                 # 定义公式中使用的变量
b = Symbol('b')                 # 定义公式中使用的变量
eq1 = a + b - 1                 # 方程式 1
eq2 = 5 * a + b - 2             # 方程式 2
ans = solve((eq1, eq2))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))

pt_x1 = 600                             
pt_y1 = ans[a] * pt_x1 + ans[b]         # 计算x=600时的y值
pt_x2 = 1000
pt_y2 = ans[a] * pt_x2 + ans[b]         # 计算x=1000时的y值

x = np.linspace(0, 2500, 250)
y = ans[a] * x + ans[b]
plt.plot(x, y)                          # 绘函数直线
plt.plot(pt_x1, pt_y1, '-o')            # 绘点 pt1
plt.text(pt_x1+60, pt_y1-10, 'pt1')     # 输出文字pt1
plt.plot(pt_x2, pt_y2, '-o')            # 绘点 pt2
plt.text(pt_x2+60, pt_y2-10, 'pt2')     # 输出文字pt2
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                              # 加网格线
plt.show()








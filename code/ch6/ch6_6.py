# ch6_6.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np
                                
x = Symbol('x')                         # 定义公式中使用的变量
y = Symbol('y')                         # 定义公式中使用的变量
eq1 = x + y - 100                       # 方程式 1
eq2 = 2 * x + 4 * y - 350               # 方程式 2
ans = solve((eq1, eq2))
print('菜鸟业务员须外出天数 = {}'.format(ans[x]))
print('资深业务员须外出天数 = {}'.format(ans[y]))

line1_x = np.linspace(0, 100, 100)
line1_y = [100 - y for y in line1_x]
line2_x = np.linspace(0, 100, 100)
line2_y = [(350 - 2 * y) / 4 for y in line2_x]

plt.plot(line1_x, line1_y)              # 绘函数直线公式 1
plt.plot(line2_x, line2_y)              # 绘函数直线公式 2

plt.plot(ans[x], ans[y], '-o')          # 绘交叉点
plt.text(ans[x]-5, ans[y]+5, '('+str(ans[x])+','+str(ans[y])+')')
plt.xlabel("Junior Salesman")
plt.ylabel("Senior Salesman")
plt.grid()                              # 加网格线
plt.show()









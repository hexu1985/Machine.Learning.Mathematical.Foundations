# ch9_11.py
import matplotlib.pyplot as plt
from sympy import Symbol, solve
import numpy as np

a = Symbol('a')                         # 定义公式中使用的变量
b = Symbol('b')                         # 定义公式中使用的变量
c = Symbol('c')                         # 定义公式中使用的变量
eq1 = a + b + c - 500                   # 第100次公式
eq2 = 4*a + 2*b + c - 1000              # 第200次公式
eq3 = 9*a + 3*b + c - 2000              # 第300次公式
ans = solve((eq1, eq2, eq3))
print('a = {}'.format(ans[a]))
print('b = {}'.format(ans[b]))
print('c = {}'.format(ans[c]))

x = np.linspace(0, 5, 50)
y = [(ans[a]*y**2 + ans[b]*y + ans[c]) for y in x]
plt.plot(x, y)                          # 绘二次函数

x4 = 4                                  # 第400次
y4 = ans[a]*x4**2 + ans[b]*x4 + ans[c]  # 第400次的y值
plt.plot(x4, y4, '-o')                  # 绘交叉点
plt.text(x4-0.7, y4-50, '('+str(x4)+','+str(y4)+')')

plt.plot(1, 500, '-x', color='b')       # 绘100次业绩点
plt.text(1-0.7, 500-50, '('+str(1)+','+str(500)+')')
plt.plot(2, 1000, '-x', color='b')      # 绘200次业绩点
plt.text(2-0.7, 1000-50, '('+str(2)+','+str(1000)+')')
plt.plot(3, 2000, '-x', color='b')      # 绘300次业绩点
plt.text(3-0.7, 2000-50, '('+str(3)+','+str(2000)+')')

plt.xlabel("Times(unit=100)")
plt.ylabel("Revenue")
plt.grid()                              # 加网格线
plt.show()











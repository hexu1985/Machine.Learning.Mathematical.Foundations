# ch9_6.py
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
import numpy as np

def f(x):
    ''' 求解方程式 '''
    return (3*x**2 - 12*x + 10)

a = 3
b = -12
c = 10
r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)         # r1
r1_y = f(r1)                                # f(r1)
plt.text(r1+0.1, r1_y-0.2, '('+str(round(r1,2))+','+str(0)+')')         
plt.plot(r1, r1_y, '-o')                    # 标记
print('root1 = ', r1)                       # print(r1)
r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)         # r2
r2_y = f(r2)                                # f(r2)
plt.text(r2-0.6, r2_y-0.2, '('+str(round(r2,2))+','+str(0)+')') 
plt.plot(r2, r2_y, '-o')                    # 标记
print('root2 = ', r2)                       # print(r2)

# 计算最小值
r = minimize_scalar(f)
print("当x是 %4.2f 时, 有函数最小值 %4.2f" % (r.x, f(r.x)))
plt.text(r.x-0.25, f(r.x)+0.3, '('+str(round(r.x,2))+','+str(round(r.x,2))+')') 
plt.plot(r.x, f(r.x), '-o')                 # 标记

# 绘制此函数图形
x = np.linspace(0, 4, 50)
y = 3*x**2 - 12*x + 10
plt.plot(x, y, color='b')
plt.show()














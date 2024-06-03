# ch6_4.py
import matplotlib.pyplot as plt
import numpy as np                            
a = 0.03
b = -18
x = np.linspace(0, 2500, 250)
y = a * x + b
pt_y = 48
pt_x = (pt_y + 18) / 0.03 
print('获利48万需有 {} 来客数'.format(int(pt_x)))
plt.plot(x, y)                                      # 绘函数直线
plt.plot(pt_x, pt_y, '-o')                          # 绘点
plt.text(pt_x-150, pt_y+3, '('+str(int(pt_x))+','+str(pt_y)+')')   
plt.xlabel("Customers")
plt.ylabel("Profit")
plt.grid()                                          # 加网格线
plt.show()








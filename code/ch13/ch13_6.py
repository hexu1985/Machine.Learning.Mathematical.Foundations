# ch13_6.py
import random
import math
import matplotlib.pyplot as plt

trials = 5000
Hits = 0
radius = 50
for i in range(trials):
    x = random.randint(1, 100)                      # x轴坐标
    y = random.randint(1, 100)                      # y轴坐标
    if math.sqrt((x-50)**2 + (y-50)**2) < radius:   # 在圆内
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')
plt.show()













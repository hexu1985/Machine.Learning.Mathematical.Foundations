# ch13_15.py
import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x轴坐标
    y = random.random() * 2 - 1     # y轴坐标
    if x * x + y * y <= 1:          # 判断是否在圆内
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)










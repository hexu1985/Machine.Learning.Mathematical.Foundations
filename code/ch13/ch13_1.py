# ch13_1.py
import random           # 导入模块random

min = 1
max = 6
target = 5
n = 10000
counter = 0
for i in range(n):
    if target == random.randint(min, max):
        counter += 1
print('经过 {} 次, 得到 {} 次 {}'.format(n, counter, target))
P = counter / n
print('机率 P = {}'.format(P))







        


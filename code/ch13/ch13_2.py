# ch13_2.py
import matplotlib.pyplot as plt
from random import randint

min = 1
max = 6                                         # 骰子有几面
times = 10000                                   # 掷骰子次数

dice = [0] * 7                                  # 建立掷骰子的列表
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
    
del dice[0]                                     # 删除索引0数据
    
for i, c in enumerate(dice, 1):
    print('{} = {} 次'.format(i, c))
    
x = [i for i in range(1, max+1)]                # 直方图x轴坐标
width = 0.35                                    # 直方图宽度
plt.bar(x, dice, width, color='g')              # 绘制直方图
plt.ylabel('Frequency')
plt.title('Test 10000 times')
plt.show()






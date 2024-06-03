# ch15_2.py
base = 100
rate = 1
hour = 10
for i in range(1, hour+1):
    base = base + base*rate
    print('经过 {0:2d} 小时后累积病毒量 {1}'.format(i,base))














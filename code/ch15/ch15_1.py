# ch15_1.py
base = 10000
rate = 0.03
year = 10
for i in range(1, year+1):
    base = base + base*rate
    print('经过 {0:2d} 年后累积金额 {1:6.2f}'.format(i,base))














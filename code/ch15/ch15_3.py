# ch15_3.py
base = 100
rate = 0.1
year = 3
for i in range(1, year+1):
    base = base - base*rate
    print('经过 {} 年后车辆残值 {}'.format(i,base))














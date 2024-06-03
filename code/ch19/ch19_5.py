# ch19_5.py

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 计算变异数
var = 0
for v in x:
    var += ((v - mean)**2)
sd = (var / len(x))**0.5
print("标准偏差 : {0:6.2f}".format(sd))







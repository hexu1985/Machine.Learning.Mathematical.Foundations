# ch19_3.py

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 计算变异数
var = 0
for v in x:
    var += ((v - mean)**2)
var = var / len(x)
print("变异数 : ", var)







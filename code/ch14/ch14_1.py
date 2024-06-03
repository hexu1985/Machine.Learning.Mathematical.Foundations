# ch14_1.py
import matplotlib.pyplot as plt
import math 
def probability(k):
    num = (math.factorial(n))/(math.factorial(n-k)*math.factorial(k))
    pro = num * success**k * (1-success)**(n-k)
    return pro
    
n = 5                                           # 销售次数                       # 成功机率
success = 0.75                                  # 销售成功机率
fail = 1 - success                              # 销售失败机率
p = []                                          # 储存成功机率

for k in range(0,n+1):
    if k == 0:
        p.append(fail**n)                       # 连续n次失败机率
        continue
    if k == n:
        p.append(success**n)                    # 连续n次成功机率
        continue
    p.append(probability(k))                    # 计算其他次成功机率

for i in range(len(p)):
    print('销售 {} 单位成功机率 {}%'.format(i, p[i]*100))
        
x = [i for i in range(0, n+1)]                  # 直方图x轴坐标
width = 0.35                                    # 直方图宽度
plt.xticks(x)
plt.bar(x, p, width, color='g')                 # 绘制直方图
plt.ylabel('Probability')
plt.xlabel('unit:100')
plt.title('Binomial Dristribution')
plt.show()






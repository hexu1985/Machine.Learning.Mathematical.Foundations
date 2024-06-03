# ch1_19.py
import matplotlib.pyplot as plt

xpt = list(range(1,101))                # 建立1-100序列x坐标点
ypt = [x**2 for x in xpt]               # 以x平方方式建立y坐标点
plt.axis([0, 100, 0, 10000])            # 留意参数是列表
plt.scatter(xpt, ypt, color=(0, 1, 0))  # 绿色
plt.show()






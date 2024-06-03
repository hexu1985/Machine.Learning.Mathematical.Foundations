# ch15_4.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 5, 5)                  # 建立含10个元素的数组
ypt1 = xpt / xpt                            # 时间复杂度是 O(1)
ypt2 = np.log2(xpt)                         # 时间复杂度是 O(logn)               
ypt3 = xpt                                  # 时间复杂度是 O(n)
ypt4 = xpt * np.log2(xpt)                   # 时间复杂度是 O(nlogn)
ypt5 = xpt * xpt                            # 时间复杂度是 O(n*n)
plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.plot(xpt, ypt4, '-o', label="O(nlogn)")
plt.plot(xpt, ypt5, '-o', label="O(n*n)")
plt.legend(loc="best")                      # 建立图例
plt.axis('equal')
plt.show()






# ch16_1.py
import numpy as np

n = np.linspace(1.1, 10, 90)            # 建立1.1-10的数组
count = 0                               # 用于计算每5笔输出换行
for i in n:
    count += 1
    print('{0:2.1f} = {1:4.3f}'.format(i, np.log10(i)), end='    ')
    if count % 5 == 0:                  # 每5笔输出就换行
        print()









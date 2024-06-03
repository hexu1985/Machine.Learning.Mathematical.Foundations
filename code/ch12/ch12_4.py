# ch12_4.py
import math

N = 30
times = 10000000000000              # 计算机每秒可处理数列数目
day_secs = 60 * 60 * 24             # 一天秒数
year_secs = 365 * day_secs          # 一年秒数
combinations = math.factorial(N)    # 组合方式
years = combinations / (times * year_secs)
print("需要 %d 年才可以获得结果" % years)







    

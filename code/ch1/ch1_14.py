# ch1_14.py
import matplotlib.pyplot as plt

Benz = [3367, 4120, 5539]               # Benz线条
BMW = [4000, 3590, 4423]                # BMW线条
Lexus = [5200, 4930, 5350]              # Lexus线条

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 设定x轴刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend(loc='best')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.savefig('out1_14.jpg', bbox_inches='tight')
plt.show()



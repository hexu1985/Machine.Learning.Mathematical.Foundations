# ch12_1.py
import itertools
n = {1, 2, 3, 4}
r = 3
A = set(itertools.permutations(n, 3))
print('元素数量 = {}'.format(len(A)))
for a in A:
    print(a)












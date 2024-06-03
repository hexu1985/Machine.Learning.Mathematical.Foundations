# ch12_3.py
import itertools
n = {'A', 'B', 'C', 'D', 'E'}
r = 5
A = set(itertools.permutations(n, 5))
print('业务员路径数 = {}'.format(len(A)))
for a in A:
    print(a)












# ch12_2.py
import itertools
n = {'a', 'b', 'c', 'd', 'e'}
r = 2
A = set(itertools.permutations(n, 2))
print('基因配对组合数量 = {}'.format(len(A)))
for a in A:
    print(a)












# ch11_4.py 
math = {'Kevin', 'Peter', 'Eric'}       # 设定参加数学夏令营成员
physics = {'Peter', 'Nelson', 'Tom'}    # 设定参加物理夏令营成员
allmember1 = math | physics
print("参加数学或物理夏令营的成员 ",allmember1)
allmember2 = math.union(physics)
print("参加数学或物理夏令营的成员 ",allmember2)




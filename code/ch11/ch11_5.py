# ch11_5.py 
math = {'Kevin', 'Peter', 'Eric'}       # 设定参加数学夏令营成员
physics = {'Peter', 'Nelson', 'Tom'}    # 设定参加物理夏令营成员
math_only1 = math - physics
print("参加数学夏令营同时没有参加物理夏令营的成员 ",math_only1)
math_only2 = math.difference(physics)
print("参加数学夏令营同时没有参加物理夏令营的成员 ",math_only2)
physics_only1 = physics - math
print("参加物理夏令营同时没有参加数学夏令营的成员 ",physics_only1)
physics_only2 = physics.difference(math)
print("参加物理夏令营同时没有参加数学夏令营的成员 ",physics_only2)





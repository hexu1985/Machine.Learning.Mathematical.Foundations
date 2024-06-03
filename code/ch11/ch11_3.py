# ch11_3.py 
math = {'Kevin', 'Peter', 'Eric'}       # 设定参加数学夏令营成员
physics = {'Peter', 'Nelson', 'Tom'}    # 设定参加物理夏令营成员
both1 = math & physics
print("同时参加数学与物理夏令营的成员 ",both1)
both2 = math.intersection(physics)
print("同时参加数学与物理夏令营的成员 ",both2)




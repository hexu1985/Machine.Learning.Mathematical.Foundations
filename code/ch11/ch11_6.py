# ch11_6.py 
math = {'Kevin', 'Peter', 'Eric'}       # 设定参加数学夏令营成员
physics = {'Peter', 'Nelson', 'Tom'}    # 设定参加物理夏令营成员
math_sydi_physics1 = math ^ physics
print("没有同时参加数学和物理夏令营的成员 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("没有同时参加数学和物理夏令营的成员 ",math_sydi_physics2)






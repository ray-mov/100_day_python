import random

randNum = random.randint(0,1)

if randNum == 1:
  print("Head")
else:
  print("Tail")

# a: the lower bound (inclusive)

# b: the upper bound (inclusive)

print(randNum)


import my_module
print(my_module.my_fav_num)

random_float = random.random()   #0.0 <= x < 1.0
print(random_float * 10)      

random_float_1 = random.uniform(1,10)  # a <= x <= b
print(random_float * 10)      
print(random_float_1)
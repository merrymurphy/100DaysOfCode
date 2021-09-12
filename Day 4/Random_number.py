import random
import my_module

random_int=random.randint(1,10)
print(random_int)
#returns a random float number between 0 and 10
#this function doesn't takes arguments.
random_float=random.random()
print(random_float)

random_float*5
#will give random float numbers from 0.00000 to 4.999999 but not 5
print(my_module.pi)
#returns a random float number within a given range
random_f=random.uniform(1,5)
print(random_f)

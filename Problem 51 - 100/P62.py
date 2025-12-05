#Create a list of 10 random numbers and sort it in ascending order

import random

LIST = list(range(1001))
Num_List = random.sample(LIST, k=10)

Num_List.sort()
print(Num_List)




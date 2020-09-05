#Remember import random function here:
import random


my_list = [4,5,734,43,45]

for i in range(10):
    my_list.append(random.randint(1, 99))
    i += i
    print(my_list)





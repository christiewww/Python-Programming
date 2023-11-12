# by Christie (no function)

import random
from random import randint

random_num = random.randint(1,10)
expression = int(input("Enter an interger between 1 and 10 (1 and 10 included): \n"))
limit1 = 9
count1 = 0

while expression != random_num:
    if count1 < limit1:
        expression = int(input("Not right! Re-enter a number between 1 and 10 (1 and 10 included): \n"))
        count1 += 1
    else:
        print("You lose!")
        break
else:
    print("You guess right!")
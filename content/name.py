import random
import math

loop = True
chars = 'bcdfghjklmnpqrstvwxyz'

while loop:
    for x in range(5,11):
        s = ""
        for y in range(math.ceil(x/2)):
            s += random.choice(chars)
        print(s)

    x = input("r to Restart, empty to exit:")
    if x=='r':
        loop = True
    else:
        loop = False
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
o = number % 10 if number > 10 else number % -10
if o > 5:
    ou = "and is greater than 5"
elif o == 0:
    ou = "and is 0"
elif o < 6 and o != 0:
    ou = "and is less than 6 and not 0"
print(f"Last digit of {number} is {o} {ou}")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if str(number)[-1] > "5":
    o = "and is greater than 5"
elif str(number)[-1] == "0":
    o = "and is 0"
elif str(number)[-1] < "6" and str(number)[-1] != "0":
    o = "and is less than 6 and not 0"
print(f"Last digit of {number} is {str(number)[-1]} {o}")

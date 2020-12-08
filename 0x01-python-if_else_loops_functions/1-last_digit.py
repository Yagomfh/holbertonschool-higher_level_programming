#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
fWords = "Last digit of "
if number < 0:
    number = -number
    lD = number % 10
    lD = -lD
    number = -number
else:
    lD = number % 10
if lD > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lD))
elif lD == 0:
    print("Last digit of {} is {} and is 0".format(number, lD))
else:
    print("{}{} is {} and is less than 6 and not 0".format(fWords, number, lD))

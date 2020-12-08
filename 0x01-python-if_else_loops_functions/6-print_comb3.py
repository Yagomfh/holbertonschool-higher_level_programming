#!/usr/bin/python3
i = 0
a = 0
while i < 10:
    j = 1 + a
    while j < 10:
        if i == 8 and j == 9:
            print("{}".format(89))
        else:
            print("{}{}, ".format(i, j), end='')
        j += 1
    i += 1
    a += 1

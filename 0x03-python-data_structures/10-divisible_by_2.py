#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return a

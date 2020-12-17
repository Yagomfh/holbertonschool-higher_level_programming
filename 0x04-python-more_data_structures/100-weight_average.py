#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    if my_list:
        mul = []
        for elem in my_list:
            a = 1
            for nb in elem:
                a *= nb
            mul.append(a)
        for nb in mul:
            res += nb
        weight = 0
        for nb in my_list:
            weight += nb[1]
        res = res / weight
    return res

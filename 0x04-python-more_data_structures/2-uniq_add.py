#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = my_list
    new = list(dict.fromkeys(new))
    result = 0
    for x in new:
        result += x
    return result

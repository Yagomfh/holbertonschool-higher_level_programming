#!/usr/bin/python3
def max_integer(my_list=[]):
    tmp = my_list.copy()
    tmp.sort()
    l = len(tmp)
    if l == 0:
        return None
    else:
        return tmp[l - 1]

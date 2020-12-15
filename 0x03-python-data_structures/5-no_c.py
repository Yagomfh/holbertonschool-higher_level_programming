#!/usr/bin/python3
def no_c(my_string):
    c = my_string.count('c')
    while c > 0:
        my_string = my_string.replace('c', '')
        c -= 1
    C = my_string.count('C')
    while C > 0:
        my_string = my_string.replace('C', '')
        C -= 1
    return my_string

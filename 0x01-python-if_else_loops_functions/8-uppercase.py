#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96:
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print("{}".format(c), end='' if i + 1 < len(str) else "\n")

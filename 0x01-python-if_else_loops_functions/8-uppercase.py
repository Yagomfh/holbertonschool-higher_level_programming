#!/usr/bin/env python3
def uppercase(str):
    tmp = ""
    for c in str:
        if ord(c) > 96:
            tmp = tmp + chr(ord(c) - 32)
        else:
            tmp = tmp + c
    print("{}".format(tmp))

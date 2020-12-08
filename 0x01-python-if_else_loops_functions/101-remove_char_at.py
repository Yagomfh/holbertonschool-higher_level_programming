#!/usr/bin/python3
def remove_char_at(str, n):
    tmp = ""
    for i in range(len(str)):
        if i == n:
            continue
        tmp += str[i]
    return tmp

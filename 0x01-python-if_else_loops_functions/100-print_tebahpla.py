#!/usr/bin/python3
i = 122
tmp = ""
while i >= 97:
    if i % 2 == 0:
        tmp += chr(i)
    else:
        tmp += chr(i - 32)
    i -= 1
print("{}".format(tmp), end='')

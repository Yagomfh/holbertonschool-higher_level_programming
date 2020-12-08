#!/usr/bin/python3
i = chr
for i in range(ord('a'), ord('z') + 1):
    if i == 113 or i == 101:
        continue
    print(chr(i), end='')

#!/usr/bin/env python3
def pow(a, b):
    result = a
    for i in range(1, b if b > 0 else -b):
            result = result * a
    if b == 0:
        return 1
    if b < 0:
        result = 1 / result
    return result

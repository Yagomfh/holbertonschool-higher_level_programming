#!/usr/bin/python3
"""Module Pascal's Triangle"""


def pascal_triangle(n):
    """rReturns a list of lists of integers
    representing the Pascal’s triangle of n"""
    res = []
    if n <= 0:
        return []
    for x in range(1, n + 1):
        c = 1
        res.append([])
        for y in range(1, x + 1):
            res[x - 1].append(c)
            c = int(c * (x - y) / y)
    return res

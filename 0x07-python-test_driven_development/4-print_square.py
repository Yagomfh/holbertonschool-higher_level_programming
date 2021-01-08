#!/usr/bin/python3
"""Module that prints a square with the character #

Raises:
    TypeError: if size not an int or size < 0
    and size is float and < 0
"""


def print_square(size):
    """Function that prints a square with the character #

    Args:
        size(int)
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()

#!/usr/bin/python3
"""Module that that adds 2 integers.

Raises:
    TypeError: if a or b are not int or floats
"""


def add_integer(a, b=98):
    """Function that adds 2 integers

    Args:
        a (int/float): first digit
        b (int/float): second digit

    Returns:
        Int sum of both digits
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)

#!/usr/bin/python3
"""Module that prints My name is <first name> <last name>

Raises:
    TypeError: if first_name or last_name are not strings
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))

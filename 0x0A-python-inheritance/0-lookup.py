#!/usr/bin/python3
'''Module that returns the list of available
attributes and methods of an object'''


def lookup(obj):
    '''Function that returns the list of available
    attributes and methods of an object

    Args:
        obj: the object to list

    Return: a list
    '''
    return dir(obj)

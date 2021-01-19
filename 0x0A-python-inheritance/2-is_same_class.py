#!/usr/bin/python3
'''Module to find if object is exactly
an instance of the specified class'''


def is_same_class(obj, a_class):
    '''Fundtion to find if object is exactly
    an instance of the specified class

    Args:
        obj: the object to test
        a_class: a type to test

    Return: True or false
    '''
    return type(obj) is a_class

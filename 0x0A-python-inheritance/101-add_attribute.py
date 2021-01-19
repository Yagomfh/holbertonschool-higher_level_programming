#!/usr/bin/python3
"""Module to add attributes if possible"""


def add_attribute(obj, name, value):
    '''Function that adds a new attribute
    to an object if it’s possible'''
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

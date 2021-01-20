#!/usr/bin/python3
"""Module of class Student"""


class Student:
    """Class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Function init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function class to JSON"""
        adict = self.__dict__
        res = {}
        if attrs is None:
            return adict
        for item in adict:
            if item in attrs:
                res[item] = adict[item]
        return res

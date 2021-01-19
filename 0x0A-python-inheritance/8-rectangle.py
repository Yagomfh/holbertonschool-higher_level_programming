#!/usr/bin/python3
'''Module for class BaseGeometry'''


class BaseGeometry:
    '''Class BaseGeometry'''
    def area(self):
        '''Public instance method: raises an Exception'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Public instance method: that validates value'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    '''Sub-class Rectangle'''
    def __init__(self, width, height):
        '''Init method'''
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

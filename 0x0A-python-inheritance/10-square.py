#!/usr/bin/python3
'''Module for class BaseGeometry'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Sub-class (of Rectangle) Square'''
    def __init__(self, size):
        '''Init method'''
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

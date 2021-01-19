#!/usr/bin/python3
'''Module for class BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Sub-class Rectangle'''

    def __init__(self, width, height):
        '''Init method'''
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

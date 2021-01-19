#!/usr/bin/python3
'''Module for class BaseGeometry'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Sub-class (of Rectangle) Square'''
    def __init__(self, size):
        '''Init method'''
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        '''Returns the area of the square'''
        return self.__size ** 2

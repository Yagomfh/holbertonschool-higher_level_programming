#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle():
    """This class defines a empty rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialise a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Output for end user: a rectangle

        Returns: a string
        """
        res = ""
        for y in range(self.height):
            for x in range(self.width):
                res += '#'
            if y != self.height - 1:
                res += '\n'
        return res

    def __repr__(self):
        """Output for developer: info about the class and its storage in mem

        Returns: a string
        """
        return 'Rectangle(%d, %d)' % (self.width, self.height)

    def __del__(self):
        """Deletes a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Function that returns the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @property
    def width(self):
        """Gets/sets width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets/sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

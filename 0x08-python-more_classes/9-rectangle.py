#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle():
    """This class defines a empty rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
        res = "{}".format('\n'.join([str(self.print_symbol) * self.__width
                          for row in range(0, self.__height)]))
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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method function that returns
         the biggest rectangle based on the area.

         Args:
            rect_1: rectangle instance n1
            rect_2: rectangle instance n2

        Returns: rect_1 if both have the same area value
        or the instance with the bieggest area.
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        area1 = rect_1.width * rect_1.height
        area2 = rect_2.width * rect_2.height
        if area2 > area1:
            return rect_2
        else:
            return rect_1
    
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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

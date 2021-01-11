#!/usr/bin/python3
"""
Rectangle Module - Contains simple class definition of Rectangle Class
"""


class Rectangle:
    """
    Rectangle Class : simple implementation
    """

    def __init__(self, width=0, height=0):
        """
        Rectangle : initialize a rectangle
        Attributes :
        Private instance attribute: width must be positive integer
        Private instance attribute: height must be positive integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for the width attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for the height attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

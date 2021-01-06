#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class Square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
    def __new__(self, size):
        return size
    def area(self):
        """Calculates the area of a square.

        Returns: the size raise to the power of two
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

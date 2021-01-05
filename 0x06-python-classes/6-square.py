#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """A class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.

        Raises:
            TypeError: if size is not an int
            ValueError: if size is < 0
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

    def area(self):
        """Calculates the area of a square.

        Returns: the size raise to the power of two
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square."""
        size = self.__size
        pos = self.__position
        for a in range(pos[1]):
            print("")
        for x in range(size):
            for b in range(pos[0]):
                print(" ", end='')
            for y in range(size):
                print("#", end='')
            print("")
        if size == 0:
            print("")

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

    @property
    def position(self):
        """Get/set the current position of the square."""
        return slef.__size

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and value[0] >= 0:
                if isinstance(value[1], int) and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

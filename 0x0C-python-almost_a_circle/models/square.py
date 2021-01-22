#!/usr/bin/python3
"""Module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method __str__"""
        return "[Square] ({}) {}/{} \
- {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

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

    def update(self, *args, **kwargs):
        """Update attributes method"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "size":
                        self.size = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

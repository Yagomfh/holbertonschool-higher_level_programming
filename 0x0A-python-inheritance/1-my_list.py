#!/usr/bin/python3
"""
MyList class and print sorted function
"""


class MyList(list):
    """ Simple list Class"""

    def print_sorted(self):
        """ Print the list in sorted order"""
        print(sorted(self))

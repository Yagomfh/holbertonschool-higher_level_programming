#!/usr/bin/python3
'''Module class MyList that inherits from list'''


class MyList(list):
    '''A class MyList that inherits from list'''

    def print_sorted(self):
        '''Public instance method that prints the list
        but sorted (ascending sort)'''
        Sorted = self[:]
        Sorted.sort()
        print(Sorted)

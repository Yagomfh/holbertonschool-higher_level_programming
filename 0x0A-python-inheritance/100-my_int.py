#!/usr/bin/python3
'''Module MyInt'''


class MyInt(int):
    '''A class MyInt that inherits from int'''
    def __init__(self, a):
        '''Init method'''
        self.a = a

    def __eq__(self, other):
        '''Equal method'''
        if self.a == other:
            return False
        else:
            return True

    def __ne__(self, other):
        '''Not equal method'''
        if self.a != other:
            return False
        else:
            return True

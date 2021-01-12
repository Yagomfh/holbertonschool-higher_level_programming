#!/usr/bin/python3
"""This module creates a LockedClass"""


class LockedClass:
    """Class that locks out every attribute declaration
    that is not 'first_name'"""
    __slots__ = ['first_name']

#!/usr/bin/python3
"""Module class_to_json"""


def class_to_json(obj):
    """Coverts a class into a JSON dict"""
    return vars(obj)

#!/usr/bin/python3
"""Module save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Function write Object to a text file in JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

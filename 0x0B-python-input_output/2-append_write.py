#!/usr/bin/python3
"""Module append_write"""


def append_write(filename="", text=""):
    """Function that appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        c_w = f.write(text)
        f.close()
    return c_w

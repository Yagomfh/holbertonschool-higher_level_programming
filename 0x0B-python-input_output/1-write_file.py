#!/usr/bin/python3
"""Module write_file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as File:
        c_w = File.write(text)
        File.close()
    return c_w

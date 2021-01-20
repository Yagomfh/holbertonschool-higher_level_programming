#!/usr/bin/python3
"""Module append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file
    after each line containing a specific string"""
    res = ""
    with open(filename, "r") as f:
        for line in f:
            res += line
            if search_string in line:
                res += new_string
        f.close()
    with open(filename, "w") as f:
        f.write(res)
        f.close()

#!/usr/bin/python3
"""Module that prints a text with 2 new lines
after each of these characters: ., ? and :

Raises:
    TypeError: if text is not a string
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each of these

    args:
        test (str): string to be parsed
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    tmp = ""
    for c in text:
        tmp += c
        if c in ".?:":
            tmp += '\n'
            tmp = tmp.lstrip()
            print("{}".format(tmp))
            tmp = ""
    tmp = tmp.lstrip()
    print("{}".format(tmp), end='')

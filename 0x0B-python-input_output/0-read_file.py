#!/usr/bin/python3
"""Read_file module"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as File:
        print(File.read())
        File.close()

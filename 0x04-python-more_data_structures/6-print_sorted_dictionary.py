#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d_sorted = sorted(a_dictionary)
    for x in d_sorted:
        print("{}: {}".format(x, a_dictionary[x]))

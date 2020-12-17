#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = []
    for k, v in a_dictionary.items():
        if v == value:
            todel.append(k)
    if todel:
        for key in todel:
            del a_dictionary[key]
    return a_dictionary

#!/usr/bin/python3
def multiple_returns(sentence):
    ls = len(sentence)
    if ls == 0:
        c = None
    else:
        c = sentence[0]
    result = ls, c
    return result

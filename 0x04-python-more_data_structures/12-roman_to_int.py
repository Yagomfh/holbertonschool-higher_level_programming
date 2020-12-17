#!/usr/bin/python3
def find_bigger_number(tocheck, nb, idx):
    for x in range(idx, len(tocheck)):
        if nb < tocheck[x]:
            return True
    return False


def roman_to_int(roman_string):
    res = 0
    if roman_string and type(roman_string) is str:
        rlist = list(roman_string)
        rdi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(roman_string) - 1):
            c = roman_string[i]
            c_next = roman_string[i + 1]
            if rdi[c] > rdi[c_next]:
                res -= rdi[c]
            else:
                res += rdi[c]
        res += rdi[roman_string[len(roman_string) - 1]]
        return res
    return res

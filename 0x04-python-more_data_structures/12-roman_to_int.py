#!/usr/bin/python3
def find_bigger_number(tocheck, nb, idx):
    for x in range(idx, len(tocheck)):
        if nb < tocheck[x]:
            return True
    return False


def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        rlist = list(roman_string)
        rdi = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        alist = []
        res = 0
        for nb in rlist:
            for lt in rdi:
                if lt == nb:
                    alist.append(rdi[lt])
        for nb in range(0, len(alist)):
            if find_bigger_number(alist, alist[nb], nb) is True:
                res -= alist[nb]
            else:
                res += alist[nb]
        return res
    return 0

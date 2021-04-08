#!/usr/bin/python3
"""Finds a peak"""


def peak(arr, low, high, n):
    """Recursive function to find peak"""
    mid = low + (high - low) / 2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return peak(arr, low, (mid - 1), n)

    else:
        return peak(arr, (mid + 1), high, n)


def find_peak(list_of_integers):
    """Wraper over recursive"""
    if list_of_integers == []:
        return None
    n = len(list_of_integers) + 1
    return peak(list_of_integers, 0, n - 1, n)

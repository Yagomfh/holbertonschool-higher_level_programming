#!/usr/bin/python3
"""Module that divides all elements of a matrix.

Raises:
    TypeError: if elems are not int or float,
    if rows are not same size,
    if div is not int or float.
    ZeroDivisionError: if div == 0
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.

    Args:
        matrix (list): matrix of int or float digits
        div (int/float): the dividers digit

    Returns:
        A new matrix.
    """
    if matrix is None or matrix == [[]]:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    for x in matrix:
        if all(isinstance(y, (int, float)) for y in x) is False:
            raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    len_last = len(matrix[0])
    for rows in range(1, len(matrix)):
        if len_last != len(matrix[rows]):
            raise TypeError('Each row of the matrix \
must have the same size')
        len_last == len(matrix[rows])

    if isinstance(div, (int, float)) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    result = [[round(y / div, 2) for y in x] for x in matrix]
    return result

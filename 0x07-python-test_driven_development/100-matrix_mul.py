#!/usr/bin/python3
"""Module that multiplies 2 matrices.

Raises:
    TypeError: m_a m_b not a list or list of list or empty or not a rectangle 
    ValueError: if m_a or m_b can't be multiplied
"""


def check_rect(matrix):
    """Function that check if the matrix is a rectangle

    Args:
        matrix: the matrix to check

    Returns:
        True if it's a rectangle or False otherwise
    """
    len_last = len(matrix[0])
    for rows in range(1, len(matrix)):
        if len_last != len(matrix[rows]):
            return False
        len_last == len(matrix[rows])
    return True

def check_int_float(matrix):
    """Function that check is matrix has elements that are not int or float

    Args:
        matrix: the matrix to check
    
    Returns:
        True if elems are int or float or False otherwise
    """
    for x in matrix:
        if all(isinstance(y, (int, float)) for y in x) is False:
            return False
    return True

def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices.

    Args:
        m_a (list): matrix 1
        m_b (list): matrix 2
    """
    if isinstance(m_a, list) is False:
        raise TypeError('m_a must be a list')
    if isinstance(m_b, list) is False:
        raise TypeError('m_b must be a list')
    if any(isinstance(l, list) for l in m_a) is False:
        raise TypeError('m_a must be a list of lists')
    if any(isinstance(l, list) for l in m_b) is False:
        raise TypeError('m_b must be a list of lists')
    if m_a == [[]]:
        raise TypeError("m_a can't be empty")
    if m_b == [[]]:
        raise TypeError("m_b can't be empty")
    if check_int_float(m_a) is False:
        raise TypeError('m_a should contain only integers or floats')
    if check_int_float(m_b) is False:
        raise TypeError('m_b should contain only integers or floats')
    if check_rect(m_a) is False:
        raise TypeError('each row of m_a must be of the same size')
    if check_rect(m_b) is False:
        raise TypeError('each row of m_b must be of the same size')
    try:
        res = []
        for i in range(0,len(m_a)):
            temp=[]
            for j in range(0,len(m_b[0])):
                s = 0
                for k in range(0,len(m_a[0])):
                    s += m_a[i][k]*m_b[k][j]
                temp.append(s)
            res.append(temp)
    except Exception:
        raise ValueError("m_a and m_b can't be multiplied")
    return res

#!/usr/bin/python3
"""Module that multiplies 2 matrices by using the module NumPy"""


import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices by using the module NumPy
    
    Args:
        m_a: matrix nb1
        m_b: matrix nb2

    Returns:
        The multiplication of both matrices
    """
    return np.dot(m_a, m_b)

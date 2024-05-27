#!/usr/bin/python3
"""
Module: matrix_operations

This module provides operations for matrix manipulation.

Functions:
    - matrix_divided(matrix, div):  Divides each element of matrix
    by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides each element of matrix by a divisor.

    Parameters:
    - matrix (list of lists):   The matrix to be divide.
    - div:  The divisor

    Returns:
    list of lists:  A new matrix where each element is the result of
    dividing the corresponding element of the input matrix by the divisor,
    rounded to two decimal places.

    Raises:
    - TypeError: If matrix is not a matrix (list of lists)
    of integers/floats, if each row of the matrix does not
    have the same size, or if div is not a number.
    - ZerDivisionError: If div is zero.
    """
    # Check if matrix is a valid matrix (list of lists)
    # containing only integers or floats
    for row in matrix:
        if type(row) not in [list]:
            raise TypeError("matrix must be a matrix(list of lists)\
                            of integers/floats")
        else:
            for element in row:
                if type(element) not in [float, int]:
                    raise TypeError("matrix must be a matrix(list\
                                    of lists) of integers/floats")
    # Check if each row of the matrix has the same size
    size = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the
                            same size")
    # Check if div is a number (either a float or an integer)
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    # Check if div is zero
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide each element of the matrix by the divisor,
    # rounding the result to two decimal places
    new_matrix = list(map(lambda row[round(x / div, 2) for x in row], matrix))
    return new_matrix

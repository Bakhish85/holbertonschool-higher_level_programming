#!/usr/bin/python3
"""
Module: matrix_operations

This module provides functions for performing
operations on matrices.

Functions:
    - square_matrix_map(matrix):    Square each element of matrix
                                    using map and lambda function.
"""
def square_matrix_map(matrix=[]):
    """
    Sqaure each element of a matrix using map and lambda functions.

    Parameters:
        matrix (list of lists): A 2D matrix represented as a
                                list of lists.

    Returns:
        list of lists:  A new matrix where each element is square of the 
                        corresponding element in the original matrix.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> square_matrix_map(matrix)
        [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
    """
    new_matrix = list(map(lambda row: (list(map(lambda x: x * x, row)), matrix)
    return new_matrix

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Function computes the square value of all integers of a matrix.
    Args:
        matrix (list): The initial matrix
    Returns:
        list:   Returns a new matrix.
                - Same size as the initial matrix.
                - Each value of a new matrix sholud be
                the square of the value of the input.
    """
    square_matrix = []
    for list in matrix:
        square_list = []
        for number in list:
            square_number = number ** 2
            square_list.append(square_number)
        square_matrix.append(square_list)
    return square_matrix

#!/usr/bin/python3
"""
Module: square_printer

This module provides a function for printing a square pattern.

Functions:
    - print_square(size):   Prints a square pattern of '#' characters
    with the specified size.
"""


def print_square(size):
    """
    Prints a square pattern of '#' characters with the specified size.

    Parameters:
    - size(int):    The size of the square (number of rows and columns).

    Raises:
    - TypeError: If size is not an integer.
    - ValueError: If size is less than 0.
    """
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    elif size > 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print('#' * size)

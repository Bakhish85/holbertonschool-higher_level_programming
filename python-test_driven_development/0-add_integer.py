#!/usr/bin/python3
"""
Module: arithmetic_operations

This module provides arithmetic operations for integers.

Functions:
    - add_integer(a, b=98): Adds two integers together.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.

    Parameters:
    - a(int or float):    The first integer to be added.
    - b(int or float):    The second integer to be added.
                            Default is 98.

    Returns:
    int:    The sum of two integers.

    Raises:
    - TypeError:    If `a` or `b` is not an integer.
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#!/usr/bin/python3
"""
Module: square

This module defines a simple Square class
for representing and manipulating square objects.
"""


class Square:
    """
    A class representing a square.
    This class provides a simple way to create
    and manipulate square objects.Each square
    is defined by its size.

    Attributes:
        __size (float or int):  The size of each side of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (float or int): The size of each side of the square.
        """
        self.__size = size

#!/usr/bin/python3
"""
Module: square

This module defines a simple Square class for representing
and manipulating square objects.
"""


# Class definition
class Square:
    """
    A class representing a square.

    This class provides a simple way to create
    and manipulate square objects. Each square is
    defined by its size.

    Attributes:
        __size (int):   The size of each side of the square.

    Methods:
        __init__(size=0):   Initializes a new Sqaure instance
                            with the given size.
        area():             Calculates the area of the square.
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    
    def area(self):
        return self.__size ** 2

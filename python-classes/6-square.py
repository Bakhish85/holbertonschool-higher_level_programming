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

    This class provides a simple way to create and manipulate
    square objects. Each sqaure is defined by its size.

    Attributes:
        __size (int):   The size of each side of the square.
        __position (tuple): The position of the square in the
                            format (x, y).

    Methods:
        __init__(size=0, position=(0, 0):   Initializes a new Square
                                            instance with the given
                                            size and position
        area():             Calculates the area of the square
        my_print():         Prints a visual representation of the
                            e using '#' characters.
        size:               Property to get or set the size of the square.
        position:           Property to get the position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if (type(position) is not tuple or len(position) != 2 or
            type(position[0]) is not int or type(position[1]) is not int or
            position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                if self.__position[1] > 0:
                    print("_" * self.__position[0], end="")
                else:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

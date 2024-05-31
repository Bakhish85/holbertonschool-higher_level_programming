#!/usr/bin/python3
"""
Module: shapes.py

This module defines classes representing geometric shapes.

Classes:
        Rectangle: A class representing a rectangle shape.
        Square: A class representing a square shape, inheriting
                from Rectangle.
"""


Rectangle = __import__('9-rectangle.py').Rectangle
Square = __import__('10-square.py').Square


class Sqaure(Rectangle):
    """
    Square class represents a square shape and inherits
    from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __str__():  Returns a string representation of the Square
                object.
    """
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

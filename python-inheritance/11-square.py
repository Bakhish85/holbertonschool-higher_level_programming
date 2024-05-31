#!/usr/bin/python3
Rectangle = __import__('9-rectangle.py').Rectangle
Square = __import__('10-square.py').Square
"""
Square class represents a square shape and inherits
from Rectangle.

Attributes:
    __size (int): The size of the square.

Methods:
    __str__():  Returns a string representation of the Square
                object.
"""


class Square(Rectangle):
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

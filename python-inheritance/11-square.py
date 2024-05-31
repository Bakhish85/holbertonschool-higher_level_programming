#!/usr/bin/python3
Rectangle = __import__('9-rectangle.py').Rectangle
Square = __import__('10-square.py').Square


class Square(Rectangle):
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

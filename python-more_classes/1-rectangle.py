#!/usr/bin/python3
"""
Module: rectangle

This module defines a Rectangle class for representing
rectangles with specified width and height.

Classes:
    - Rectangle: A class representing rectangle
    with width and height attributes.
"""


class Rectangle:
    """
    A class representing rectangles with width and height attributes.

    Attributes:
        width(int): The width of the rectangle
        height(int): The height of the rectangle.

    Methods:
        __init__(self, width=0, height=0):  Initializes a
        Rectangle object with the given width and height.
        width(self):    Getter method for retrieving the width of rectangle
        height(self):   Getter method for retrieving the height of rectangle
        width(self, value): Setter method for setting the width of rectengle
        height(self, value): Setter method for setting the height of rectangle
    """


    def __init__(self, width=0, height=0):
        if type(height) not in [float, int]:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")        
        self.__height = height
        if type(width) not in [float, int]:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [float, int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [float, int]:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

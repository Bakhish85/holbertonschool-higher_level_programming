#!/usr/bin/python3
"""
Module: base_geometry.py

This module defines the Basegeometry class, which serves
as a base class for geometry related operations.

Classes:
    BaseGeometry: A base class for geometry operations.
    Rectangle: A class representing a rectangle, inheriting
    from BaseGeometry.
"""


class BaseGeometry:
    """
    This class provides a foundation for geometry related
    operations.

    Methods:
        area(): This method is a placeholder and should be
            implemented by subclass to calculate the area.
        integer_validator(name, value):    This method
            validates whether the provided value is an
            integer and greater than 0.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle shape and inherits
    from BaseGeometry.

    Attributes:
        __width (int):  The width of the rectangle
        __height (int): The height of the rectangle

    Methods:
        __init__(width, height):    Initializes a Rectangle
                        object with the given width and height.
        area(self):     Returns the area of the rectangle.
        __str__(self):  Returns a string representation of the
                        Rectangle object.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

#!/usr/bin/python3
"""
Module: base_geometry.py

This module defines the Basegeometry class, which serves
as a base class for geometry related operations.

Classes:
    BaseGeometry: A base class for geometry operations.
"""


class BaseGeometry:
    """
    This class provides a foundation for geometry related
    operations.

    Methods:
        area(): This method is a placeholder and should be
        implemented by subclass to calculate the area.
        integer_validation(name, value):    This method
        validates whether the provided value is an integer
        and greater than 0.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

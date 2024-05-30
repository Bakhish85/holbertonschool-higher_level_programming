#!/usr/bin/python3
"""
6-base_geometry module

This module contains the definition of the BaseGeometry
class. It provides a template for derived classes to
implement specific geometric properties and behaviors.
"""


class BaseGeometry:
    """
    This class is an abstract base class for geometric
    shapes. It provides a framework for derived classes
    to implement geometric operations.

    Methods:
        - area(self):   This method is intended to calculate
        the area of geometric shape. However it is not implemented
        instead it raises an exception to indicate that derived
        classes must override this method with their own implementation.
    """
    def area(self):
        raise Exception("area() is not implemented")

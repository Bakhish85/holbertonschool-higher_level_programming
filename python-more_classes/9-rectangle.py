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
        number_of_instances (int):  Total number of instances of
            Rectangle class.
        print_symbol (any):  A class attribute representing
            the symbol used for printing the rectangle.

    Methods:
        __init__(self, width=0, height=0):  Initializes a
        Rectangle object with the given width and height.
        width(self):    Getter method for retrieving the width of rectangle
        height(self):   Getter method for retrieving the height of rectangle
        width(self, value): Setter method for setting the width of rectengle
        height(self, value): Setter method for setting the height of rectangle
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self):  Returns a string representation of the
                        rectangle with '#' characters.
        __repr__(self): Returns a string representation of the rectangle
                        to be able to recreate a new instance by using eval()
        __del__(self):  Prints the message Bye rectangle...
                        when an instance of Rectangle is deleted
        bigger_or_equal(rect_1, rect_2):    Static method that compares
                        the areas of rectangles and returns the rectangle
                        with bigger area.
        square(cls, size=0):    Creates a square Rectangle instance with
                        equal width and height.
    """
    number_of_instances = 0
    print_symbol = '#'

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
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

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

    def area(self):
        area = self.__width * self.__height
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter

    def __str__(self):
        hash_rec = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                hash_rec += str(self.print_symbol)
            if h < self.__height - 1:
                hash_rec += "\n"
        return hash_rec

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

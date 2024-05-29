#!/usr/bin/python3
"""
1-my_list module

This module defines a custom list class called MyList.

Classes:
    MyList: A custom list class inheriting
    from the built-in list class.
"""


class MyList(list):
    """
    A custom list class inheriting from the
    built-in list class.

    Methods:
        print_sorted(self): Prints the elements
        of the list in the sorted order.
    """
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)

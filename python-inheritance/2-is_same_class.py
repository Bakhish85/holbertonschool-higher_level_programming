#!/usr/bin/python3
"""
same_class module

This module is for checking if an object belongs
to a specific class.

"""


def is_same_class(obj, a_class):
    """
    Check if the given object belongs to the specified class.

    Parameters:
        obj (object):   The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool:   True if the objects belongs to the specified
                class, False otherwise
    """
    return type(obj) == a_class

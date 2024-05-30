#!/usr/bin/python3
"""
3-same_class module

This module is for checking if the object is an
instance of a class or a class that inherited from
specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of a
    class or a class that inherited from specified class.

    Parameters:
        obj (object):   The object to be checked.
        a_class (type): The class to compare against.

    Returns:
        bool:   True if the object is an instance of,
        or if the object is an instance of a class that
        inherited from, the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)

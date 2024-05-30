#!/usr/bin/python3
"""
4-inherits_from module

This module is for checking if the object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    This function checks if the object is an instance
    of a class that inherited from the specified class.

    Parameters:
        obj(object):    The object to be checked
        a_class(class): The class to compare against

    Returns:
        bool:   returns True if the object is an instance
        of a class that inherited (directly or indirectly)
        from the specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

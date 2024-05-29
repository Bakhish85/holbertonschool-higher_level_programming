#!/usr/bin/python3
"""
Lookup Module

This module provides a function for looking up
attributes and methods of an object.

Functions:
    lookup(obj):    Returns a list of attribute
    and method names of the given object.
"""


def lookup(obj):
    """
    Returns a list of attribute and method names
    of the given object:

    Parameters:
        obj (object):   The object to look up.

    Returns:
        list: A list of strings containing the names
        of attribute and method names of given object.
    """
    return dir(obj)

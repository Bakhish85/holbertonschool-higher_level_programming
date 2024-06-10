#!/usr/bin/python3
"""
This module provides a function to convert objects
into a JSON-serializable structure.
"""


def class_to_json(obj):
    """
    Converts an object into a JSON-serializable structure.

    Parameters:
        obj(any):    The object to be converted.

    Returns:
        JSON-serializable representation of the object
    """
    if hasattr(obj, '__dict__'):
        attributes = obj.__dict__
        return {key: class_to_json(value) for key, value in attributes.items()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return obj
    elif isinstance(obj, bool):
        return obj
    else:
        return None

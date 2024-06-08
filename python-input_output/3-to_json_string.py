#!/usr/bin/python3
"""
This module provides a single function to_json_string for
converting Python objects to JSON formatted strings.
"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON formatted string.

    Parameters:
        my_obj (any): The Python object to be converted to JSON.

    Returns:
        str: A JSON formatted string representing the input Python object.
    """
    js_string = json.dumps(my_obj)
    return js_string

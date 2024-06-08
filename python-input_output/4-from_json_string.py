#!/usr/bin/python3
"""
This module provides a single function from_json_string
for converting JSON formatted strings to Python objects.
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON formatted string to a Python object.

    Parameters:
        my_str (str):   The JSON formatted string to be
                        converted to a Python object.

    Returns:
        any:    A Python object representing
                the input JSON formatted string.
    """
    my_obj = json.loads(my_str)
    return my_obj

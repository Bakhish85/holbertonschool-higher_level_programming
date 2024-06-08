#!/usr/bin/python3
"""
This module provides a single function save_to_json_file
for saving Python objects to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    Parameters:
        my_obj (any):   The Python object to be saved
                        to the JSON file.
        filename (str): The name of the JSON file to which
                        the object will be saved.

    Returns:    None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json_str = json.dumps(my_obj)
        file.write(json_str)

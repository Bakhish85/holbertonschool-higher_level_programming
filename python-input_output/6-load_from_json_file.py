#!/usr/bin/python3
"""
This module provides a single function load_from_json_file
for loading Python objects from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.


    Parameters:
        filename (str): The name of the JSON file from
                        which the object will be loaded.

    Returns:
        any:    A Python object representing the data
                loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        json_str = file.read()
        obj = json.loads(json_str)
        return obj

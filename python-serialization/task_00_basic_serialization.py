#!/usr/bin/env python3
"""
JSON Serialization Module

This module provides functions for serializing Python data structures into JSON format
and saving them to files, as well as loading JSON data from files and deserializing
them into Python data structures.

Functions:
    - serialize_and_save_to_file(data, filename): Serialize and save data to a JSON file.
    - load_and_deserialize(filename): Load and deserialize data from a JSON file.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to a JSON file.

    Parameters:
    - data: Python data structure to be serialized and saved.
    - filename: Name of the file where the data will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as jsonfile:
        jsonfile.write(json.dumps(data))
    pass


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Parameters:
    - filename: Name of the file from which JSON data will be loaded.

    Returns:
    - Deserialized Python data structure.
    """
    with open(filename, "r", encoding="utf-8") as jsonfile:
        return json.load(jsonfile)
    pass

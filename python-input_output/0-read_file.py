#!/usr/bin/python3
"""This module provides a function to read the contents of a file."""
def read_file(filename=""):
    """
    Read the contents of the specified file and print them to the console.

    Args:
        filename (str): The path to the file to be read.
                        If not provided, an empty string is assumed.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

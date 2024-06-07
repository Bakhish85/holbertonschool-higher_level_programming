#!/usr/bin/python3
"""
This module provides functions for reading from and writing to files.
"""


def append_write(filename="", text=""):
    """
    Append the specified text to the given file
    and return the number of characters added.

    Args:
        filename (str): The path to the file to append the text to.
                        If not provided, an empty string is assumed.
        text (str):     The text to be appended to the file.

    Returns:
        int:            The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)

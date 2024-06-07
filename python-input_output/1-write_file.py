#!/usr/bin/python3
"""This module provides functions for reading from and writing to files."""


def write_file(filename="", text=""):
    """
    Write the specified text to the given file and
    return the number of characters written.

    Args:
        filename (str): The path to the file to write the text to.
                        If not provided an empty string is assumed.
        text (str):     The text to be written to the file.

    Returns:
        int:            The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as w:
        w.write(text)
        return len(text)

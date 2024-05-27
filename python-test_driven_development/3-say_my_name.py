#!/usr/bin/python3
"""
Module: name_utils

This module provides utilities for handling names.

Functions:
    - say_my_name(first_name, last_name=""):    Prints the full name using
    the provided first name and last name.
"""


def say_my_name(first_name, last_name):
    """
    Prints the full name using the provided
    first name and last name.

    Parameters:
    - first_name (str): The first name.
    - last_name (str, optional):    The last name.
    Defaults to an empty string.

    Raises:
    - TypeError:    If first_name or last_name is
    not a string.
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    elif type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Function prints a dictionary by ordered keys.
    Args:
        a_dictionary (dict):    The input dictionary.
    Returns:
        (dict):     Returns keys sorted by alphabetic order
        and relevant values each in the new line.
        - Only sort keys of the first level.
        - Dictionary values can have any type.
    """
    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print(f"{key}: {a_dictionary.get(key)}")

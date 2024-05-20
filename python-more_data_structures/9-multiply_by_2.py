#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    The function returns a new dictionary with all values multiplied by 2.
    Args:
        a_dictionary (dict):    The input dictionary.
    Returns:
        dict:   A new dictionary with values multiplied with 2.
        - The old dictionary will remain same.
    """
    new_dictionary = {}
    for key in a_dictionary.keys():
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary

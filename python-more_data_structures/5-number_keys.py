#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Function returns the number of keys in a dictionary.
    Args:
        a_dictionary (dict):    The input dictionary
    Returns:
        int:    The number of key in the input dictionary.
    """
    keys_list = a_dictionary.keys()
    return len(keys_list)

#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    The function replaces or adds key/value in a dictionary.
    Args:
        a_dictionary (dict):    The input dictionary
        key (str):      The key to be added or updated.
        value (Any):    The value to be added or updated.
    Returns:
        dict:   Returns updated dictionary.
            - If a key exists in the dictionary,
            the value will be replaced.
            - If a key does not exist in the dictionary
            it will be created
    """
    a_dictionary[key] = value
    return a_dictionary

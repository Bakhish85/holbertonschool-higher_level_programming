#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    The function deletes a key in a dictionary.
    Args:
        a_dictionary (dict):    The input dictionary
        key (str):      The key to be deleted.
    Returns:
        (dict): Returns updated dictionary
        with deleted key and its value.
        - If a key does not exist,
        the dictionary will not change.
    """
    key_del = a_dictionary.get(key)
    if key_del is not None:
        del a_dictionary[key]
    return a_dictionary

#!/usr/bin/python3
def best_score(a_dictionary):
    """
    The function returns a key with the biggest integer value.
    Args:
        a_dictionary (dict):    The input dictionary
    Returns:
        (str):  Returns a key with the biggest integer values
                - If no dictionary found, return None
    """
    if a_dictionary is not None:
        best_key = max(a_dictionary.keys())
        return best_key
    else:
        return None

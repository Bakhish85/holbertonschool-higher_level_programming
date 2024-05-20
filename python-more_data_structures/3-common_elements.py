#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Function returns a set of common elements in two sets.
    Args:
        set_1 (set):    The first input set
        set_2 (set):    The second input set
    Returns:
        set:   The set of common elements of set_1 and set_2..
    """
    common_set = set_1 & set_2
    return common_set

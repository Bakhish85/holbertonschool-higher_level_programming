#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Function returns a set of all elements present in only one set.
    It is called symmetric difference.
    Args:
        set_1 (set):    The first input set
        set_2 (set):    THe second input set
    Returns:
        set:            The set of all different elements.
    """
    dif_set = set_1 ^ set_2
    return dif_set

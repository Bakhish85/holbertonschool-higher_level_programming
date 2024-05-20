#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Function adds all unique integers in a list (only once for each integer).
    Args:
        my_list (list): The input list
    Returns:
        int:            The sume of all unique integers in my_list.
    """
    my_set = set(my_list)
    result = 0
    for number in my_set:
        result += number
    return result

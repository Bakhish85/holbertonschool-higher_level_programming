#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Function returns the biggest integer of a list.
    Args:
        my_list (list): The input list
    Returns:
        int: Max number among the elements of my_list.
        If the input list is empty, the function will return None.
        Note: We are not allowed to use builtin max().
    """
    if len(my_list) == 0:
        return None
    max_number = my_list[0]
    for number in my_list:
        if number >= max_number:
            max_number = number
    return max_number

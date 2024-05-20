#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Function deletes the item at a specific position in a list.
    Args:
        my_list (list): The input list
        idx (int):      The specific position in the list to be deleted
    Returns:
        list:           The list with deleted item.
                        If idx is negative or out of range,
                        nothing change (returns the same list).
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list.remove(my_list[idx])
    return my_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function replaces all occurrences of an element
    by another in a new list.
    Args:
        search (int): The element to replace in the list
        replace (int):  The new element
    Returns:
        list:   The new list with replaced elements
    """
    new_list = []
    for number in my_list:
        if number == search:
            number = replace
        new_list.append(number)
    return new_list

#!/usr/bin/python3
"""
Module: weightes_average

This module provides functions for calculating weightes averages.

Functions:
    - weight_average(my_list):  Calculate the weightes average
                                of a list of tuples.
"""


def weight_average(my_list=[]):
    """
    Calculate the weightes average of alist of tuples.

    Parameters:
        my_list (list): A list of tuples where each tuple
                        contains two elements:
                        - The first element represents the value
                        - The second element represents the weight of value

    Returns:
        float:          The weightes average of the values in the lisr.
    """
    total_sum = 0
    weight_sum = 0
    for tuple_ in my_list:
        total_sum += tuple_[0] + tuple_[1]
        weight_sum += tuple_[1]
    result = total_sum / weight_sum
    return result

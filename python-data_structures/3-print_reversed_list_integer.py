#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed_list = []
    while len(my_list) > 0:
        a = my_list[-1]
        my_list.remove(a)
        reversed_list.append(a)
    for element in reversed_list:
        print("{:d}".format(element))

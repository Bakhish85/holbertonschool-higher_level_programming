#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for i, number in enumerate(list):
            if i == len(list) - 1:
                print("{:d}".format(number))
            else:
                print("{:d} ".format(number), end="")

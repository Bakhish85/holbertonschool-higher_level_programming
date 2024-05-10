#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print("")
    else:
        for i, element in enumerate(matrix):
            for j, element in enumerate(matrix):
                if j < len(matrix) - 1:
                    print("{:d} ".format(matrix[i][j]), end="")
                else:
                    print("{}".format(matrix[i][j]), end="")
            print("")

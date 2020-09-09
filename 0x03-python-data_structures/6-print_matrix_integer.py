#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        j = 0
        for k in i:
            if j != len(i) - 1:
                print("{:d}".format(k), end=" ")
                j = j + 1
            else:
                print("{:d}".format(k), end="")
        print()

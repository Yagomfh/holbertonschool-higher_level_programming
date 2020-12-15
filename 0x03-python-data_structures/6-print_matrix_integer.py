#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for row in matrix:
        for j in range(0, len(row)):
            if j == len(row) - 1:
                print("{:d}".format(row[j]))
            else:
                print("{:d}".format(row[j]), end=" ")

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print("{:d}".format(matrix[i][j]), end=" " if j != 2 else "\n")

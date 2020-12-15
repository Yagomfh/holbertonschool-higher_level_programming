#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j == len(matrix) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=" ")

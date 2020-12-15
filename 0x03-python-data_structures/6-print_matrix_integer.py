#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])
    if row == 1 and col == 0:
        print("")
    for i in range(0, row):
        for j in range(0, col):
            print("{:d}".format(matrix[i][j]), end=" " if j != 2 else "\n")

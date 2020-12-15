def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])
    if row == 1 and col == 0:
        print("")
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=" " if i != 2 else "\n")

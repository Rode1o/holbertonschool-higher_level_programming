#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for files in matrix:
        token = 0
        for column in files:
            token += 1
            print('{:d}'.format(column), end='')
            if token != len(files):
                print(" ", end='')
        print('')

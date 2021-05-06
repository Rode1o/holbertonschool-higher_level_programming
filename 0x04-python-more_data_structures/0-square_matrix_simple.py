#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    _matrix = matrix[:]
    for token in range(len(matrix)):
        for i in range(len(matrix[token])):
            _matrix[token] = list(map(lambda x: x ** 2, matrix[token]))
    return _matrix

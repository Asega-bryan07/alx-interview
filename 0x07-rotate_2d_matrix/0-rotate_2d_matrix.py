#!/usr/bin/env/python3
'''
Test 0x07 - Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''

def transpose_matrix(matrix, n):
    '''
    _summary_
        Args:
                matrix (_type_): description
    '''
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    '''
    _summary_
    Args:
    matrix (_type_): description
    '''
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    '''
    _summary_
        Args:
            matrix (_type_): description
    '''
    n = len(matrix)
    
    '''
    #simple matrix
    1 2 3
    4 5 6
    7 8 9

    # transpose matrix
    1 4 7
    2 5 8
    3 6 9

    # reverse matrix
    7 4 1
    8 5 2
    9 6 3
    '''
    transpose_matrix(matrix, n)

    reverse_matrix(matrix)

    return matrix

#!/usr/bin/python3
'''
Test 0x07 - Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    '''
    _summary_
    Args:
    matrix (list[[list]]): a matrix
    '''
    n = len(matrix)
    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n -1 - j)
            # current number
            tmp = matrix[i][j]
            #change top for left
            matrix[i][j] = matrix[x][i]
            #change left for bottom
            matrix[x][i] = matrix[y][x]
            #change bottom for right
            matrix[y][x] = matrix[j][y]
            #chamge right for top
            matrix[j][y] = tmp

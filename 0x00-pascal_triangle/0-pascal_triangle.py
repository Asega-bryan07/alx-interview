#!/usr/bin/python3

'''A script that creates pascal triangle for any number
a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    Assume n will be always an integer
'''

def pascal_triangle(n):
    '''
    returns a list of lists
    of integers representing the Pascal’s triangle of n
    '''
    triangle = []

    '''
    Returns an empty list if n <= 0
    '''
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        triangle.append(temp_list)

    return triangle


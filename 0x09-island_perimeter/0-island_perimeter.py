#!/usr/bin/python3
'''
Create a function def island_perimeter(grid): that returns
the perimeter of the island described in grid:
grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
'''


def check_val(x):
    '''
    _summary_
    args:
        n (_type_): _description_
    returns
        _type_: _description_
    '''
    if (x == 0):
        return 1
    return 0


def island_perimeter(grid):
    '''
    returns
    the perimeter of the island described in grid
    '''
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 and 100"

    x = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1), \
                    "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i-1][j])
                if j-1 < 0:
                    x += 1
                else:
                    x += check_val(grid[i][j-1])

                try:
                    x += check_val(grid[i+1][j])
                except IndexError:
                    x += 1
                try:
                    x += check_val(grid[i][j+1])
                except IndexError:
                    x += 1
    return x

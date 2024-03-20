#!/usr/bin/python3
'''
In a text file, there is a single character H. Your
text editor can execute only two operations in this
file: Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:
    n = 9
    H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
    Paste => HHHHHH => Paste => HHHHHHHHH
    Number of operations: 6
'''


def minOperations(n):
    '''
    execute only two operations in this
    file: Copy All and Paste.
    '''
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        '''
        if n evenly divides by the root
        '''
        if n % root == 0:
            ops += root
            '''
            sets n to the remainder
            '''
            n = n / root
            '''
            reduce root to find the remaining values; smaller
            that divide n evenly
            '''
            root -= 1
            '''
            increment root until it is divisible by n evenly
            '''
            root += 1
    return ops

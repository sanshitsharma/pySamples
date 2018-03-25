#!/usr/bin/python

"""
Given a 2D matrix, print all elements of the given matrix in diagonal order. For example, consider the following 5 X 4 input matrix.

    1     2     3     4
    5     6     7     8
    9    10    11    12
   13    14    15    16
   17    18    19    20
Diagonal printing of the above matrix is

    1
    5     2
    9     6     3
   13    10     7     4
   17    14    11     8
   18    15    12
   19    16
   20
"""

def in_bound(cols, i, j):
    return i >= 0 and j < cols

def diagonal_print(mat):
    r = len(mat)
    c = len(mat[0])

    # First print col 0
    for i in range(r):
        string = ''
        j = 0
        while in_bound(c, i, j):
            string = string + str(mat[i][j]) + ' '
            i = i - 1
            j = j + 1
        print string

    # Now print the lower half starting at index (r-1, 1) to (r-1, c-1)
    for j in range(1, c):
        string = ''
        i = r-1
        while in_bound(c, i, j):
            string = string + str(mat[i][j]) + ' '
            i = i - 1
            j = j + 1
        print string

if __name__ == "__main__":
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    diagonal_print(mat)
#!/usr/bin/python

import numpy as np 

def getDiagStartPoints(x, y, n, dtype='principle'):
    d_start = [x, y]
    if dtype == 'principle':
        while d_start[0] > 0 and d_start[1] > 0:
            d_start[0] -= 1
            d_start[1] -= 1
    else:
        while d_start[0] < n-1 and d_start[1] > 0:
            d_start[0] += 1
            d_start[1] -= 1

    return d_start

def isValid(mat, a, b):
    r = len(mat)
    c = len(mat[0])

    # Check row
    for j in range(c):
        if mat[a][j] == 1 and j != b:
            return False

    # Check Col
    for i in range(r):
        if mat[i][b] == 1 and i != a:
            return False

    # Check diagonals
    # Given a coordinate (a,b), find out the top-left and the bottom-left 
    # starting points of the two diagonals on which this point lies
    pd_start = getDiagStartPoints(a, b, r, dtype='principle')
    sd_start = getDiagStartPoints(a, b, r, dtype='secondary')

    #print "Principle Diagonal Start point for (", a, ",", b, "): ", pd_start
    #print "Secondary Diagonal Start point for (", a, ",", b, "): ", sd_start

    # Check principle diagonal
    i = pd_start[0]
    j = pd_start[1]
    while i < r and j < c:
        if mat[i][j] == 1 and i != a and j != b:
            return False
        i += 1
        j += 1

    # Check secondary diagonal
    i = sd_start[0]
    j = sd_start[1]
    while i < r and j < c:
        if mat[i][j] == 1 and i != a and j != b:
            return False
        i -= 1
        j += 1

    return True

def solve(mat, queensLeft, r):
    if queensLeft == 0:
        return True

    for c in range(len(mat)):
        mat[r][c] = 1
        if isValid(mat, r, c) and solve(mat, queensLeft - 1, r + 1):
            return True
        # If not, then backtrack
        mat[r][c] = 0

    return False

def placeQueens(n):
    mat = np.zeros([n, n], dtype=int)
    solve(mat, n, 0)

    print mat

if __name__ == "__main__":
    n = 8
    placeQueens(n)
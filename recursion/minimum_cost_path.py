#!/usr/bin/python

import numpy as np 
import sys

MAXINT = sys.maxint

'''
Recursive solution:

The solution starts at 
'''

def _mcp(mat, i, j, sol):
    if sol[i][j] != 0:
        #print "Hit the cache.."
        return sol[i][j]
    
    #print "Solving.. i =", i, "j =", j 
    if i == 0 and j == 0:
        sol[0][0] = mat[0][0]
        return sol[0][0]

    if i < 0 or j < 0:
        return MAXINT
    
    sol[i][j] = mat[i][j] + min(_mcp(mat, i-1, j-1, sol), _mcp(mat, i-1, j, sol), _mcp(mat, i, j-1, sol))
    return sol[i][j]

def mcp(mat, indx):
    r = len(mat)
    c = len(mat[0])

    sol = np.zeros(shape=(r,c), dtype=int)
    _mcp(mat, indx[0], indx[1], sol)

    print sol
    return sol[indx[0]][indx[1]]

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
    index = (2, 2)
    mcp(mat, index)
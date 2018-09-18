#!/usr/bin/python

'''
Ref: https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
'''

import sys

def solve(p, i, j):
    if i == j:
        return 0

    _min = sys.maxsize

    for k in range(i, j):
        count = solve(p, i, k) + solve(p, k+1, j) + (p[i-1]*p[k]*p[j])

        if count < _min:
            _min = count

    return _min

def matrixChainMultiplication(p):
    low = 1
    high = len(p) - 1

    return solve(p, low, high)

if __name__ == "__main__":
    p = [1, 2, 3, 4, 3]
    print matrixChainMultiplication(p)
#!/usr/bin/python

"""
Given an n x n matrix, where every row and column is sorted in non-decreasing order. Print all elements of matrix in sorted order.

Example:

Input: mat[][]  =  { {10, 20, 30, 40},
                     {15, 25, 35, 45},
                     {27, 29, 37, 48},
                     {32, 33, 39, 50},
                   };

Output:
Elements of matrix in sorted order
10 15 20 25 27 29 30 32 33 35 37 39 40 45 48 50
"""

INF = float("inf")

def youngify(mat, i, j):
    N = len(mat)

    #Calculate down value and right value
    down_value = mat[i+1][j] if i+1 < N else INF
    right_value = mat[i][j+1] if j+1 < N else INF

    if down_value == INF and right_value == INF:
        return

    if down_value < right_value:
        mat[i][j] = down_value
        mat[i+1][j] = INF
        youngify(mat, i+1, j)
    else:
        mat[i][j] = right_value
        mat[i][j+1] = INF
        youngify(mat, i, j+1)

def extract_min(mat):
    ret = mat[0][0]
    mat[0][0] = INF
    youngify(mat, 0, 0)
    return ret

if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    n = len(mat)
    string = ''
    for i in range(n*n):
        string = string + str(extract_min(mat)) + ' '
        print mat

    print string
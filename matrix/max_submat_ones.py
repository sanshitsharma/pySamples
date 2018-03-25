#!/usr/bin/python

"""
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.

0 1 1 0 1
1 1 0 1 0
0 1 1 1 0
1 1 1 1 0
1 1 1 1 1
0 0 0 0 0

The output should be a 3x3 matrix from index 
(2,1) - (5,3)
"""
"""
Solution:
Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which
each entry S[i][j] represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost
and bottommost entry in sub-matrix.

1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)    Copy first row and first columns as it is from M[][] to S[][]
     b)    For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]
"""

import numpy as np 

def find_max_square_sub_matrix(mat):
    # Create an matrix S of same size as mat
    S = np.zeros(len(mat)*len(mat[0]), dtype=int).reshape(len(mat), len(mat[0]))
    
    # Copy the first row and first col as is
    i = 0
    for j in range(len(mat[0])):
        S[i][j] = mat[i][j]

    j = 0
    for i in range(len(mat)):
        S[i][j] = mat[i][j]

    # For each remaining element, if element is 0, do nothing, if element is 1
    # calculate S[i][j] = 1 + min(mat[i-1][j], mat[i][j-1])
    for i in range(1, len(S)):
        for j in range(1, len(S[0])):
            if mat[i][j] == 1:
                S[i][j] = 1 + min(S[i-1][j], S[i][j-1], S[i-1][j-1])

    max = -1
    indx = (-1, -1)
    # Find the max value & it's index in S
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] > max:
                max = S[i][j]
                indx = (i, j)

    sub_mat = np.ones(max*max, dtype=int).reshape(max, max)
    return sub_mat

if __name__ == "__main__":
    mat = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
    sub_mat = find_max_square_sub_matrix(mat)

    for i in range(len(sub_mat)):
        string = ''
        for j in range(len(sub_mat[0])):
            string = string + str(sub_mat[i][j]) + ' '
        print string
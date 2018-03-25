#!/usr/bin/python

'''
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then
make all the cells of ith row and jth column as 1.

Example 1
The matrix
1 0
0 0
should be changed to following
1 1
1 0

Example 2
The matrix
0 0 0
0 0 1
should be changed to following
0 0 1
1 1 1

Example 3
The matrix
1 0 0 1
0 0 1 0
0 0 0 0
should be changed to following
1 1 1 1
1 1 1 1
1 0 1 1

reference: https://www.geeksforgeeks.org/a-boolean-matrix-question/
'''

def insert_to_list(lst, elem):
    try:
        lst.index(elem)
    except ValueError as e:
        lst.append(elem)

def is_in_lst(lst, elem):
    try:
        lst.index(elem)
    except ValueError as e:
        return False

    return True

def transform(mat):
    rows = []
    cols = []

    # First figure out which rows and cols have to be set to 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                insert_to_list(rows, i)
                insert_to_list(cols, j)

    # Traverse the matrix again, for each mat[i][j], if i exists in rows 
    # & j exists in cols, mark mat[i][j] = 1
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if is_in_lst(rows, i) or is_in_lst(cols, j):
                mat[i][j] = 1

if __name__ == "__main__":
    mat = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]
    transform(mat)

    print mat
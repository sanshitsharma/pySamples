#!/usr/bin/python3

'''
Question 1:
Given an n x n matrix and a number x, find position of x in the matrix if it is present in it. Else print "Not Found".
In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity.

Example:
Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 29
Output: Found at (2, 1)

Input: mat[4][4] = { {10, 20, 30, 40},
                      {15, 25, 35, 45},
                      {27, 29, 37, 48},
                      {32, 33, 39, 50}};
              x = 100
Output: Element not found
'''

def is_in_bounds(n, i, j):
    return i >= 0 and i < n and j >= 0 and j < n

def find(mat, x):
    n = len(mat)

    # Start at top right
    indx = (0, n-1)

    # Compare element(e) at indx to x
    while True:
        if not is_in_bounds(n, indx[0], indx[1]):
            break

        if mat[indx[0]][indx[1]] == x:
            return indx

        # If e > x, move indx to left
        if mat[indx[0]][indx[1]] > x:
            indx = (indx[0], indx[1]-1)
            continue

        # if e < x, move indx down
        if mat[indx[0]][indx[1]] < x:
            indx = (indx[0]+1, indx[1])
            continue

    return None

if __name__ == "__main__":
    mat = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
    tests = [29, 100]

    for test in tests:
        res = find(mat, test)
        if res:
            print(res)
        else:
            print("Element not found")
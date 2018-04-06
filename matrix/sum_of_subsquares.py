#!/usr/bin/python

"""
Given an n x n square matrix, find sum of all sub-squares of size k x k where k is smaller than or equal to n.

Examples

Input:
n = 5, k = 3
arr[][] = { {1, 1, 1, 1, 1},
            {2, 2, 2, 2, 2},
            {3, 3, 3, 3, 3},
            {4, 4, 4, 4, 4},
            {5, 5, 5, 5, 5},
         };
Output:
       18  18  18
       27  27  27
       36  36  36


Input:
n = 3, k = 2
arr[][] = { {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
         };
Output:
       12  16
       24  28
"""

"""
Brute Force: Simple approach is to start from topleft corner and keep discovering subsquares of size k
and keep printing their sums. 

Time Complexity: O(k^2n^2)
"""

def get_sum(si, mat):
    sum = 0
    for i in range(si[0], si[2]+1):
        for j in range(si[1], si[3]+1):
            sum += mat[i][j]

    return sum

def printSubSquaresSum(mat, k):
    n = len(mat)
    if k < 1 or k > n:
        return

    for i in range(n - k + 1):
        string = ''
        for j in range(n - k + 1):
            subsquare_indexes = (i, j, i + k - 1, j + k - 1)
            string += str(get_sum(subsquare_indexes, mat)) + ' '
        print string

"""
Optimized solution: Preprocess the matrix. In the preprocessing step, create a temp matrix
stripSum which stores the sum of all strips of size k X 1. 

Once we have all the vertical strip sums, we can calculate the sum of first subsquare by adding
the first k values of first row and then every subsequent subsquare can be calculated by removing
the left value and adding the right value

Time Complexity: O(n^2)
"""

def print_subsquares_sum(mat, k):
    n = len(mat)

    if k < 1 or k > n:
        return

    # Pre-process
    stripSum = [[0 for x in range(n)] for y in range(n - k + 1)]

    for j in range(n):
        string = ''
        sum = 0
        for i in range(k):
            sum += mat[i][j]
        stripSum[0][j] = sum

        for i in range(1, n-k+1):
            sum += (mat[i+k-1][j] - mat[i-1][j])
            stripSum[i][j] = sum

    # Now we combine on the columns, k at a time
    subsquares_sum = [[0 for x in range(n - k + 1)] for y in range(n - k + 1)]
    
    for i in range(len(stripSum)):
        sum = 0
        for j in range(k):
            sum += stripSum[i][j]
        subsquares_sum[i][0] = sum

        for j in range(1, n-k+1):
            sum += stripSum[i][j+k-1] - stripSum[i][j-1]
            subsquares_sum[i][j] = sum

    for i in range(len(subsquares_sum)):
        string = ''
        for j in range(len(subsquares_sum)):
            string += str(subsquares_sum[i][j]) + ' '
        print string

if __name__ == "__main__":
    #mat = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]
    mat = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    k = 3
    #printSubSquaresSum(mat, k)
    print_subsquares_sum(mat, k)

    print 
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 2
    #printSubSquaresSum(mat, k)
    print_subsquares_sum(mat, k)
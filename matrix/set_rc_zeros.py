#!/usr/bin/python

'''
Given a matrix, if an element a[i][j] is 0, set all other elements in row i and col j to 0
'''

class Solution(object):
    def setZeroesInPlace(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time Complexity: O(m^2n^2)
        # Space Compexity: O(1)

        r, c = len(matrix), len(matrix[0])

        # First parse the matrix to find a number that does not occur in the array
        num = -1
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == num:
                    num -= 1

        # Loop through each row and which ever row has a 0, set all non-zero elements to num
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    for k in range(c):
                        if matrix[i][k] != 0:
                            matrix[i][k] = num
                    
                    for k in range(r):
                        if matrix[k][j] != 0:
                            matrix[k][j] = num
        
        
        # Loop through the matrix once more and change all the num to 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == num:
                    matrix[i][j] = 0

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Time Complexity: O(mn)
        # Space Complexity: O(m+n)

        r, c = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        # First pass to figure out which row & cols need to be set to zero
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for j in range(c):
                matrix[row][j] = 0
    
        for col in cols:
            for i in range(r):
                matrix[i][col] = 0

if __name__ == "__main__":
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    #m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(m)
    print m

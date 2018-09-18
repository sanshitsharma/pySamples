#!/usr/bin/python

import numpy as np 
from datetime import datetime

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # First swap the rows
        for i in range(rows/2):
            j = rows - i - 1
            for k in range(cols):
                matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
        
        # Now swap mirros, all elements south of principle diagonal
        for i in range(1, rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == "__main__":
    mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    #mat = [[ 5, 1, 9, 11], [ 2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print "Original:"
    print mat

    obj = Solution()
    start_time = datetime.now()
    obj.rotate(mat)
    duration = datetime.now() - start_time
    print "Duration:", duration.microseconds, "microseconds"
    
    print "\nRotated:"
    print mat

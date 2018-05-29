#!/usr/bin/python

'''
Problem #240
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Example 1:
Input: matrix, target = 5
Output: true

Example 2:
Input: matrix, target = 20
Output: false

Ref: https://leetcode.com/problems/search-a-2d-matrix-ii/description/ 
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        r = 0
        c = len(matrix[0]) - 1

        while c >= 0 and r < len(matrix):
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1

        return False

if __name__ == "__main__":
    mat = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    trgt = 21
    print Solution().searchMatrix(mat, trgt)
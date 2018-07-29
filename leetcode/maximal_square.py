#!/usr/bin/python

'''
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

Ref: https://leetcode.com/problems/maximal-square/description/
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        nr = len(matrix)
        nc = len(matrix[0])

        max_side_length = 0
        ans = [[int(matrix[r][c]) for c in range(nc)] for r in range(nr)]
        
        print ans
        for r in range(nr):
            for c in range(nc):
                ans[r][c] = self.getSideLengthAtIndex(ans, r, c)
                if ans[r][c] > max_side_length:
                    max_side_length = ans[r][c]


        print ans
        return max_side_length**2

    def getSideLengthAtIndex(self, mat, r, c):
        # Check values at (r-1 ,c), (r-1, c-1) and (r, c-1) and return the min
        if r == 0 or c == 0 or mat[r][c] == 0:
            return int(mat[r][c])

        return int(mat[r][c]) + min(int(mat[r-1][c]), int(mat[r-1][c-1]), int(mat[r][c-1]))

if __name__ == "__main__":
    #A = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 1, 1]]
    #A = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    A = [["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]
    print Solution().maximalSquare(A)
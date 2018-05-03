#!/usr/bin/env python

'''
Problem #62: Unique Paths

A robot is located at the top-left corner of a m x n grid

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid
How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

Ref: https://leetcode.com/problems/unique-paths/description/
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype:
        """

        # Create a matrix mat of size mxn. 
        # Initialize all cells to 1
        mat = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i-1][j] + mat[i][j-1]

        return mat[m-1][n-1]

        '''
        # Constant Space/Constant Time solution
        return int(math.factorial(m+n-2)/(math.factorial(m-1)*math.factorial(n-1)))
        '''


if __name__ == "__main__":
    m = 98
    n = 98

    res = Solution().uniquePaths(m, n)
    print "Num unique paths:", res

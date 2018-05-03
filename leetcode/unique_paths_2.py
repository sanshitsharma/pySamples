#!/usr/bin/python

'''
Problem #63: Unique Paths II
A robot is located at the top-left corner of a m x n grid

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Ref: https://leetcode.com/problems/unique-paths-ii/description/ 
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Create a sol matrix, initialize sol[0][0] with 1
        # Also sol[i][j] = 0 if a[i][j] = 1
        sol = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    sol[i][j] = 1
                    continue

                # If cell(i, j) is blocked in matrix 'a', set sol[i][j] to 0 and continue
                if obstacleGrid[i][j] == 1:
                    sol[i][j] = 0
                    continue

                if i == 0:
                    sol[i][j] = sol[i][j-1]
                elif j == 0:
                    sol[i][j] = sol[i-1][j]
                else:
                    sol[i][j] = sol[i-1][j] + sol[i][j-1]

        return sol[m-1][n-1]

if __name__ == "__main__":
    a = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
    res = Solution().uniquePathsWithObstacles(a)
    print res
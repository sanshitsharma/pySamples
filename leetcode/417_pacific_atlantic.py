#!/usr/bin/python

'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches
the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.

Example:
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

Ref: https://leetcode.com/problems/pacific-atlantic-water-flow/description/
'''

import numpy as np

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = []
        for i in range(m):
            for j in range(n):
                visited = np.zeros((m, n), dtype=bool)
                #print "Evaluating i =", i, "j =", j
                if self.canFlowToPacific(matrix, visited, i, j) and self.canFlowToAtlantic(matrix, visited, i, j):
                    ans.append([i, j])
        return ans
        
    def canFlowToPacific(self, mat, visited, i, j):
        if i <= 0 or j <= 0:
            return True
        
        r = len(mat)
        c = len(mat[0])

        visited[i][j] = True
        if mat[i][j] >= mat[i-1][j] and not visited[i-1][j]:
            return self.canFlowToPacific(mat, visited, i-1, j)
        if mat[i][j] >= mat[i][j-1] and not visited[i][j-1]:
            return self.canFlowToPacific(mat, visited, i, j-1)
        if i < r-1 and mat[i][j] >= mat[i+1][j] and not visited[i+1][j]:
            return self.canFlowToPacific(mat, visited, i+1, j)
        if j < c-1 and mat[i][j] >= mat[i][j+1] and not visited[i][j+1]:
            return self.canFlowToPacific(mat, visited, i, j+1)
        
        visited[i][j] = False
        return False
        
    def canFlowToAtlantic(self, mat, visited, i, j):
        r = len(mat)
        c = len(mat[0])

        if i >= r-1 or j >= c-1:
            return True
        
        visited[i][j] = True
        if mat[i][j] >= mat[i+1][j]:
            return self.canFlowToAtlantic(mat, visited, i+1, j)
        if mat[i][j] >= mat[i][j+1]:
            return self.canFlowToAtlantic(mat, visited, i, j+1)
        if i > 0 and mat[i][j] > mat[i-1][j]:
            return self.canFlowToAtlantic(mat, visited, i-1, j)
        if j >0 and mat[i][j] > mat[i][j-1]:
            return self.canFlowToAtlantic(mat, visited, i, j-1)
            
        visited[i][j] = False
        return False

if __name__ == "__main__":
    #mat = np.array([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
    #mat = np.array([[1,2,3],[8,9,4],[7,6,5]])
    mat = np.array([[10,10,10],[10,1,10],[10,10,10]])
    #print mat
    print Solution().pacificAtlantic(mat)
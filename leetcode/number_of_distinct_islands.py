#!/usr/bin/python

import numpy as np

class Solution(object):
    def dfs(self, r, c, grid, iC):
        nr = len(grid)
        nc = len(grid[0])

        if r < 0 or r >=nr or c < 0 or c >=nc or grid[r][c] == 0:
            return
        
        grid[r][c] = 0
        iC.append((r, c))
        self.dfs(r-1, c, grid, iC)
        self.dfs(r+1, c, grid, iC)
        self.dfs(r, c-1, grid, iC)
        self.dfs(r, c+1, grid, iC)

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numIslands = 0
        nr = len(grid)
        nc = len(grid[0])

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    islandCoords = []
                    self.dfs(r, c, grid, islandCoords)
                    print "Island Coordinates:", islandCoords
                    numIslands += 1

        return numIslands

if __name__ == "__main__":
    grid = np.array([[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]])
    #grid = np.array([[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]])
    #grid = np.array([[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 0, 1, 0]])
    print grid
    print Solution().numDistinctIslands2(grid)
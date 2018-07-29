#!/usr/bin/python

class Island(object):
    def __init__(self, grid):
        self.isl = grid
        self.length = len(grid)
        self.height = len(grid[0])

    def isInbounds(self, r, c):
        if r < 0 or r >= self.length or c < 0 or c >= self.height:
            return False
        return True

    def isWater(self, r, c):
        return self.isl[r][c] == '0'

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0

        island = Island(grid)

        count = 0
        for i in range(island.length):
            for j in range(island.height):
                if island.isl[i][j] == '0':
                    continue
                
                count += 1
                self.dfs(i, j, island)

        return count

    def dfs(self, r, c, island):
        if not island.isInbounds(r, c) or island.isWater(r, c):
            return

        island.isl[r][c] = '0'
        self.dfs(r-1, c, island)
        self.dfs(r+1, c, island)
        self.dfs(r, c-1, island)
        self.dfs(r, c+1, island)

if __name__ == "__main__":
    #grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid = [['1', '1', '0', '1', '1'], ['1', '1', '1', '1', '1'], ['0', '0', '0', '0', '0'], ['1', '0', '1', '0', '1'], ['0', '1', '0', '1', '0']]
    #grid = [['1', '0', '1'], ['0', '1', '0'], ['1', '0', '1']]
    ans = Solution().numIslands(grid)
    print ans
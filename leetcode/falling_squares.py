#!/usr/bin/python

class Solution(object):
    """
    :type positions: List[List[int]]
    :rtype: List[int]
    """
    def tripletIntersection(self, a, b):
        if a[0] > b[1] or a[1] < b[0]:
            return None
    
        return [min(a[0], b[0]), max(a[1], b[1]), a[2]+b[2]]

    def getTriplet(self, pos):
        return [pos[0], pos[0]+pos[1], pos[1]]

    def fallingSquares(self, positions):
        ranges = [self.getTriplet(positions[0])]
        maxHeight = ranges[0][2]
        res = [maxHeight]

        for i in range(1, len(positions)):
            #print self.getTriplet(positions[i])
            t = self.getTriplet(positions[i])

        print res
if __name__ == "__main__":
    #a = [1, 3, 2]
    #b = [2, 5, 3]

    Solution().fallingSquares([[1,2], [2,3], [6,1]])
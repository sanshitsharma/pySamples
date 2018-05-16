#!/usr/bin/python

class Solution(object):
    def solve(self, n):
        if n == 0:
            return [0, 1, 0]

        prev = self.solve(n-1)
        curr = [0]
        for i in range(len(prev)-1):
            curr.append(prev[i] + prev[i+1])
        
        curr.append(0)
        return curr
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = self.solve(rowIndex)
        row.pop()
        row.pop(0)
        return row


if __name__ == "__main__":
    n = 33
    print Solution().getRow(n)
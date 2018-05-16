#!/usr/bin/python

import math

class Solution(object):
    def makeSum(self, num, n):
        #print "num =", num, "n =", n
        if num == n:
            return [n]

        res = [num]
        r = num + 1
        l = num - 1
        while True:
            num += r
            res.append(r)
            if num > n:
                num -= r
                res.pop()
            elif num == n:
                break
            else:
                r += 1
            
            num += l
            res = [l] + res
            l -= 1
            if num >= n:
                break
            elif l < 0:
                return None
        
        if num == n:
            return res

        return None

    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        targetFactor = int(round(math.sqrt(N)+1))
        if N%2 == 0:
            targetFactor += 1
        #print "TF:", targetFactor
        numList = []
        for i in range(1, targetFactor):
            #print "i =", i
            nums = self.makeSum(N/i, N)
            if nums is not None and nums not in numList:
                print "Added for factor:", i
                numList = [nums] + numList

        return numList

    #BRUTE Force
    def consSum(self, n):
        res = []
        for num in range(1, n+1):
            nums = [num]
            i = 0
            j = num + 1
            while sum(nums) + j <= n:
                nums.append(j)
                i += 1
                j += 1
            
            if sum(nums) == n:
                res.append(nums)

        return res

if __name__ == "__main__":
    n = 735
    print Solution().consecutiveNumbersSum(n)
    #print Solution().consSum(n)
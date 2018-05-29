#!/usr/bin/python

'''
Problem #89
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

Ref: https://leetcode.com/problems/gray-code/description/ 
'''
from datetime import datetime

class Solution(object):
    def binToDec(self, bList):
        num = 0
        size = len(bList)
        for i in range(size-1, -1, -1):
            exp = size-i-1
            num += int(bList[i])*pow(2, exp)
        return num

    '''
    # Recursive Solution
    def grayCodeUtil(self, n):
        if n == 1:
            return ['0', '1'], ['1', '0']
        
        l1, l2 = self.grayCodeUtil(n-1)
        l1 = ['0'+x for x in l1]
        l2 = ['1'+x for x in l2]
        l3 = l1+l2
        l3.reverse()

        return (l1+l2), l3
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]

        l1, l2 = self.grayCodeUtil(n)
        res = []
        for bStr in l1:
            res.append(self.binToDec(bStr))

        return res
    '''

    # Iterative Solution
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return [0]

        l = ['0', '1']

        for i in range(2, n+1):
            for j in range(len(l)-1, -1, -1):
                l.append(l[j])

            halfSize = len(l)/2
            for j in range(halfSize):
                l[j] = '0'+l[j]
            
            for j in range(halfSize, len(l)):
                l[j] = '1'+l[j]

        res = []
        for bStr in l:
            res.append(self.binToDec(bStr))
        return res

if __name__ == "__main__":
    n = 3
    obj = Solution()
    start_time = datetime.now()
    res = obj.grayCode(n)
    print "Time to complete:", (datetime.now() - start_time).microseconds, "microsecs"
    print res

#!/usr/bin/env python

'''
Given a sorted array and a number x, find the pair in array whose sum is closest to x

Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

Ref: https://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/
'''

import sys

class Solution(object):
    def findClosestPair(self, A, trgt):
        l = 0
        r = len(A) - 1

        smallestDiff = sys.maxint
        pair = ()
        
        while l < r:
            currSum = A[l] + A[r]
            diff = trgt - currSum
            if abs(diff) < smallestDiff:
                smallestDiff = abs(diff)
                pair = (A[l], A[r])

            if diff == 0:
                return pair
            elif currSum < trgt:
                l += 1
            else:
                r -= 1

        return pair

if __name__ == "__main__":
    #print Solution().findClosestPair([10, 22, 28, 29, 30, 40], 54)
    print Solution().findClosestPair([1, 3, 4, 7, 10], 15)
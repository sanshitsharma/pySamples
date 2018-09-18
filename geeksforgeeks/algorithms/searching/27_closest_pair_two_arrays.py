#!/usr/bin/python

'''
Find the closest pair from two sorted arrays
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array.

We are given two arrays ar1[0..m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute
value of (ar1[i] + ar2[j] - x) is minimum.

Example:

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40

Ref: https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/ 
'''

import sys

class Solution(object):
    def findClosestPair(self, A, B, x):
        if not A or not B:
            return None

        l = 0
        r = len(B)-1
        pair = None
        smallestDiff = sys.maxint

        while l < len(A) and r >= 0:
            currSum = A[l] + B[r]
            diff = x - currSum

            if abs(diff) < smallestDiff:
                smallestDiff = abs(diff)
                pair = (A[l], B[r])

            if diff == 0:
                return pair

            if currSum < x:
                l += 1
            else:
                r -= 1

        return pair

if __name__ == "__main__":
    #print Solution().findClosestPair([1, 4, 5, 7], [10, 20, 30, 40], 32)
    print Solution().findClosestPair([1, 4, 5, 7], [10, 20, 30, 40], 50)
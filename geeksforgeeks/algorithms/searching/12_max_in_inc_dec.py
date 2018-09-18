#!/usr/bin/env python

'''
Find the maximum element in an array which is first increasing and then decreasing
Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.
Examples :

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120

Ref: https://www.geeksforgeeks.org/find-the-maximum-element-in-an-array-which-is-first-increasing-and-then-decreasing/
'''

class Solution(object):
    '''
    Solution: Basically the arr is rotated. We can perform a binary search for an element
    until we find an element whose left and right are both smaller
    '''
    def findMax(self, arr):
        return self._findMaxUtil(arr, 0, len(arr)-1)

    def _findMaxUtil(self, A, lo, hi):
        print "lo:", lo, "hi:", hi 
        if hi < lo:
            return None

        mid = (lo+hi)/2
        print "mid:", mid
        if (mid > 0 and mid < len(A)-1 and A[mid-1] < A[mid] and A[mid+1] < A[mid]) or (mid == 0 and A[mid+1] < A[mid]) or (mid == len(A)-1 and A[mid-1] < A[mid]):
            return A[mid]
        elif A[mid-1] > A[mid]:
            return self._findMaxUtil(A, lo, mid-1)
        else:
            return self._findMaxUtil(A, mid+1, hi)

if __name__ == "__main__":
    print Solution().findMax([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1])
    print Solution().findMax([1, 3, 50, 10, 9, 7, 6])
    print Solution().findMax([10, 20, 30, 40, 50])
    print Solution().findMax([120, 100, 80, 20, 0])
    #print Solution().findMax([20, 100])
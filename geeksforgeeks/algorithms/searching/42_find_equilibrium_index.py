#!/usr/bin/env python

'''
Find the element before which all the elements are smaller than it, and after which all are greater
Given an array, find an element before which all elements are smaller than it, and after which all are greater than it. Return index of the element if there is such an element, otherwise return -1.

Examples:

Input:   arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
Output:  Index of element is 4
All elements on left of arr[4] are smaller than it
and all elements on right are greater.
 
Input:   arr[] = {5, 1, 4, 4};
Output:  Index of element is -1
Expected time complexity is O(n).

Ref: https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
'''

import sys

class Solution(object):
    def findEquilibriumIndex(self, A):
        if not A:
            return -1

        leftMax = [-sys.maxint]
        rightMin = [sys.maxint]

        currLeftMax = -sys.maxint
        for i in range(1, len(A)):
            currLeftMax = max(currLeftMax, A[i-1])
            leftMax.append(currLeftMax)

        currRightMin = sys.maxint
        for i in range(len(A)-2, -1, -1):
            currRightMin = min(currRightMin, A[i+1])
            rightMin = [currRightMin] + rightMin

        '''
        print "Array:", A
        print "Left Max:", leftMax
        print "Right Min:", rightMin
        '''

        # Now we need to find the index 'i' such that leftMax[i] < A[i] < rightMin[i]
        for i in range(len(A)):
            if leftMax[i] < A[i] and A[i] < rightMin[i]:
                return i

        return -1

if __name__ == "__main__":
    A = [5, 1, 4, 7, 6, 8, 10, 12, 9]
    print "Equilibrium Index for", A, "=", Solution().findEquilibriumIndex(A)
    A = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    print "Equilibrium Index for", A, "=", Solution().findEquilibriumIndex(A)
    A = [5, 1, 4, 4]
    print "Equilibrium Index for", A, "=", Solution().findEquilibriumIndex(A)
    A = [5]
    print "Equilibrium Index for", A, "=", Solution().findEquilibriumIndex(A)
    A = []
    print "Equilibrium Index for", A, "=", Solution().findEquilibriumIndex(A)
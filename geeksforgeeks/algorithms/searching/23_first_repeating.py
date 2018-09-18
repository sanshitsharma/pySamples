#!/usr/bin/env python

'''
Find the first repeating element in an array of integers
Given an array of integers, find the first repeating element in it. We need to find the element that occurs more than once and whose index of first occurrence is smallest.

Examples:

Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 [5 is the first element that repeats]

Input:  arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
Output: 6 [6 is the first element that repeats]

Ref: https://www.geeksforgeeks.org/find-first-repeating-element-array-integers/
'''

import sys

class Solution(object):
    def firstRepeating(self, A):
        if len(A) < 2:
            return None

        firstOccurence = {}
        minIndex = sys.maxint

        for indx, elem in enumerate(A):
            try:
                if firstOccurence[elem] < minIndex:
                    minIndex = firstOccurence[elem]
            except KeyError as ke:
                firstOccurence[elem] = indx

        return A[minIndex] if minIndex < len(A) else None

if __name__ == "__main__":
    print Solution().firstRepeating([10, 5, 3, 4, 3, 5, 6])
    print Solution().firstRepeating([6, 7, 9, 8, 6, 7, 9, 8])
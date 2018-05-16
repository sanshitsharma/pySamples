#!/usr/bin/python

'''
Problem #658: Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

Ref: https://leetcode.com/problems/find-k-closest-elements/description/
'''

''' 
The solution presented below uses binary search and has time complexity = O(log(n))
'''

import pyCollections

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        if x < arr[0]:
            return arr[0:k]
        elif x > arr[len(arr)-1]:
            return arr[len(arr)-k:len(a)]
        else:
            res = []
            # Search for x or the element that's closest to the x
            indx = pyCollections.binarySearch(arr, x)
            print "Index:", indx
            if indx < 0:
                # binarySearch function returned the index at which x can be inserted in array
                indx = -indx - 1
                
            l = indx - 1
            r = indx
            count = 0

            while l >= 0 and r < len(arr) and count < k:
                if x - arr[l] < arr[r] - x:
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
                count += 1

            # No more elements on right
            while count < k and l >= 0:
                res.append(arr[l])
                l -= 1
                count += 1

            while count < k and r < len(arr):
                res.append(arr[r])
                r += 1
                count += 1

        return res

if __name__ == "__main__":
    #a = [1, 2, 4, 5, 6, 8, 11]
    #k = 4
    #x = 8

    a = [1,1,2,3,3,3,4,6,8,8]
    k = 6
    x = 1

    print "Input:", a
    res = Solution().findClosestElements(a, k, x)
    print res
#!/usr/bin/python

'''
Problem #215
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 <= k <= array's length.

Ref: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Since we need to find the kth largest element, we will substract k from len(nums) to 
        # translate it into the kth smallest element.
        # kth largest element = (len(nums) - k)th smallest element
        newK = len(nums) - k

        return self.quickSelect(nums, newK, 0, len(nums)-1)

    def quickSelect(self, nums, k, l, r):
        if l > r:
            return
        
        pivotIndx = self.partition(nums, l, r, k)
        if k == pivotIndx:
            return nums[k]
        elif k < pivotIndx:
            return self.quickSelect(nums, k, l, pivotIndx-1, k)
        else:
            return self.quickSelect(nums, k, pivotIndx+1, r, k)

    def partition(self, a, l, r, k):
        pivotIndx = k

        while l < r:
            while l <= r and a[l] <= a[pivotIndx]:
                l += 1

            while r >= l and a[r] >= a[pivotIndx]:
                r -= 1

            if l < r:
                a[l], a[r] = a[r], a[l]

        
        # Finally put the pivotIndex element in it's designated spot
        a[pivotIndx], a[r] = a[r], a[pivotIndx]
        return r

if __name__ == "__main__":
    a = [3,2,3,1,2,4,5,5,6]
    k = 4

    res = str(k) + "th largest element = " + str(Solution().findKthLargest(a, k))
    print res
#!/usr/bin/python

'''
Problem #239
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Ref: https://leetcode.com/problems/sliding-window-maximum/description/
'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        if k > len(nums):
            return []

        """ Create a Double Ended Queue, Qi that 
        will store indexes of array elements. 
        The queue will store indexes of useful 
        elements in every window and it will
        maintain decreasing order of values from
        front to rear in Qi, i.e., arr[Qi.front[]]
        to arr[Qi.rear()] are sorted in decreasing
        order"""
        q = []
        res = []

        # Process the first k elements and store the indexes
        for i in range(k):
            # For every element, any existing element which
            # are smaller than nums[i] are useless, so 
            # discard them
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

        # Process the remaining elements
        for i in range(k, len(nums)):
            # The element at index 0 of q is the biggest element of 
            # existing window. store that to the result
            res.append(nums[q[0]])

            # Move the window
            while q and q[0] <= i-k:
                q.pop(0)

            # Now remove all elements that are smaller than nums[i]
            while q and nums[i] >= nums[q[-1]]:
                q.pop()

            q.append(i)

        res.append(nums[q[0]])
        return res

if __name__ == "__main__":
    arr = [12, 1, 78, 90, 57, 89, 56]
    #arr = [5, 4, 3, 2, 1]
    k = 3
    #printMax(arr, len(arr), k)
    print Solution().maxSlidingWindow(arr, k)
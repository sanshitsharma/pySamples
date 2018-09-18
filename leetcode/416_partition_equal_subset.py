#!/usr/bin/python

'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of
elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

Ref: https://leetcode.com/problems/partition-equal-subset-sum/description/
'''

###########################################
#                RECURSIVE                #
###########################################
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        s = sum(nums)
        if s%2 != 0:
            return False

        return self.isSubsetSum(nums, len(nums)-1, s/2)

    def isSubsetSum(self, arr, n, s):
        if sum(arr[:n+1]) == s:
            return True

        if n < 0 or sum(arr[:n+1]) < s or s < 0:
            return False

        return self.isSubsetSum(arr, n-1, s) or self.isSubsetSum(arr, n-1, s-arr[n])

if __name__ == "__main__":
    a = [1, 3, 1, 3]
    print Solution().canPartition(a)
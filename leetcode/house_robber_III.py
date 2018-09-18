#!/usr/bin/env python

'''
Problem 337: House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root,
each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It
will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

Ref: https://leetcode.com/problems/house-robber-iii/description/
'''

"""
Solution:
Perform a level order traversal of the tree starting at the root and store the total sum of 
even levels and odd levels. In the end, return the max of the two
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        evenQ = [root]
        oddQ = []

        lvlSums = []

        while evenQ or oddQ:
            lvlSums.append(self._processQueue(evenQ, oddQ))
            lvlSums.append(self._processQueue(oddQ, evenQ))

        return self._maximizeLoot(lvlSums)

    def _processQueue(self, srcQ, dstQ):
        qSum = 0
        while srcQ:
            node = srcQ.pop(0)
            qSum += node.val
            if node.left:
                dstQ.append(node.left)
            if node.right:
                dstQ.append(node.right)

        return qSum

    def _maximizeLoot(self, nums):
        if not nums:
            return 0

        if len(nums) < 3:
            return max(nums)

        for i in range(2, len(nums)):
            if i == 2:
                nums[i] += nums[i-2]
            else:
                nums[i] += max(nums[i-2], nums[i-3])

        return max(nums)
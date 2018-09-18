#!/usr/bin/env python

'''
250. Count Univalue Subtrees

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4

Ref: https://leetcode.com/problems/count-univalue-subtrees/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        self.cUtil(root, count)
        return count[0]

    def cUtil(self, root, count):
        if not root:
            return

        if (not root.left and not root.right) or (root.left and root.right and root.val == root.left.val and root.val == root.right.val) or (not root.right and root.left and root.val == root.left.val) or (not root.left and root.right and root.val == root.right.val):
            count[0] += 1

        self.cUtil(root.left, count)
        self.cUtil(root.right, count)

if __name__ == "__main__":
    '''
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    '''

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print Solution().countUnivalSubtrees(root)
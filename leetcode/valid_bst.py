#!/usr/bin/python

'''
Problem #98: Validate BST

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input:
    2
   / \
  1   3
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

Ref: https://leetcode.com/problems/validate-binary-search-tree/description/
'''

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBSTUtil(self, root, minV, maxV):
        if root is None:
            return True

        if root.val > minV and root.val > maxV:
            return self.isValidBSTUtil(root.left, minV, root.val) and self.isValidBSTUtil(root.right, root.val, maxV)

        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTUtil(root, -sys.maxint-1, sys.maxint)

if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(15)

    print Solution().isValidBST(root)
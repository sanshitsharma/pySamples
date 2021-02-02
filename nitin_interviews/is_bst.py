#!/usr/bin/python3

'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Validate:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValidUtil(root, float("-inf"), float("inf"))
    
    def _isValidUtil(self, root, mii, mxi):
        if not root:
            return True
        
        if root.val <= mii or root.val >= mxi:
            return False
        
        return self._isValidUtil(root.left, mii, root.val) and self._isValidUtil(root.right, root.val, mxi)

if __name__ == "__main__":
    # Test 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print("isValid:", Validate().isValidBST(root))

    # Test 2
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print("isValid:", Validate().isValidBST(root))
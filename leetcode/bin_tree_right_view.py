#!/usr/bin/python

'''
Problem #199
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

Ref: https://leetcode.com/problems/binary-tree-right-side-view/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        evenQ = [root]
        oddQ = []

        res = []

        while evenQ or oddQ:
            if evenQ:
                res.append(evenQ[-1].val)
                while evenQ:
                    elem = evenQ.pop(0)
                    if elem.left:
                        oddQ.append(elem.left)
                    if elem.right:
                        oddQ.append(elem.right)

            if oddQ:
                res.append(oddQ[-1].val)
                while oddQ:
                    elem = oddQ.pop(0)
                    if elem.left:
                        evenQ.append(elem.left)
                    if elem.right:
                        evenQ.append(elem.right)

        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(6)
    root.right.right.left = TreeNode(9)
    root.right.right.right = TreeNode(10)
    root.right.right.right.left = TreeNode(11)

    res = Solution().rightSideView(root)
    print res
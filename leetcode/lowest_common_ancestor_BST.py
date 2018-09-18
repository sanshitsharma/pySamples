#!/usr/bin/python

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p

        if root is None:
            print "found none node"
            return None
        
        print "Evaluating.. root:", root.val, "p:", p.val, "q:", q.val
        if (p.val < root.val and q.val > root.val) or p.val == root.val or q.val == root.val:
            return root.val
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        print "returning None"
        return None

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)

    print Solution().lowestCommonAncestor(root, TreeNode(1), TreeNode(4))
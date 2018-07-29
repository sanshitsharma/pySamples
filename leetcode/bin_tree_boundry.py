#!/usr/bin/python

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isLeaf(self, root):
        return root.left is None and root.right is None

    def getLeftBoundary(self, root, res):
        if not root:
            return
        
        if not self.isLeaf(root):
            res.append(root.val)
        
        if root.left:
            return self.getLeftBoundary(root.left, res)
        
        return self.getLeftBoundary(root.right, res)

    def getLeaves(self, root, res):
        if not root:
            return

        if self.isLeaf(root):
            res.append(root.val)

        self.getLeaves(root.left, res)
        self.getLeaves(root.right, res)

    def getRightBoundary(self, root, res):
        if not root:
            return

        if not self.isLeaf(root):
            res.append(root.val)

        if root.right:
            return self.getRightBoundary(root.right, res)

        return self.getLeftBoundary(root.left, res)

    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ans = []
        if not root.left:
            ans.append(root.val)
        else:
            self.getLeftBoundary(root, ans)
        #print "After left boundary:", ans

        it not self.isLeaf(root):
            self.getLeaves(root, ans)
        print "After leaves:", ans

        rB = []
        if root.right:
            self.getRightBoundary(root.right, rB)
        while rB:
            ans.append(rB.pop())

        #print "After right boundary:", ans
        return ans
        
if __name__ == "__main__":
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)

    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(9)
    root.right.left.right = TreeNode(10)
    '''

    '''
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    '''

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print Solution().boundaryOfBinaryTree(root)
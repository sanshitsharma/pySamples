#!/usr/bin/python

class TreeNode(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution(object):
    def getPathUtil(self, root, path, target):
        if root is None:
            return

        #print "Path:", path, "root:", root.val
        if path[-1] == target:
            return

        # Look left if possible
        if root.left:
            path.append(root.left.val)
            self.getPathUtil(root.left, path, target)
            if path[-1] == target:
                return
            path.pop()

        # Look right if possible
        if root.right:
            path.append(root.right.val)
            self.getPathUtil(root.right, path, target)
            if path[-1] == target:
                return
            path.pop()

    def getPath(self, root, target):
        if root is None:
            return []

        path = [root.val]
        self.getPathUtil(root, path, target)
        if path[-1] != target:
            path.pop()

        return path

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP = self.getPath(root, p)
        pathQ = self.getPath(root, q)

        size = min(len(pathP), len(pathQ))
        i = -1

        while i+1 < size and pathP[i+1] == pathQ[i+1]:
            i += 1

        if i != -1:
            print "i =", i, "pathP:", pathP, "pathQ:", pathQ, "lowest common ancestor:", pathP[i]
            return pathP[i]
        
        print "i =", i, "pathP:", pathP, "pathQ:", pathQ
        return None

if __name__ == "__main__":
    '''
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    '''

    root = TreeNode(1)
    root.right = TreeNode(2)

    p = 1
    q = 2
    print Solution().lowestCommonAncestor(root, p, q)
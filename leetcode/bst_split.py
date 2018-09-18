#!/usr/bin/python

'''
Problem #776: Split BST
Given a Binary Search Tree (BST) with root node root, and a target value V, split the tree into two subtrees where one subtree has nodes that
are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value.  It's not
necessarily the case that the tree contains a node with value V.

Additionally, most of the structure of the original tree should remain.  Formally, for any child C with parent P in the original tree, if they
are both in the same subtree after the split, then node C should still have the parent P.

You should output the root TreeNode of both subtrees after splitting, in any order.

Example 1:
Input: root = [4,2,6,1,3,5,7], V = 2
Output: [[2,1],[4,3,6,null,null,5,7]]
Explanation:
Note that root, output[0], and output[1] are TreeNode objects, not arrays.

The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

          4
        /   \
      2      6
     / \    / \
    1   3  5   7

while the diagrams for the outputs are:

          4
        /   \
      3      6      and    2
            / \           /
           5   7         1

Note:
The size of the BST will not exceed 50.
The BST is always valid and each node's value is different.

Ref: https://leetcode.com/problems/split-bst/description/
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _find(self, root, V, parent):
        if root is None:
            return None, None

        if V == root.val:
            return root, parent
        elif V < root.val:
            return self._find(root.left, V, root)
        else:
            return self._find(root.right, V, root)

    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        node, parent = self._find(root, V, None)

        if node is None:
            return [[], root]

        if parent is None:
            # Target node is root
            return [root, []]
            
        if parent.left == node:
            parent.left = node.right
            node.right = None
        else:
            parent.right = node.right

        return [node, root]

def preorder(root, trav):
    if not root:
        return

    trav.append(root.val)
    preorder(root.left, trav)
    preorder(root.right, trav)

if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    trav = []
    preorder(root, trav)
    print "Original:", trav

    root1, root2 = Solution().splitBST(root, 2)

    trav = []
    preorder(root1, trav)
    print "Root1:", trav

    trav = []
    preorder(root2, trav)
    print "Root2:", trav

    '''
    n, p = Solution()._find(root, 2, None)
    print "N:", n, "val:", n.val
    print "P:", p, "val:", p.val
    '''
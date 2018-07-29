#!/usr/bin/python

'''
Problem #297: Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file
or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized
to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: Just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please
be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Ref: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
Approach 1: 

One way to serialize a binary tree is to use some sort of delimiter to depict the null children
of a node, e.g., the binary tree above can be serialized using preorder traversal and injecting
'#' to depict null child

Deserialization will then be straight forward
'''
'''
class Codec:
    def __serialize(self, root, ans):
        if root is None:
            ans.append('#')
            return

        ans.append(str(root.val))
        self.__serialize(root.left, ans)
        self.__serialize(root.right, ans)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        ans = []
        self.__serialize(root, ans)
        return ' '.join(ans)

    def __deserialize(self, data, indx):
        if indx[0] > len(data)-1 or data[indx[0]] == '#':
            return None
        
        root = TreeNode(data[indx[0]])
        indx[0] += 1
        root.left = self.__deserialize(data, indx)
        indx[0] += 1
        root.right = self.__deserialize(data, indx)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        indx = [0]
        root = self.__deserialize(data.split(), indx)
        return root
'''

'''
Approach 2: 

Using the string delimiter has two issues:

1. The delimiter used might be part of tree's data
2. The space required to store the serialized tree with this approach can be a lot

An alternate approach is to serialize the tree using it's inorder and preorder traversals
The two traversals can be joined using a unique delimiter that is not part of the tree data

Then we can reconstruct the tree using the these two traversals

Caveat: This approach only works for trees with unique node values
'''

class Codec:
    def _inorderTrav(self, root, trav):
        if not root:
            return 

        self._inorderTrav(root.left, trav)
        trav.append(str(root.val))
        self._inorderTrav(root.right, trav)

    def _preorderTrav(self, root, trav):
        if not root:
            return 

        trav.append(str(root.val))
        self._preorderTrav(root.left, trav)
        self._preorderTrav(root.right, trav)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        inOrd = []
        self._inorderTrav(root, inOrd)

        preOrd = []
        self._preorderTrav(root, preOrd)

        return ' '.join(inOrd) + '#' + ' '.join(preOrd)

    def __deserialize(self, inOrd, preOrd, preIndx, s, e):
        if s > e:
            return None

        # The current value in preOrd at preIndx is the root
        root = TreeNode(int(preOrd[preIndx[0]]))

        # Find the index of this value in inOrd
        inIndx = inOrd.index(preOrd[preIndx[0]])

        # Increment the preIndx
        preIndx[0] += 1

        # If there are not more nodes, return the root
        if s == e:
            return root
        
        # Build left
        root.left = self.__deserialize(inOrd, preOrd, preIndx, s, inIndx-1)

        # Build right
        root.right = self.__deserialize(inOrd, preOrd, preIndx, inIndx+1, e)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        inOrd, preOrd = data.split('#')
        inOrd = inOrd.split()
        preOrd = preOrd.split()

        preIndx = [0]
        return self.__deserialize(inOrd, preOrd, preIndx, 0, len(inOrd)-1)

def preorder(root):
    if not root:
        return
    
    print root.val
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    '''

    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)

    data = Codec().serialize(root)
    print data
    rootNew = Codec().deserialize(data)
    print "New Tree:"
    preorder(rootNew)
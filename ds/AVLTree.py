#!/usr/bin/env python

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def getHeight(self, node):
        if node is None:
            return 0

        return node.height

    def getBalance(self, node):
        if not node:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)

    def _insertRecurse(self, root, value):
        # Step 1: Insert the node at it's proper position
        if root is None:
            return Node(value)
        elif value <= root.data:
            root.left = self._insertRecurse(root.left, value)
        else:
            root.right = self._insertRecurse(root.right, value)

        # Step 2: Update the height of node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        
        # Step 3: Get the balance factor
        balanceFactor = self.getBalance(root)

        # Step 4: If balanceFactor is > 1: then we are either in Left Left Case or Left Right Case
        # Figure out which one it is
        if balanceFactor > 1 and value < root.left.data:
                return self.RightRotate(root)
        
        if balanceFactor > 1 and value > root.left.data:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)

        if balanceFactor < -1 and value > root.right.data:
            return self.LeftRotate(root)
        
        if balanceFactor < -1 and value < root.right.data:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)

        return root

    def _getParent(self, node, value):
        if node is None:
            raise ValueError(value, 'does not exist in tree')
        if (node.left is not None and node.left.data == value) or (node.right is not None and node.right.data == value):
            return node
        elif value < node.data:
            # Search for parent in left subtree
            return self._getParent(node.left, value)
        elif value > node.data:
            return self._getParent(node.right, value)

    def GetParent(self, value):
        # Will return the parent of the node if value exists in tree
        # else raise a ValueError exception
        if value == self.root.data:
            return None

        return self._getParent(self.root, value)

    def _getNode(self, node, value):
        if node is None:
            raise ValueError(value, 'does not exist in tree')
        elif node.data == value:
            return node
        elif value < node.data:
            return self._getNode(node.left, value)
        else:
            self._getNode(node.right, value)

    def GetNode(self, value):
        # Will return the node if value exists in tree
        # else raise a ValueError exception
        return self._getNode(self.root, value)

    def RightRotate(self, node):
        if node.left is None:
            raise ValueError('right rotate cannot be performed on a node with empty left subtree')

        temp = node.left
        T3 = temp.right

        # Rotate
        temp.right = node
        node.left = T3

        # Recalculate the heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right)) 

        return temp

    def LeftRotate(self, node):
        if node.right is None:
            raise ValueError('left rotate cannot be performed on a node with empty right subtree')

        temp = node.right
        T3 = temp.left

        # Rotate
        temp.left = node
        node.right = T3

        # Recalculate the heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        temp.height = 1 + max(self.getHeight(temp.left), self.getHeight(temp.right))

        return temp

    def Insert(self, value):        
        self.root = self._insertRecurse(self.root, value)

    def _inorderRecurse(self, node):
        if node is None:
            return
        
        self._inorderRecurse(node.left)
        print "Data:", node.data, "Height:", node.height
        self._inorderRecurse(node.right)

    def Inorder(self):
        self._inorderRecurse(self.root)

    def _preorderRecurse(self, node):
        if node is None:
            return 

        print "Data:", node.data, "Height:", node.height
        self._preorderRecurse(node.left)
        self._preorderRecurse(node.right)

    def Preorder(self):
        self._preorderRecurse(self.root)

if __name__ == "__main__":
    avlTree = AVLTree()

    avlTree.Insert(10)
    avlTree.Insert(20)
    avlTree.Insert(30)
    avlTree.Insert(40)
    avlTree.Insert(50)
    avlTree.Insert(25)
    '''
    avlTree.Insert(13)
    avlTree.Insert(10)
    avlTree.Insert(5)
    avlTree.Insert(15)
    avlTree.Insert(12)
    avlTree.Insert(4)
    avlTree.Insert(3)
    avlTree.Insert(16)
    avlTree.Insert(4)
    avlTree.Insert(8)
    '''
    
    avlTree.Preorder()

    '''
    try:
        val = 10
        parent = avlTree.GetParent(val)
        if parent is None:
            print val, "is the root of the tree"
        else:
            print "Parent of", val, ":", parent.data
    except ValueError as ve:
        print ve

    avlTree.Preorder()
    '''
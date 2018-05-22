#!/usr/bin/python

import sys

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def size(root):
    if root is None:
        return 0

    return size(root.left) + 1 + size(root.right)

def maxT(root):
    if root is None:
        return 0

    return max(maxT(root.left), root.val, maxT(root.right))

def minT(root):
    if root is None:
        return sys.maxsize

    return min(minT(root.left), root.val, minT(root.right))

def _printLeftViewUtil(root, cLvl, pLvl, view):
    if root is None:
        return pLvl
    
    if cLvl > pLvl:
        view.append(str(root.val))
        pLvl += 1

    pLvl = _printLeftViewUtil(root.left, cLvl+1, pLvl, view)
    pLvl = _printLeftViewUtil(root.right, cLvl+1, pLvl, view)

    return pLvl

def printLeftView(root):
    currLevel = 0
    printedLevel = -1
    leftView = []

    _printLeftViewUtil(root, currLevel, printedLevel, leftView)
    return ' '.join(leftView)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.right = Node(7)
    root.right.left = Node(5)
    root.right.right = Node(6)

    '''
    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.right.left = Node(3)
    root.right.right = Node(1)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    '''

    # Find size of tree
    print "Size of Tree:", size(root)

    # Find max element in tree
    print "Max element in Tree:", maxT(root)

    # Find min element in tree
    print "Min element in Tree:", minT(root)

    # Print left view of the tree
    print "Tree Left View:", printLeftView(root)
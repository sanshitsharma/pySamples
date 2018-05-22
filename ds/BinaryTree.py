#!/usr/bin/python

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None 
        self.right = None

def __preorderUtil(root, pOrd):
    if root is None:
        return

    pOrd.append(str(root.data))
    __preorderUtil(root.left, pOrd)
    __preorderUtil(root.right, pOrd)

def preorder(root):
    trav = []
    __preorderUtil(root, trav)
    return trav

def size(root):
    if root is None:
        return 0

    return size(root.left) + 1 + size(root.right)
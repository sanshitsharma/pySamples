#!/usr/bin/python

'''
Construct Ancestor Matrix from a Given Binary Tree
Given a Binary Tree where all values are from 0 to n-1. Construct an ancestor matrix mat[n][n]. Ancestor matrix is defined as below.

mat[i][j] = 1 if i is ancestor of j
mat[i][j] = 0, otherwise

Examples:
Input: Root of below Binary Tree.
          0
        /   \
       1     2
Output: 0 1 1
        0 0 0 
        0 0 0 

Input: Root of below Binary Tree.
           5
        /    \
       1      2
      /  \    /
     0    4  3
Output: 0 0 0 0 0 0 
        1 0 0 0 1 0 
        0 0 0 1 0 0 
        0 0 0 0 0 0 
        0 0 0 0 0 0 
        1 1 1 1 1 0

Ref: https://www.geeksforgeeks.org/construct-ancestor-matrix-from-a-given-binary-tree/ 
'''

from ds.BinaryTree import Node, preorder, size

def aMatrix(root, mat, ancestors):
    if root is None:
        return

    for ancestor in ancestors:
        mat[ancestor][root.data] = 1

    # Add current node as ancestors for it's children
    ancestors.append(root.data)

    # Go left
    aMatrix(root.left, mat, ancestors)

    # Go Right
    aMatrix(root.right, mat, ancestors)

    # Backtrack
    ancestors.pop()

def ancestorMatrix(root):
    s = size(root)

    mat = [[0 for i in range(s)] for j in range(s)]
    c = []
    aMatrix(root, mat, c)
    return mat

if __name__ == "__main__":
    root = Node(5)
    root.left = Node(1)
    root.right = Node(2)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.right.left = Node(3)

    mat = ancestorMatrix(root)
    for i in range(len(mat)):
        s = ''
        for j in range(len(mat)):
            s += str(mat[i][j]) + ' '
        print s
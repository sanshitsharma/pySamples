#!/usr/bin/python

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None 
        self.right = None

def constructUtil(p, s):
    if constructUtil.indx > len(p) - 1:
        return None

    root = Node(p[constructUtil.indx])

    if s[constructUtil.indx] == 'L':
        constructUtil.indx += 1
        return root
    
    constructUtil.indx += 1
    root.left = constructUtil(p, s)
    root.right = constructUtil(p, s)

    return root

def construct(p):
    constructUtil.indx = 0
    return constructUtil(p, s)

def preorder(root, pOrd):
    if root is None:
        return

    pOrd.append(str(root.data))
    preorder(root.left, pOrd)
    preorder(root.right, pOrd)

if __name__ == "__main__":
    #p = [10, 30, 20, 5, 15]
    #s = ['N', 'N', 'L', 'L', 'L']

    p = ['A', 'B', 'D', 'E', 'C', 'F']
    s = ['N', 'N', 'L', 'L', 'N', 'L']

    root = construct(p)

    trav = []
    preorder(root, trav)
    print ' '.join(trav)
#!/usr/bin/python

class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def buildTreeUtil(preOrd, inOrd, s, e):
    if s > e:
        return None

    # Create a node from the current preIndx 
    root = Node(preOrd[buildTreeUtil.preIndx])

    # Find the index of this node in inOrd array
    inIndx = inOrd.index(preOrd[buildTreeUtil.preIndx])

    # Increment the preIndx
    buildTreeUtil.preIndx += 1

    if s == e:
        return root

    root.left = buildTreeUtil(preOrd, inOrd, s, inIndx-1)
    root.right = buildTreeUtil(preOrd, inOrd, inIndx+1, e)

    return root

def buildTree(inOrd, preOrd):
    buildTreeUtil.preIndx = 0
    return buildTreeUtil(preOrd, inOrd, 0, len(inOrd)-1)

def preorder(root, pOrd):
    if root is None:
        return

    pOrd.append(str(root.data))
    preorder(root.left, pOrd)
    preorder(root.right, pOrd)

if __name__ == "__main__":
    inOrd = ['D', 'B' ,'E', 'A', 'F', 'C']
    preOrd = ['A', 'B', 'D', 'E', 'C', 'F']

    root = buildTree(inOrd, preOrd)

    trav = []
    preorder(root, trav)
    print ' '.join(trav)
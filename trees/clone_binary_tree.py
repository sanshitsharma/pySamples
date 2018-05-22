#!/usr/bin/python

from ds.BST import BST, BNode

def clone(root):
    if root is None:
        return None

    newRoot = BNode(root.value)
    newRoot.left = clone(root.left)
    newRoot.right = clone(root.right)

    return newRoot

def cloneTree(bst):
    newRoot = clone(bst.root)
    return BST(newRoot)

if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    newBst = cloneTree(bst)

    print "Original Tree Preorder"
    print bst.preorder()

    print "New Tree Preorder"
    print newBst.preorder()

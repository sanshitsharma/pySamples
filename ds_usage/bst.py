#!/usr/bin/python

from ds.BST import BST, Type

def main():
    bst = BST()

    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print bst.breadth_first_traversal()

    print bst.depth_first_traversal()
    
    print bst.height()

    #bst.print_bst(Type.PREORDER)

    #print bst.serialize()

    """
    num = 40
    print "Inorder Successor of " + str(num) + " --> " + str(bst.inorder_successor(num))

    val = 10
    parent = bst.find_parent(val)
    if parent == 0:
        print "'" + str(val) + "' is the Root Node"
    elif parent == -1:
        print "'" + str(val) + "' does not exists in the BST"
    else:
        print "parent of '" + str(val) + "' --> '" + str(parent) + "'"
    

    bst.delete(70)
    bst.print_bst(Type.PREORDER)
    """

if __name__ == "__main__":
    main()

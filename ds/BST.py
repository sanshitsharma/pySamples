#!/usr/bin/python

from enum import Enum

class BNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_children(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        
        return children

class Type(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class BST:
    def __init__(self):
        self.root = None
    
    def __insert_recurse(self, node, value):
        if node is None:
            return BNode(value)

        if value <= node.value:
            node.left = self.__insert_recurse(node.left, value)
        else:
            node.right = self.__insert_recurse(node.right, value)

        return node

    def insert(self, value):
        self.root = self.__insert_recurse(self.root, value)

    def __serialize(self, curr, result=''):
        if curr is None:
            result += '# '
            return result

        result += str(curr.value) + ' '
        result = self.__serialize(curr.left, result)
        result = self.__serialize(curr.right, result)

        return result

    def serialize(self):
        result = ''
        result = self.__serialize(self.root, result)
        return result

    def __preorder_traverse(self, node, pre_list=None):
        if node is None:
            return

        if pre_list is None:
            pre_list = []

        pre_list.append(node.value)
        self.__preorder_traverse(node.left, pre_list)
        self.__preorder_traverse(node.right, pre_list)

    def preorder(self):
        pre_list = []
        self.__preorder_traverse(self.root, pre_list)

        return pre_list

    def __inorder_traverse(self, node, in_list=None):
        if node is None:
            return

        if in_list is None:
            in_list = []

        self.__inorder_traverse(node.left, in_list)
        in_list.append(node.value)
        self.__inorder_traverse(node.right, in_list)

    def inorder(self):
        in_list = []
        self.__inorder_traverse(self.root, in_list)

        return in_list

    def __postorder_traverse(self, node, post_list=None):
        if node is None:
            return

        if post_list is None:
            post_list = []

        self.__postorder_traverse(node.left, post_list)
        self.__postorder_traverse(node.right, post_list)
        post_list.append(node.value)

    def postorder(self):
        post_list = []
        self.__postorder_traverse(self.root, post_list)
        
        return post_list

    def print_bst(self, traversal_type = Type.PREORDER):
        if traversal_type == Type.PREORDER:
            print self.preorder()
        elif traversal_type == Type.INORDER:
            print self.inorder()
        else:
            print self.postorder()

    def __delete(self, node, parent, is_root):
        children = node.get_children()
        num_children = len(children)

        if num_children == 0: # Case 1: Target node is a leaf node
            if parent is None and is_root:
                self.root = None
            else:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        elif num_children == 1: # Case 2: Target node has 1 child
            if parent is None and is_root:
                # Corner case, root has one child and root needs to be deleted
                self.root = children[0]
            else:
                if parent.left == node:
                    parent.left = children[0]
                else:
                    parent.right = children[0]
        else: # Case 3: Target node has 2 children
            inorder_succ = self.__inorder_succ_recurse(self.root, node.value, None)
            # Swap the value of node with value of inorder succ and then call delete again
            # on the inorder successor node
            temp = node.value
            node.value = inorder_succ.value
            inorder_succ.value = temp
            print "Swapped.."
            self.print_bst(Type.PREORDER)

            return self.delete(inorder_succ.value)

    def delete(self, value):
        # delete in BST is two step process:
        # 1. Find the node in the BST
        # 2. Delete the node: Deleting a node 'a' itself can be classifed into 3 categories:
        #   i. Node 'a' is a leaf node: Node can be delete and the parent pointer can be set to None
        #   ii. Node 'a' has one child node ('b'): Value of 'a' is replaced by value of 'b' and 'b' is delete by setting the pointer of 'a' to None
        #   iii. Node 'a' has two children ('b' & 'c'): Node 'a' needs to be replaced with it's in-order successor and then the successor needs to be 
        #        evaluated for deletion based on the above criterias

        node = self.__get_node_recurse(value, self.root)
        if node is None:
            print "Value", value, "does not exist in BST"
            return

        parent, is_root = self.__find_parent_recurse(node.value, self.root, None, True)
        print "Parent:", parent.value

        return self.__delete(node, parent, is_root)

    def __get_node_recurse(self, value, curr):
        if curr is None:
            return None
        if value == curr.value:
            return curr
        elif value < curr.value:
            return self.__get_node_recurse(value, curr.left)
        else:
            return self.__get_node_recurse(value, curr.right)

    def get_node(self, value):
        return self.__get_node_recurse(value, self.root)

    def __inorder_succ_recurse(self, curr, trgt_value, successor):
        if curr is None:
            return None

        if curr.value == trgt_value:
            if curr.right is not None:
                curr = curr.right
                successor = curr
                while curr.left is not None:
                    curr = curr.left
                    successor = curr

            return successor

        if trgt_value < curr.value:
            successor = self.__inorder_succ_recurse(curr.left, trgt_value, curr)
        else:
            successor = self.__inorder_succ_recurse(curr.right, trgt_value, successor)

        return successor

    def inorder_successor(self, trgt):
        succ = self.__inorder_succ_recurse(self.root, trgt, None)
        if succ is not None:
            return succ.value
        else:
            return None

    def __find_parent_recurse(self, value, curr, parent, is_root):
        if curr is None:
            return None, False
        elif value == curr.value:
            return parent, is_root
        elif value < curr.value:
            parent, is_root = self.__find_parent_recurse(value, curr.left, curr, False)
        else: # value > curr.value:
            parent, is_root = self.__find_parent_recurse(value, curr.right, curr, False)

        return parent, is_root

    def find_parent(self, value):
        parent, is_root = self.__find_parent_recurse(value, self.root, None, True)
        if parent is not None:
            return parent.value
        else:
            if is_root:
                return 0
            return -1

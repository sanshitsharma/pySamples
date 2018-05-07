#!/usr/bin/env python

from ds.LinkedList import LinkedList

def length_recurse(node):
    if node is None:
        return 0

    return 1 + length_recurse(node.next_node)

def length(ll):
    if ll is None:
        raise ValueError('invalid list object')

    return length_recurse(ll.head)

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_end(1)
    l.insert_at_end(2)
    l.insert_at_end(3)
    l.insert_at_end(4)
    l.insert_at_end(5)

    print "List Length =", length(l)

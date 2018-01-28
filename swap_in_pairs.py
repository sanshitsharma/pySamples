#!/usr/bin/python

from ds.LinkedList import LinkedList

def print_node(node):
    if node is None:
        return None
    else:
        return node.get_data()

def main():
    print "Given a Linked list, swap nodes in pairs. DO NOT swap the values in the nodes"
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)

    ll.show()

    prev = ll.head
    l = ll.head
    r = l.get_next()

    while r is not None:
        temp = r.get_next()

        #print "prev:", print_node(prev), "left:", print_node(l), "right:", print_node(r), "temp:", print_node(temp)
        r.next_node = l
        l.next_node = temp

        if prev == ll.head:
            ll.head = r
        else:
            prev.next_node = r

        prev = l
        l = temp
        if l is not None:
            r = l.get_next()
        else:
            r = None

    ll.show()

if __name__ == "__main__":
    main()
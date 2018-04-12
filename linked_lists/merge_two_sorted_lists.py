#!/usr/bin/python

from ds.LinkedList import LinkedList

def sorted_merge(l1, l2):
    if l1 is None or l1.head is None:
        return l2
    
    if l2 is None or l2.head is None:
        return l1
        
    if l1.head.data > l2.head.data:
        l1, l2 = l2, l1

    prev = None
    curr = l1.head

    while True:
        while curr is not None and l2.head is not None and curr.data < l2.head.data:
            prev = curr
            curr = curr.next_node
        
        if l2.head is None:
            break

        temp = l2.head
        l2.head = l2.head.next_node

        # Insert temp in l1
        prev.next_node = temp
        temp.next_node = curr
        prev = temp

    if l2.head is not None:
        # We have reached the end of list 1 but there are elements in list 2
        # Simply append the remainder to list 2 to list 1
        prev.next_node = l2.head

if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(3)
    l1.insert_at_end(5)
    l1.insert_at_end(7)

    l2 = LinkedList()
    #l2.insert_at_end(2)
    #l2.insert_at_end(4)
    #l2.insert_at_end(6)
    #l2.insert_at_end(8)

    sorted_merge(l2, l1)
    string = ''
    for node in l1:
        string += str(node) + ' '
    print string
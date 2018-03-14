#!/usr/bin/python

#from ds.LinkedList import LinkedList
from ds.LinkedList import LinkedList

def zig_zag_list(llist):
    if llist.head is None or llist.head.get_next() is None:
        print "nothing to zig zag"
        return

    # Step 1: find the point from where we need to start reversing the list
    # Use a modified mid point determination method, which points to n/2 -1 
    # index node when 'n' is even
    slow = llist.head
    fast = llist.head

def main():
    print "Welcome to data structure test module"

    print "Testing insertion to linked list"
    llist = LinkedList()
    llist.insert_at_head(3)
    llist.insert_at_head(5)
    llist.insert_at_end(8)
    llist.insert_at_end(1)
    llist.insert_at_end(10)

    print "\nPretty print the list"
    llist.show()

    print "\nIterate over the list"
    for val in llist:
        print val

    print "\nTesting delete from linked list"
    llist.delete_from_head()
    llist.delete_from_end()
    llist.show()

    print "\nTesting reversing a linked list"
    llist.reverse()
    llist.show()

    print "\nTesting find linked list mid point"
    print "Mid: " + str(llist.get_mid().data)

    print "\nCreate a new linked list"
    ll = LinkedList()
    ll.insert_at_end('a')
    ll.insert_at_end('b')
    ll.insert_at_end('c')
    ll.insert_at_end('d')
    ll.insert_at_end('e')
    ll.insert_at_end('f')
    ll.show()

    #zig_zag_list(ll)
    
    # Write a function to modify the linked list such that 
    # a -> b -> c -> d -> e -> f becomes a -> f -> b -> e -> c -> d
    
if __name__ == "__main__":
    main()
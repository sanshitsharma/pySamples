#!/usr/bin/env python

'''
Given a linked list, interleave the list as follows:

Input: a --> b --> c --> d --> e
Output: a --> e --> b --> d --> c

Input: a --> b --> c --> d --> e --> f
Output: a --> f --> b --> e --> c --> d

Ref: Asked in Facebook phone interview
'''

from ds.LinkedList import LinkedList

# Modified implementation of the find mid in linked list. This function
# returns the mid node, node before mid and the length of the list.
# If the list length is odd, we will reverse from the node next to mid
# But if the list length is even, we will reverse from mid in which case,
# we will have a previous pointer
def get_mid(ll):
    prev = None
    slow = ll.head
    fast = ll.head
    length = 0

    if ll.head != None:
        while fast is not None and fast.next_node is not None:
            fast = fast.next_node.next_node
            prev = slow
            slow = slow.next_node
            length += 2

        if fast is not None:
            length += 1

    if length%2 == 0:
        return prev

    return slow

def reverse_from_middle(ll):
    if ll.head is None:
        return

    mid = get_mid(ll)

    prev = mid
    curr = mid.next_node

    while curr is not None:
        temp = curr.next_node
        if prev == mid:
            prev.next_node = None
            curr.next_node = None
        else:
            curr.next_node = prev
        
        prev = curr
        curr = temp

    if mid != prev:
        mid.next_node = prev

def interleave_list(ll):
    reverse_from_middle(ll)
    # Find mid
    mid = get_mid(ll)

    left = ll.head
    right = mid.next_node

    while left != mid:
        temp = left.next_node
        left.next_node = right
        mid.next_node = right.next_node
        right.next_node = temp

        # Reset left and right
        left = temp
        right = mid.next_node
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end('a')
    ll.insert_at_end('b')
    ll.insert_at_end('c')
    ll.insert_at_end('d')
    ll.insert_at_end('e')
    ll.insert_at_end('f')

    #reverse_from_middle(ll)
    interleave_list(ll)

    ll.show()
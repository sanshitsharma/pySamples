#!/usr/bin/env python

'''
Problem #61
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

Ref: https://leetcode.com/problems/rotate-list/description/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return
        
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = ListNode(val)

def show(head):
        curr = head
        string = ''
        while curr.next is not None:
            string += str(curr.val) + " --> "
            curr = curr.next

        string += str(curr.val)
        return string

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        if head.next is None:
            return head

        curr = head
        count = 1
        while count < k and curr.next is not None:
            count += 1
            curr = curr.next

        if count < k:
            k = k%count

        # At this point, count is == k
        if count == k and curr.next is None:
            # Length of list == k, k rotations will bring the list to same state
            return head

        # Now the rotations
        slow = head
        fast = head
        for i in range(0, k):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Slow is now pointing to the node that needs to become the last node
        fast.next = head
        head = slow.next
        slow.next = None

        return head

if __name__ == "__main__":
    l = List()
    l.insert('a')
    l.insert('b')
    l.insert('c')
    #l.insert('d')
    #l.insert('e')

    k = 4

    print show(l.head)

    head = Solution().rotateRight(l.head, k)
    print show(head)


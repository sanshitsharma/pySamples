#!/usr/bin/python

'''
Problem #234
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

Ref: https://leetcode.com/problems/palindrome-linked-list/description/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        curr = head
        res = ''
        while curr.next is not None:
            res += str(curr.val) + ' --> '
            curr = curr.next
        
        res += str(curr.val)

        return res

class Solution(object):
    def _getMid(self, head):
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow
        
    def _reverse(self, head):
        prev = head.next
        curr = prev.next

        while curr:
            temp = curr.next
            curr.next = prev
            if prev == head.next:
                prev.next = None
            prev = curr
            curr = temp

        head.next = prev

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return head

        # Find mid
        mid = self._getMid(head)

        # Reverse from mid
        self._reverse(mid)

        # Compare
        mid = mid.next
        start = head

        while mid:
            if start.val != mid.val:
                return False

            mid = mid.next
            start = start.next

        return True

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    obj = Solution()
    print obj.isPalindrome(head)
    print head
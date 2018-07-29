#!/usr/bin/python

'''
Problem #2
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their
nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Ref: https://leetcode.com/problems/add-two-numbers/description/
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addDigits(self, digits):
        sumD = 0
        carry = 0
        for digit in digits:
            sumD += digit

        if sumD > 9:
            carry = sumD/10
            sumD %= 10
        
        return sumD, carry

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumList = None
        listTail = None

        carry = 0

        while l1 and l2:
            s, carry = self.addDigits((l1.val, l2.val, carry))
            temp = ListNode(s)
            if not sumList:
                sumList = temp
                listTail = sumList
            else:
                listTail.next = temp
                listTail = listTail.next

            l1 = l1.next
            l2 = l2.next
        
        if not l1:
            l1 = l2

        while l1:
            s, carry = self.addDigits((l1.val, carry))
            temp = ListNode(s)
            if not sumList:
                sumList = temp
                listTail = sumList
            else:
                listTail.next = temp
                listTail = listTail.next
            
            l1 = l1.next
        
        if carry > 0:
            listTail.next = ListNode(carry)

        return sumList

def string(l):
    curr = l
    ans = []
    while curr:
        ans.append(str(curr.val))
        curr = curr.next

    #ans.reverse()
    return '->'.join(ans)

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(8)

    l2 = ListNode(5)
    l2.next = ListNode(1)
    l2.next.next = ListNode(3)


    l3 = Solution().addTwoNumbers(l1, l2)
    print string(l1), '+', string(l2), '=', string(l3)
#!/usr/bin/python

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        # Pass 1: Duplicate the nodes
        curr = head
        while curr:
            temp = RandomListNode(curr.label)
            temp.next = curr.next
            curr.next = temp
            curr = temp.next

        print printList(head)
        # Pass 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        
        # Pass 3: Extract the new list and restore the original
        curr = head
        newHead = None
        newTail = None

        while curr:
            if not newHead:
                newHead = curr.next
                newTail = newHead
            else:
                newTail.next = curr.next
                newTail = newTail.next

            curr.next = newTail.next
            newTail.next = None
            curr = curr.next

        return newHead

def printList(head):
    ans = []
    curr = head
    while curr:
        if curr.random:
            ans.append(curr.label + '(' + curr.random.label + ')')
        else:
            ans.append(curr.label + '(null)')
        curr = curr.next
    
    return ' --> '.join(ans)

if __name__ == "__main__":
    '''
    head = RandomListNode('a')
    head.next = RandomListNode('b')
    head.next.next = RandomListNode('c')

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head
    '''

    head = RandomListNode('-1')
    print "Ori List:", printList(head)

    newHead = Solution().copyRandomList(head)
    print "New List:", printList(newHead)

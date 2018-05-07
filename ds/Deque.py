#!/usr/bin/env python

from ds.DoublyLinkedList import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__q = DoublyLinkedList()

    def EnqueueFront(self, value):
        self.__q.insertAtHead(value)

    def EnqueueBack(self, value):
        self.__q.insertAtTail(value)

    def DequeueFront(self):
        return self.__q.deleteFromHead()

    def DequeueBack(self):
        return self.__q.deleteFromTail()

    def PeekFront(self):
        return self.__q.head.data

    def PeekBack(self):
        return self.__q.tail.data

    def show(self):
        self.__q.show()

    def isEmpty(self):
        return self.__q.isEmpty()

if __name__ == "__main__":
    dq = Deque()
    dq.EnqueueFront(3)
    dq.EnqueueFront(2)
    dq.EnqueueFront(1)
    dq.EnqueueBack(4)
    dq.EnqueueBack(5)
    dq.EnqueueBack(6)
    print "After 6 enqueues:"
    dq.show()

    dq.DequeueBack()
    dq.DequeueBack()
    dq.DequeueBack()
    dq.DequeueBack()
    print "After 4 dequeues"
    dq.show()
    
    dq.DequeueFront()
    print "After 1 more dequeues"
    dq.show()

    dq.DequeueFront()
    print "Finally:"
    dq.show()
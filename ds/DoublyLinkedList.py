#!/usr/bin/env python

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtHead(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAtTail(self, value):
        node = Node(value)
        if self.tail is None:
            self.tail = node
            self.head = self.tail

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def deleteFromHead(self):
        if self.head is None:
            return None

        node = self.head
        if self.head != self.tail:
            self.head.next.prev = None
        else:
            self.tail = None

        self.head = self.head.next
        return node.data

    def deleteFromTail(self):
        if self.tail is None:
            return None

        node = self.tail
        if self.head != self.tail:
            self.tail.prev.next = None
        else:
            self.head = None

        self.tail = self.tail.prev
        return node.data

    def search(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                return curr
        
        return None

    def isEmpty(self):
        return self.head == None

    def show(self):
        if self.isEmpty():
            print "DS is empty"
            return

        curr = self.head
        string = ''
        while curr.next is not None:
            string += str(curr.data) + ' <--> '
            curr = curr.next

        string += str(curr.data)
        print string

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insertAtHead(2)
    dll.insertAtTail(3)
    dll.insertAtHead(1)
    dll.insertAtTail(4)

    dll.show()

    print dll.deleteFromHead()
    dll.show()

    print dll.deleteFromTail()
    dll.show()
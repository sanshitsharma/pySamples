#!/usr/bin/python

class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        # Traverse to end of list
        curr = self.head
        while curr.get_next() != None:
            curr = curr.get_next()

        curr.set_next(Node(data))

    def show(self):
        curr = self.head
        list_str = ""
        while curr != None:
            if curr.get_next() != None:
                list_str = list_str + str(curr.data) + " --> "
            else:
                list_str = list_str + str(curr.data)

            curr = curr.get_next()

        print list_str

    def delete_from_head(self):
        if self.head is None:
            print "list is empty"
            return

        self.head = self.head.get_next()

    def delete_from_end(self):
        if self.head is None:
            print "list is empty"
            return
        
        if self.head.get_next() is None:
            self.head = None
            return

        curr = self.head
        while curr.get_next().get_next() is not None:
            curr = curr.get_next()

        curr.set_next(None)

    def reverse(self):
        if self.head is None or self.head.get_next() is None:
            print "nothing to reverse"
            return

        prev = self.head
        curr = prev.get_next()

        while curr is not None:
            last = curr.get_next()
            curr.set_next(prev)
            if prev == self.head:
                prev.set_next(None)

            prev = curr
            if last is None:
                self.head = curr
            curr = last

    def peek(self):
        return self.head.data

    def get_mid(self):
        if self.head is None or self.head.get_next() is None:
            print "nothing to do"
            return

        slow = self.head
        fast = self.head

        while fast != None and fast.get_next() != None:
            fast = fast.get_next().get_next()
            slow = slow.get_next()

        return slow
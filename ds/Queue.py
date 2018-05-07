#!/usr/bin/python

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, val):
        self.items.append(val)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        
        return self.items[0]

    def get(self):
        # returns the elements of queue as a list
        return list(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    items = q.get()
    print type(items)
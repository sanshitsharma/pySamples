#!/usr/bin/python

'''
This module provides a stable priority queue implementation using binary heap
with the following key fields that are maintained in each node
priority (int): lower value is higher priority, p1 > p2
entry_count (int): a number which stores the count at which the element
                   was added to the priority queue. this key helps us 
                   resolve contention when data is same
data (generic): this is the actual data
'''
'''
Node obj will be stored by priority queue
'''
class Node:
    def __init__(self, priority, entry_count, data):
        self.priority = priority
        self.entry_count = entry_count
        self.data = data

class PriorityQueue:
    def __init__(self):
        self.__pq = []
        self.__ec = 0
        self.__indx = 0

    def __iter__(self):
        return self

    def next(self):
        if self.__indx == len(self.__pq):
            self.__indx = 0
            raise StopIteration
        
        self.__indx = self.__indx + 1
        indx = self.__indx - 1
        #return (self.__pq[indx].priority, self.__pq[indx].entry_count, self.__pq[indx].data)
        return (self.__pq[indx].priority, self.__pq[indx].data)

    def __heapify(self):
        indx = len(self.__pq) - 1
        p_indx = (indx - 1)/2
        node = self.__pq[indx]
        p_node = self.__pq[p_indx]

        while indx > 0 and node.priority < p_node.priority:
            self.__pq[p_indx], self.__pq[indx] = self.__pq[indx], self.__pq[p_indx] #swap the elements
            indx = p_indx
            p_indx = (indx - 1)/2
            node = self.__pq[indx]
            p_node = self.__pq[p_indx]

    def add(self, priority, data):
        self.__ec = self.__ec + 1
        self.__pq.append(Node(priority, self.__ec, data))
        self.__heapify()

    def peek(self):
        if len(self.__pq) == 0:
            raise Exception("Underflow.. queue is empty")

        node = self.__pq[0]
        return (node.priority, node.data)

    def __check_count_and_swap(self, indx, c_indx):
        if self.__pq[indx].priority == self.__pq[c_indx].priority:
            if self.__pq[indx].entry_count > self.__pq[c_indx].entry_count:
                self.__pq[indx], self.__pq[c_indx] = self.__pq[c_indx], self.__pq[indx]
                return True
        elif self.__pq[indx].priority > self.__pq[c_indx].priority:
            self.__pq[indx], self.__pq[c_indx] = self.__pq[c_indx], self.__pq[indx]
            return True

        return False

    def __fix(self):
        indx = 0
        num_elems = len(self.__pq) - 1

        while indx <= num_elems:
            num_children = 0
            c1_indx = 2*indx + 1
            c2_indx = 2*indx + 2

            if c1_indx <= num_elems and c2_indx <= num_elems:
                num_children = 2
            elif c1_indx <= num_elems:
                num_children = 1

            '''            
            print "num children =", num_children
            elems = [(item.priority, item.entry_count, item.data) for item in self.__pq ]
            print elems
            '''

            if num_children == 2:
                if self.__pq[indx].priority >= self.__pq[c1_indx].priority and self.__pq[indx].priority >= self.__pq[c2_indx].priority:
                    # Find the children which takes preference
                    if self.__pq[c1_indx].priority <= self.__pq[c2_indx].priority:
                        swap_indx = c1_indx
                    else:
                        swap_indx = c2_indx
                    if self.__check_count_and_swap(indx, swap_indx):
                        indx = swap_indx
                elif self.__pq[indx].priority >= self.__pq[c1_indx].priority:
                    if self.__check_count_and_swap(indx, c1_indx):
                        indx = c1_indx
                elif self.__pq[indx].priority >= self.__pq[c2_indx].priority:
                    if self.__check_count_and_swap(indx, c2_indx):
                        indx = c2_indx
                else:
                    break
            elif num_children == 1:
                if self.__pq[indx].priority >= self.__pq[c1_indx].priority:
                    if self.__check_count_and_swap(indx, c1_indx):
                        indx = c1_indx
            else:
                break

    def remove(self):
        if len(self.__pq) == 0:
            raise Exception("Underflow.. queue is empty")

        node = self.__pq[0]
        self.__pq[0] = self.__pq[len(self.__pq) - 1]
        self.__pq.pop()
        self.__fix()

        return (node.priority, node.data)

    def is_empty(self):
        if len(self.__pq) == 0:
            return True

        return False

    def printQ(self):
        print self.__pq

def testPQ():
    pq = PriorityQueue()

    def iteratePQ(pq):
        print "Priority Queue Iteration"
        for datum in pq:
            print datum
        print    

    # Check if the queue is empty
    print "IsEmpty:", pq.is_empty()
    print

    # Add some value
    pq.add(3, 'abc')
    pq.add(2, 'def')
    pq.add(4, 'ghi')
    pq.add(1, 'jkl')

    # Iterate over the value
    iteratePQ(pq)

    # Check if the queue is empty
    print "IsEmpty:", pq.is_empty()
    print

    # Peek in the queue
    print "Peek:", pq.peek()
    print

    # Remove the smallest element and then print
    print "Remove:", pq.remove()
    iteratePQ(pq)

    # Add another element with same priority & iterate
    print "Add 'xyz'"
    pq.add(2, 'xyz')
    iteratePQ(pq)

    # remove element & iterate
    print "Remove:", pq.remove()
    iteratePQ(pq)

if __name__ == "__main__":
    testPQ()
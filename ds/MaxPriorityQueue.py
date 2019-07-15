#!/usr/bin/python

"""
A max priority queue implementation. Each node of the PQ stores a 
(key, value) pair. The PQ uses the key to maintain the heap property.

Input:
    key: an integer value used to maintain the heap property
    value: object
"""

class MaxPriorityQueue(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return '(' + str(self.key) + ', ' + str(self.value) + ')'

    def __init__(self):
        self.__pq = []

    def __repr__(self):
        return str(self.__pq)

    def push(self, key, value):
        self.__pq.append(MaxPriorityQueue.Node(key, value))
        currIdx = len(self.__pq) - 1
        while currIdx > 0:
            parentIdx = (currIdx - 1)/2
            if self.__pq[parentIdx].key >= key:
                break
            
            self.__pq[parentIdx], self.__pq[currIdx] = self.__pq[currIdx], self.__pq[parentIdx]
            currIdx = parentIdx

    def pop(self):
        if not self.__pq:
            raise ValueError('priority queue is empty')
        
        # Swap first and last elements of the array
        self.__pq[0], self.__pq[-1] = self.__pq[-1], self.__pq[0]
        pqNode = self.__pq.pop()

        if self.__pq:
            self._heapify(0)

        return pqNode.key, pqNode.value
    
    def _heapify(self, index):
        if not self._inBound(index):
            raise ValueError('invalid index to start heapifying. index' + str(index) + ' is out of bounds')
        
        lChildIdx = 2*index+1
        hasLeft = self._inBound(lChildIdx)

        rChildIdx = 2*index+2
        hasRight = self._inBound(rChildIdx)

        # Case 1: No children
        if not hasLeft and not hasRight:
            return
        # Case 2: Has two children
        elif hasLeft and hasRight:
            # If element at index is greater than both left and right, nothing to do
            if self.__pq[index] > self.__pq[lChildIdx] and self.__pq[index] > self.__pq[rChildIdx]:
                return
            
            # Else find the greater child and swap with it and then recurse
            isLeftGreater = False
            if self.__pq[lChildIdx] > self.__pq[rChildIdx]:
                isLeftGreater = True

            if isLeftGreater:
                # Swap
                self.__pq[lChildIdx], self.__pq[index] = self.__pq[index], self.__pq[lChildIdx]
                # Recurse
                self._heapify(lChildIdx)
            else:
                # Swap
                self.__pq[rChildIdx], self.__pq[index] = self.__pq[index], self.__pq[rChildIdx]
                # Recurse
                self._heapify(rChildIdx)
        # Case 3a: Has only Left Child
        elif hasLeft:
            if self.__pq[lChildIdx].key > self.__pq[index].key:
                # Swap
                self.__pq[lChildIdx], self.__pq[index] = self.__pq[index], self.__pq[lChildIdx]
                # Recurse
                self._heapify(lChildIdx)
            else:
                return
        # Case 3b: Has only Right Child
        else:
            if self.__pq[rChildIdx].key > self.__pq[index].key:
                # Swap
                self.__pq[rChildIdx], self.__pq[index] = self.__pq[index], self.__pq[rChildIdx]
                # Recurse
                self._heapify(rChildIdx)
            
    def _inBound(self, index):
        if index < len(self.__pq):
            return True
        
        return False

if __name__ == "__main__":
    pq = MaxPriorityQueue()
    try:
        pq.pop()
    except ValueError as ve:
        print ve

    pq.push(8, [2, -2])
    pq.push(13, [-3, 2])
    pq.push(10, [1, 3])
    print "Before pop:", pq

    key, value = pq.pop()
    print "fetched key:", key, " value:", value

    print "After Pop:", pq
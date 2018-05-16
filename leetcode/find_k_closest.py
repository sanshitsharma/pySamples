#!/usr/bin/python

'''
Problem #658: Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

Ref: https://leetcode.com/problems/find-k-closest-elements/description/
'''

''' 
The solution presented below is a linear time solution and has time complexity = O(n)
'''

class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return self.items

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
        return list(self.items)

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        q = Queue()
        for i in range(k):
            # Insert the first k elements to the queue
            q.enqueue(arr[i])

        for i in range(k, len(arr)):
            # If the distance of new element from x is less than
            # the distance of head of queue, remove head of queue 
            # and add the new element to the queue
            if abs(arr[i] - x) < abs(q.peek() - x):
                q.dequeue()
                q.enqueue(arr[i])

        return q.get()

if __name__ == "__main__":
    a = [1, 2, 4, 5, 6, 8, 11]
    k = 3
    x = 9

    res = Solution().findClosestElements(a, k, x)
    print res
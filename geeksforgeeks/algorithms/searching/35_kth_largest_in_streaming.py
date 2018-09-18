#!/usr/bin/env python

'''
K'th largest element in a stream
Given an infinite stream of integers, find the k'th largest element at any point of time.

Example:

Input:
stream[] = {10, 20, 11, 70, 50, 40, 100, 5, ...}
k = 3

Output:    {_,   _, 10, 11, 20, 40, 50,  50, ...}
Extra space allowed is O(k).

Ref: https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
'''

from ds.Heap import Heap, Type

class Solution():
    def kthLargest(self, arr, k):
        if k < 1:
            return []

        kHeap = Heap(Type.MIN)
        res = []
        for indx, elem in enumerate(arr):
            # Check the new element, if it's greater than the top of the heap,
            # insert it. Otherwise ignore and move on
            if kHeap.size() < k:
                kHeap.insert(elem)
            elif elem > kHeap.peek():
                kHeap.pop()
                kHeap.insert(elem)

            if indx < k-1:
                res.append('_')
            else:
                res.append(kHeap.peek())

        return res

if __name__ == "__main__":
    A = [10, 20, 11, 70, 50, 40, 100, 5]
    k = 4
    print Solution().kthLargest(A, k)
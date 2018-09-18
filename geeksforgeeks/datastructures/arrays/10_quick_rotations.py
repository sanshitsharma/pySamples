#!/usr/bin/env python

'''
Quickly find multiple left rotations of an array | Set 1
Given an array of size n and multiple values around which we need to left rotate the array. How to quickly find multiple left rotations?

Examples:
Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 1
        k2 = 3
        k3 = 4
        k4 = 6
Output : 3 5 7 9 1
         7 9 1 3 5
         9 1 3 5 7
         3 5 7 9 1

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 14 
Output : 9 1 3 5 7

Ref: https://www.geeksforgeeks.org/quickly-find-multiple-left-rotations-of-an-array/
'''

class Solution(object):
    def __init__(self, A):
        # Preprocess the array store it back to back
        self.arr = A
        self.__temp = A*2
        self.__len = len(self.arr)

    def leftRotate(self, k):
        if k < 1:
            return self.arr

        rotations = k % self.__len
        return self.__temp[rotations:rotations+self.__len]

    def rightRotate(self, k):
        if k < 1:
            return self.arr

        rotations = (self.__len - k)%self.__len
        return self.__temp[rotations:rotations+self.__len]

if __name__ == "__main__":
    A = [1, 3, 5, 7, 9]
    obj = Solution(A)
    print "Left Rotations"
    print "k = 1", obj.leftRotate(1)
    print "k = 0", obj.leftRotate(0)
    print "k = 5", obj.leftRotate(len(A))
    print "k = 4", obj.leftRotate(14)
    print "k = 2", obj.leftRotate(2)

    print "Right Rotations"
    print "k = 1", obj.rightRotate(1)
    print "k = 0", obj.rightRotate(0)
    print "k = 5", obj.rightRotate(len(A))
    print "k = 4", obj.rightRotate(14)
    print "k = 2", obj.rightRotate(2)

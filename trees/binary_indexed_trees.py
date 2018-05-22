#!/usr/bin/python

'''
A binary indexed tree or a Fenwick tree2 can be seen as a dynamic variant
of a prefix sum array. It supports two O(logn) time operations on an array:

1. processing a range sum query 
2. updating a value.

The advantage of a binary indexed tree is that it allows us to efficiently update
array values between sum queries. This would not be possible using a prefix sum
array, because after each update, it would be necessary to build the whole prefix
sum array again in O(n) time.

Structure:
Even if the name of the structure is a binary indexed tree, it is usually represented
as an array. In this section we assume that all arrays are one-indexed, because it
makes the implementation easier.

Let p(k) denote the largest power of two that divides k. We store a binary
indexed tree as an array tree such that
tree[k] = sumq(k-p(k)+1, k) = sum(tree[k-p(k)+1]:tree[k+1])

i.e., each position k contains the sum of values in a range of the original array
whose length is p(k) and that ends at position k. For example, since p(6) = 2,
tree[6] contains the value of sumq(5,6).
'''

class BinaryIndexedTree(object):
    def __init__(self, arr):
        self.a = [None] + arr
        self.__bit = [0] * len(self.a)
        self.__create()

    def __create(self):
        for k in range(1, len(self.a)):
            pk = k & -k
            self.__bit[k] = sum(self.a[k-pk+1:k+1])

    def __repr__(self):
        return str(self.__bit[1:])

    def updateIndex(self, indx, val):
        indx += 1
        if indx < 1 or indx > len(self.a) - 1:
            return None

        diff = val - self.__bit[indx]
        for k in range(indx, len(self.a)):
            pk = k & - k
            if indx >= k-pk+1 and indx <= k:
                self.__bit[k] += diff

    def sumToIndex(self, k):
        s = 0
        while k >= 1:
            s += self.__bit[k]
            k -= k & -k
        
        return s

    def sumRange(self, l, h):
        l += 1
        h += 1

        if l == 1:
            return self.sumToIndex(h)
        
        return self.sumToIndex(h) - self.sumToIndex(l) 

if __name__ == "__main__":
    a = [1, 3, 4, 8, 6, 1, 4, 2]
    bit = BinaryIndexedTree(a)
    print bit

    print "Sum range (0..3) =", bit.sumRange(0,3)
    print "Sum range (5..7) =", bit.sumRange(5,7)
    print "Sum range (0..6) =", bit.sumRange(0,6)

    bit.updateIndex(2, 7)
    print bit

    bit.updateIndex(6, 1)
    print bit
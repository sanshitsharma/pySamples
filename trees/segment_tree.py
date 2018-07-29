#!/usr/bin/python

import math

class SegmentTree(object):
    '''
    @paramin: arr - Array of elements from which segment tree is created
    '''
    def __init__(self, arr):
        n = len(arr) # array length

        self.h = int(math.ceil(math.log(n, 2))) # Segment tree height
        self.max_size = 2 * pow(2, self.h) - 1 # Maximum length of segment tree array
        self.st = [0] * self.max_size # Segment tree array

        self._constructSTUtil(arr, 0, n-1, self.st, 0)

    def _constructSTUtil(self, arr, ss, se, st, si):
        if ss == se:
            st[si] = arr[ss]
            return arr[ss]

        mid = ss + (se-ss)/2
        st[si] = self._constructSTUtil(arr, ss, mid, st, 2*si+1) + self._constructSTUtil(arr, mid+1, se, st, 2*si+2)
        return st[si]

    def __repr__(self):
        return str(self.st)

if __name__ == "__main__":
    a = [2, 3, 7, 4, 1]
    st = SegmentTree(a)

    print st

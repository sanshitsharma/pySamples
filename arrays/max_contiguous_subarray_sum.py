#!/usr/bin/python

import sys

def maxContiguousSum(a):
    maxSoFar = -sys.maxint - 1
    maxEndingHere = 0
    s = 0
    start = 0
    end = 0

    for i in range(len(a)):
        '''
        maxEndingHere = max(a[i], maxEndingHere + a[i])
        if maxEndingHere + a[i] > a[i]:

        maxSoFar = max(maxEndingHere, maxSoFar)
        '''
        maxEndingHere += a[i]

        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            start = s
            end = i

        if maxEndingHere < 0:
            maxEndingHere = 0
            s = i + 1
            print "s =", s

    return maxSoFar, start, end

if __name__ == "__main__":
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    #a = [-2, -3, -1, -2]
    maxSum, s, e = maxContiguousSum(a)
    print "Maximum contiguous sub-array sum =", maxSum, " start index:", s, "end index:", e
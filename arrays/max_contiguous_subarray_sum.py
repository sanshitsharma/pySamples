#!/usr/bin/python

import sys

def maxSubarraySum(a):
    max_sum = -sys.maxint - 1
    curr_sum = 0

    # Find the indices
    start = 0
    end = 0
    s = 0

    for i in range(len(a)):
        curr_sum += a[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = i

        if curr_sum < 0:
            curr_sum = 0
            s = i + 1

    return max_sum, start, end

if __name__ == "__main__":
    #a = [-2, -3, 4, -1, -2, 1, 5, -3]
    #a = [-2, -3, -1, -2]
    a = [-5, 6, 7, 1, 4, -8, 16]
    maxSum, s, e = maxSubarraySum(a)
    print "Maximum contiguous sub-array sum =", maxSum, " start index:", s, "end index:", e
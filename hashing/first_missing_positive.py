#!/usr/bin/python

'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

''' 
Solution:
Below is a hash based solution that runs in O(n) time. 
The downside is that it uses O(n) space. 
'''

import sys

def firstMissingPositive(a):
    shift = segregate(a)
    arr = a[shift:]
    size = len(arr)

    for i in range(len(arr)):
        if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]

    for i in range(len(arr)):
        if arr[i] > 0:
            return i + 1

    return size + 1

def segregate(a):
    j = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return j
'''
def segregate(a):
    j = 0
    for i in range(len(a)):
        if a[i] < 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return j

def find_missing(a):
    size = len(a)
    print a
    for i in range(size):
        print "Evaluating i =", i
        if abs(a[i]) - 1 < size and a[abs(a[i]) - 1] > 0:
            print "abs(a[i]) - 1 =", abs(a[i]) - 1, "size =", size
            print "a[abs(a[i]) - 1] =", a[abs(a[i]) - 1]
            a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]

    print a

def test(a):
    shift = segregate(a)
    find_missing(a[shift:])
'''

if __name__ == "__main__":
    lst = [2, 3, -7, 6, 8, 1, -10, 15]
    print "First missing positive number:", firstMissingPositive(lst)
    #test(lst)
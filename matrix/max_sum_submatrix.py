#!/usr/bin/python

import sys

def getMaxSubarraySum(a):
    max_sum = -sys.maxint - 1
    curr_sum = 0

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
            curr_sum = max(curr_sum, 0)
            s = i + 1

    return max_sum, start, end

def getElems(nr, col, arr, mat):
    for row in range(nr):
        arr[row] += mat[row][col]

def display(mat, top, bottom, left, right, max_sum):
    print "Max Sum =", max_sum
    for r in range(top, bottom+1):
        s = ''
        for c in range(left, right+1):
            s += str(mat[r][c]) + ' '
        print s

def getMaxSubmatrixSum(mat):
    nr = len(mat)
    nc = len(mat[0])

    curr_left = curr_right = curr_sum = 0
    max_left = max_right = max_top = max_bottom = 0
    max_sum = -sys.maxint - 1

    for curr_left in range(nc):
        # Temp array initialized to 0
        arr = [0 for x in range(nr)]
        for curr_right in range(curr_left, nc):
            getElems(nr, curr_right, arr, mat)
            curr_sum, start, end = getMaxSubarraySum(arr)

            if curr_sum > max_sum:
                max_sum = curr_sum
                max_left = curr_left
                max_right = curr_right
                max_top = start
                max_bottom = end
    
    #display(mat, max_top, max_bottom, max_left, max_right, max_sum)
    return max_sum, max_top, max_left, max_bottom, max_right
            
if __name__ == "__main__":
    mat = [[2, 1, -3, -4, 5], [0, 6, 3, 4, 1], [2, -2, -1, 4, -5], [-3, 3, 1, 0, 3]]
    max_sum, t, l, b, r = getMaxSubmatrixSum(mat)
    display(mat, t, b, l, r, max_sum)
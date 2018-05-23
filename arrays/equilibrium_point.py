#!/usr/bin/python

"""Given an array A your task is to tell at which position the equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.

Input:
The first line of input contains an integer T denoting the no of test cases then T test cases follow.
First line of each test case contains an integer N denoting the size of the array.
Then in the next line are N space separated values of the array A.

Output:
For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

Constraints:
1<=T<=100
1<=N<=100

Example:
Input:
2
1
1
5
1 3 5 2 2

Output:
1
3

Explanation:
1. Since its the only element hence its the only equilibrium point
2. For second test case equilibrium point is at position 3 as elements below it (1+3) = elements after it (2+2)

ref: https://practice.geeksforgeeks.org/problems/equilibrium-point/0 
"""

def get_equilibrium_point(a):
    l = 0
    r = len(a) - 1

    left_sum = 0
    right_sum = 0

    left_sum += a[l]
    right_sum += a[r]

    while l < r:
        #print "l =", l, "r =", r, "left_sum =", left_sum, "right_sum =", right_sum
        if (l == r or r - l == 2) and left_sum == right_sum:
            return l + 1

        if left_sum == right_sum:
            l += 1
            left_sum += a[l]
            r -= 1
            right_sum += a[r]
        elif left_sum > right_sum:
            r -= 1
            right_sum += a[r]
        else:
            l += 1
            left_sum += a[l]

    #print "Finally.. l =", l, "r =", r, "left_sum =", left_sum, "right_sum =", right_sum
    return -1

if __name__ == "__main__":
    #lst = [1, 3, 5, 2, 2]
    #lst = [4, 4, 1, 4, 5, 13]
    lst = [4, 42, 27, 16, 28, 3, 4, 5, 9, 3, 31, 5, 5, 29, 10, 18, 35, 35, 33, 19, 41, 23, 8, 32, 9, 5, 8, 18, 35, 13, 6, 7, 6, 10, 11, 13, 37, 2, 25, 7, 28, 43]
    print get_equilibrium_point(lst)
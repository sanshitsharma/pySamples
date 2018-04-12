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
    left_sum = 0
    right_sum = 0

    # Calculate the left and right sum
    n = len(a)
    for i in range(n):
        if i < n/2:
            left_sum += a[i]
        
        if i > n/2:
            right_sum += a[i]

    print "left_sum =", left_sum
    print "right_sum =", right_sum

    # Now we compare left_sum and right_sum and try to make them equal
    '''
    Set mid = n/2 
    while mid < n and left_dum != right_sum:
        if left sum < right sum, move one position to right and recalculate
    '''


if __name__ == "__main__":
    #lst = [1, 3, 5, 2, 2]
    lst = [4, 4, 3, 4, 5, 13]
    print get_equilibrium_point(lst)
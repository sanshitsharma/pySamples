#!/usr/bin/python

"""
Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:

Corresponding to each test case, in a new line, print the starting and ending positions of first such occuring subarray if sum equals
to subarray, else print -1.

Note: Position of 1st element of the array should be considered as 1.

Expected Time Complexity: O(n)

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= an array element <= 200

Example:

Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10

Output:
2 4
1 5

Explanation : 
In first test case, sum of elements from 2nd position to 4th position is 12
In second test case, sum of elements from 1st position to 5th position is 15
"""

def subarray_with_sum(arr, k):
    # Start with two pointers left and right both from index 0
    l = 0
    r = 0

    curr_sum = 0

    # in a loop start adding numbers until:
    # curr sum == k, return l, r
    # curr sum < k, add arr[r] to curr_sum
    # curr sum > k, subtract arr[l] from curr_sum
    while r < len(arr):
        if curr_sum == k:
            return (l+1, r) # because the solution wants first index to be 1
        
        if curr_sum < k:
            curr_sum += arr[r]
            r += 1
            continue

        if curr_sum > k:
            curr_sum -= arr[l]
            l += 1

    return -1

if __name__ == "__main__":
    #arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #k = 15
    arr = [1, 2, 3, 7, 5]
    k = 41
    print subarray_with_sum(arr, k)
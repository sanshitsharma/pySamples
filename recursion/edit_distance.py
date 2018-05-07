#!/usr/bin/env python

'''
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a

Ref: https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/ 
'''

count = 0

def edit_dist(a, b, m , n):
    global count
    count += 1

    if m == 0:
        return n

    if n == 0:
        return m

    if a[m-1] == b[n-1]:
        return edit_dist(a, b, m-1, n-1)
    else:
        return 1 + min(edit_dist(a, b, m, n-1), edit_dist(a, b, m-1, n), edit_dist(a, b, m-1, n-1))

if __name__ == "__main__":
    a = 'horse'
    b = 'ros'

    dist = edit_dist(a, b, len(a), len(b))
    print dist

    print "Count =", count
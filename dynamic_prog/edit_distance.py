#!/usr/bin/python

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

import numpy as np

def editDistance(a, b):
    r = len(a) + 1
    c = len(b) + 1
    DT = np.zeros([r, c], dtype=int)
    #DT = [[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        for j in range(c):
            if i == 0:
                DT[i][j] = j
            elif j == 0:
                DT[i][j] = i
            elif a[i-1] == b[j-1]:
                DT[i][j] = DT[i-1][j-1]
            else:
                DT[i][j] = 1 + min(DT[i-1][j], DT[i][j-1], DT[i-1][j-1])

    print DT
    return DT[r-1][c-1]

if __name__ == "__main__":
    a = 'horse'
    b = 'ros'

    res = "Edit distance b/w '" + a + "' & '" + b +"' = " + str(editDistance(a, b))
    print res
#!/usr/bin/python

'''
Ways of transforming one string to other by removing 0 or more characters
Given two sequences A, B, find out number of unique ways in sequence A, to form a subsequence of A that is identical to the sequence B.
Transformation is meant by converting string A (by removing 0 or more characters) to string B.

Examples:
Input : A = "abcccdf", B = "abccdf"
Output : 3
Explanation : Three ways will be -> "ab.ccdf", 
"abc.cdf" & "abcc.df" .
"." is where character is removed. 

Input : A = "aabba", B = "ab"
Output : 4
Expalnation : Four ways will be -> "a.b..",
 "a..b.", ".ab.." & ".a.b." .
"." is where characters are removed.

Ref: https://www.geeksforgeeks.org/ways-transforming-one-string-removing-0-characters/
'''

import numpy as np 

def countTransformations(A, B):
    # Create a mxn 2D array where m = len(b) + 1 and n = len(a) + 1
    m = len(B) + 1
    n = len(A) + 1
    cT = np.zeros([m, n], dtype=int)

    # Build the solutions
    '''
    If i = 0, there is only 1 way to get to B[0..i] from A[0..j], i.e. remove all chars
    If j = 0 and i > 0, then there is no way to get to B[0..j] from A[0..i], so set cT[i][0] = 0 for i > 0
    If A[j] != B[i], we ignore A[j] and align B[0..i] with A[0..j-1]
    If A[j] == B[i] then cT[i][j] = cT[i-1][j] + cT[i-1][j-1]
    '''

    for i in range(m):
        for j in range(n):
            if i == 0:
                cT[i][j] = 1
            elif j == 0:
                cT[i][j] = 0
            elif A[j-1] != B[i-1]:
                cT[i][j] = cT[i][j-1]
            else: # A[j] == B[i]
                cT[i][j] = cT[i][j-1] + cT[i-1][j-1]

    #print cT
    return cT[m-1][n-1]

if __name__ == "__main__":
    #a = 'aabba'
    #b = 'ab'

    a = 'abcccdf'
    b = 'abccdf'

    res = "Number of way to transform '" + a + "' to '" + b + "' = " + str(countTransformations(a, b))
    print res
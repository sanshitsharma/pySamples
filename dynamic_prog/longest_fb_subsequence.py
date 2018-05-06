#!/usr/bin/python

'''
FB sequence

A sequence x_1, x_2,..., x_m is called FB sequence if it satisfies the condition:
There is no two adjacent elements which are coprime, i.e. gcd(xi, xi+1)=1 for each i (1<=i<m). (gcd = greatest common divisor)

Please find the longest subsequence from the given input sequence which can be called FB sequence.

Function definition:
function findLongestFBSequence(list<int> seq) -> int:

Example Input:
[2 3 4 6 9]

Example Output:
4

In the above example, following sequences are examples of FB sequences: [2; 4; 6; 9], [2; 4; 6], [3; 9], [6].
The length of the longest FB sequence is 4.
'''

'''
Helper Functions
'''

def gcd(a, b):
    while b != 0:
        a, b = b, a%b

    return a

def areCoprimes(a, b):
    return gcd(a, b) == 1

def lfbs(a):
    lfbs = [1 for x in a]

    for i in range(1, len(a)):
        for j in range(i):
            if not areCoprimes(a[i], a[j]) and lfbs[i] < lfbs[j] + 1:
                lfbs[i] = lfbs[j] + 1

    return max(lfbs)

if __name__ == "__main__":
    a = [2, 3, 4, 6, 9]
    print lfbs(a)
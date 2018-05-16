#!/usr/bin/python

'''
Min flips of continuous characters to make all characters same in a string

Given a string consisting only of 1's and 0's. In one flip we can change any continuous sequence of this string.
Find this minimum number of flips so the string consist of same characters only.

Examples:

Input : 00011110001110
Output : 2
We need to convert 1's sequence
so string consist of all 0's.

Input : 010101100011
Output : 4

Ref: https://www.geeksforgeeks.org/min-flips-of-continuous-characters-to-make-all-characters-same-in-a-string/
'''

def minFlips(n):
    zeroFlips = 0
    oneFlips = 0

    lastOneIndx = -1
    lastZeroIndx = -1

    i = 0
    while True:
        while i < len(n) and n[i] == '0':
            i += 1
        lastZeroIndx = i - 1

        if lastZeroIndx > lastOneIndx and lastOneIndx != -1:
            oneFlips += 1
            #print "i =", i, "lZI:", lastZeroIndx, "lOI:", lastOneIndx, "one flips:", oneFlips

        if i >= len(n):
            zeroFlips += 1
            break

        while i < len(n) and n[i] == '1':
            i += 1
        lastOneIndx = i - 1

        if lastOneIndx > lastZeroIndx and lastZeroIndx != -1:
            zeroFlips += 1
            #print "i =", i, "lZI:", lastZeroIndx, "lOI:", lastOneIndx, "zero flips:", zeroFlips

        if i >= len(n):
            oneFlips += 1
            break

    #print "zero flips:", zeroFlips
    #print "one flips:", oneFlips

    #return min(zeroFlips, oneFlips)

    minimum = min(zeroFlips, oneFlips)
    if minimum == 0:
        return "No flips needed"

    if zeroFlips < oneFlips:
        return "Flip " + str(zeroFlips) + " sets of consecutive 0's to make all 1's"
    elif oneFlips < zeroFlips:
        return "Flip " + str(oneFlips) + " sets of consecutive 1's to make all 0's"
    else:
        return "Flip " + str(oneFlips) + " sets of consecutive 1's or 0's to make all 0's or 1's"

if __name__ == "__main__":
    #n = '010101100011'
    n = '00011110001110'
    #n = '1111'
    print minFlips(n)
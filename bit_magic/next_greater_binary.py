#!/usr/bin/python

'''
Given a binary input that represents binary representation of positive number n, find binary representation of smallest number greater
than n with same number of 1's and 0's as in binary representation of n. If no such number can be formed, print "no greater number".

The binary input may be and may not fit even in unsigned long long int.

Examples:

Input : 10010
Output : 10100
Here n = (18)10 = (10010)2
next greater = (20)10 = (10100)2
Binary representation of 20 contains same number of
1's and 0's as in 18.

Input : 111000011100111110
Output :  111000011101001111

Ref: https://www.geeksforgeeks.org/binary-representation-next-greater-number-number-1s-0s/ 
'''

def nextGreaterBin(s):
    if len(s) < 2:
        return "no greater binary"

    a = list(s)
    count = 0
    i = len(a) - 1

    while i >= 0 and a[i] == '0':
        a[i] = '1'
        count += 1
        i -= 1

    if i == 0:
        return "no greater binary"

    while a[i] == '1' and i > -1:
        i -= 1

    if i < 0:
        return "no greater binary"

    a[i] = '1'
    i += 1
    count += 1

    while count > 0 and i < len(a):
        a[i] = '0'
        count -= 1
        i += 1
    
    if i > len(a):
        return "no greater binary"

    return ''.join(a)

if __name__ == "__main__":
    #s = '111'
    #s = '111000011100111110'
    s = '101110'
    print nextGreaterBin(s)
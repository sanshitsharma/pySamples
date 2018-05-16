#!/usr/bin/python

'''
Add two bit strings
Given two bit sequences as strings, write a function to return the addition of the two sequences. Bit strings can be of different
lengths also. For example, if string 1 is “1100011” and second string 2 is “10”, then the function should return “1100101”.

Ref: https://www.geeksforgeeks.org/add-two-bit-strings/ 
'''

def addBinary(a, b):
    diff = len(a) - len(b)
    if diff > 0:
        b = ('0' * diff) + b
    elif diff < 0:
        a = ('0' * -diff) + a

    carry = 0
    res = []

    for i in range(len(a) - 1, -1, -1):
        aBit = ord(a[i]) - ord('0')
        bBit = ord(b[i]) - ord('0')

        res = [str(aBit ^ bBit ^ carry)] + res
        carry = (aBit & bBit) | (bBit & carry) | (carry & aBit)

    if carry == 1:
        res = ['1'] + res

    return ''.join(res)

if __name__ == "__main__":
    a = '1100011'
    b = '10'

    r = addBinary(a, b)
    string = "'" + a + "' + '" + b + "' = " + r
    print string
#!/usr/bin/python

'''
The problem is to check whether the decimal representation of the given binary number is divisible by 5 or not.
Take care, the number could be very large and may not fit even in long long int. The approach should be such that
there are zero or minimum number of multiplication and division operations. No leading 0's are there in the input.

Examples:

Input : 1010
Output : YES
(1010)2 = (10)10,
and 10 is divisible by 5.

Input : 10000101001
Output : YES

Ref: https://www.geeksforgeeks.org/decimal-representation-given-binary-string-divisible-5-not/
'''

def convertBinaryToBase4(n):
    base4Map = {'00': '0', '01': '1', '10': '2', '11': '3'}
    # Start pairing from right
    nBase4 = []
    for i in range(len(n)-1, -1, -2):
        if i == 0:
            nBase4 = [base4Map['0'+n[i]]] + nBase4
        else:
            nBase4 = [base4Map[n[i-1:i+1]]] + nBase4

    return ''.join(nBase4)

def isDivisibleBy5(n):
    n = convertBinaryToBase4(n)
    oddSum = 0
    evenSum = 0
    for i in range(len(n)):
        if i%2 == 0:
            oddSum += (ord(n[i]) - ord('0'))
        else:
            evenSum += (ord(n[i]) - ord('0'))

    return (oddSum - evenSum)%5 == 0

if __name__ == "__main__":
    n = '100100'
    if isDivisibleBy5(n):
        print 'YES'
    else:
        print 'NO'

#!/usr/bin/python

'''
Generate all binary strings from given pattern
Given a string containing of '0', '1' and '?' wildcard characters, generate all binary strings that can be formed by replacing each
wildcard character by '0' or '1'.

Input str = "1??0?101"
Output: 
        10000101
        10001101
        10100101
        10101101
        11000101
        11001101
        11100101
        11101101

Ref: https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/
'''

def generateStrings(s):
    a = list(s)
    res = []
    indx = 0

    generate(a, indx, res)
    return res

def generate(a, indx, res):
    if indx >= len(a):
        res.append(''.join(a))
        return

    if a[indx] != '?':
        return generate(a, indx+1, res)

    a[indx] = '0'
    generate(a, indx+1, res)
    a[indx] = '1'
    generate(a, indx+1, res)
    a[indx] = '?'

if __name__ == "__main__":
    #s = '1??0?101'
    s = '1?0?'
    r = generateStrings(s)
    for st in r:
        print st
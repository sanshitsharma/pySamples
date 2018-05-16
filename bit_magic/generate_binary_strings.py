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

def generate(a, i, res):
    if i < 0:
        res.append(''.join(a))
        return

    if a[i] != '?':
        return generate(a, i-1, res)

    a[i] = '0'
    generate(a, i-1, res)
    a[i] = '1'
    generate(a, i-1, res)
    a[i] = '?' # backtracking

def generateStrings(s):
    res = []
    a = list(s)
    n = len(s) - 1

    generate(a, n, res)
    return res

if __name__ == "__main__":
    s = '1??0?101'
    r = generateStrings(s)
    for st in r:
        print st
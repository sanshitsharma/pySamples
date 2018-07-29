#!/usr/bin/python

'''
Given a string, find all it's subsequences
'''

def allSubsequences(s):
    n = len(s)
    
    res = []

    for i in range(pow(2,n)):
        ss = ''
        j = n - 1
        while i != 0:
            if i & 1 == 1:
                ss = s[j] + ss
            j -= 1
            i = i >> 1

        res.append(ss)

    return res

def subsequenceByN(string, n):
    l = len(string)
    res = []

    for i in range(pow(2, l)):
        ss = ''
        j = l - 1
        while i != 0:
            if i & 1 == 1:
                ss = string[j] + ss
            j -= 1
            i = i >> 1

        if ss != '' and int(ss)%n == 0:
            res.append(ss)

    return res

if __name__ == "__main__":
    s = '676'
    n = 3
    #print allSubsequences(s)
    print subsequenceByN(s, n)
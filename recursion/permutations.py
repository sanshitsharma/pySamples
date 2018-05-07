#!/usr/bin/python

def permute(a, p, start, end):
    if start == end:
        p.append(list(a))
        return
    
    for i in range(start, end+1):
        a[i], a[start] = a[start], a[i]
        permute(a, p, start+1, end)
        a[i], a[start] = a[start], a[i]

def getAllPermutations(s):
    p = []
    permute(s, p, 0, len(s)-1)
    return p

if __name__ == "__main__":
    s = 'abc'
    print getAllPermutations(list(s))
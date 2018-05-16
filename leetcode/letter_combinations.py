#!/usr/bin/python

'''
class Solution(object):
    def __init__(self):
        self.kMap = {'0': ['0'], '1': ['1'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    
    def letterCombinations(self, digits)
'''

#def permute(a, b, a_l, a_h, b_l, b_h):

def permute(a, low, high):
    if low == high:
        print ''.join(a)
        return
    
    for i in range(low, high+1):
        a[i], a[low] = a[low], a[i]
        permute(a, low+1, high)
        a[i], a[low] = a[low], a[i]

def allPermutations(s1):#, s2):
    a = list(s1)
    #b = list(s2)

    #permute(a, b, 0, len(a)-1, 0, len(b)-1)
    permute(a, 0, len(a)-1)

if __name__ == "__main__":
    s1 = 'aaabbb'
    #s2 = 'def'

    allPermutations(s1)#, s2)
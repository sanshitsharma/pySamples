#!/usr/bin/python

'''
Given a set, print all subsets of the set
'''

def get_all_subsets(s):
    subsets = []
    for num in range(1<<len(s)):
        indx = 0
        ss = []
        while num != 0:
            if num & 1 == 1:
                ss.append(s[indx])
            indx += 1
            num = num >> 1
        subsets.append(''.join(ss))
    
    return subsets

if __name__ == "__main__":
    res = get_all_subsets(list('Vri'))
    print res
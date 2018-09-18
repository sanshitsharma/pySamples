#!/usr/bin/python

'''
Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers,
the consecutive numbers can be in any order.

Examples

Input: arr[] = {1, 9, 3, 10, 4, 20, 2};
Output: 4
The subsequence 1, 3, 4, 2 is the longest subsequence
of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
The subsequence 36, 35, 33, 34, 32 is the longest subsequence
of consecutive elements. 

Ref: https://www.geeksforgeeks.org/longest-consecutive-subsequence/ 
'''

def lcs(a):
    hash_map = {}
    # Insert all elements to hash
    for elem in a:
        hash_map[elem] = True

    '''
    Loop over the array elements again and do the following:
    1. check is a[i] - 1 exists in the map. If it doesn't exist, then
    a[i] is a start of a subsequence. 
    Keep looking for a[i] + 1 until no more can be found
    Check against the current lcs and replace as needed
    '''
    lcs = 0
    for elem in a:
        if (elem-1) not in hash_map.keys():
            curr_lcs = 1
            # Element is the beginning of a new subsequence. Now count
            while elem + 1 in hash_map.keys():
                curr_lcs += 1
                elem += 1
            
            lcs = curr_lcs if curr_lcs > lcs else lcs

    return lcs

if __name__ == "__main__":
    #print lcs([1, 9, 3, 10, 4, 20, 2])
    print "Length of longest consecutive subsequence =", lcs([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42])
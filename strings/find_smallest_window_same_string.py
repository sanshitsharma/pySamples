#!/usr/bin/env python

'''
Smallest window that contains all characters of string itself
Given a string, find the smallest window length with all distinct characters of the given string. For eg. str = "aabcbcdbca",
then the result would be 4 as of the smallest window will be "dbca" .

Examples:

Input  : aabcbcdbca
Output : dcba
Explanation : 
dbca of length 4 is the smallest 
window with highest number of distinct
characters.         

Input : aaab
Output : ab
Explanation : 
ab of length 2 is the smallest window 
with highest number of distinct characters.

Ref: https://www.geeksforgeeks.org/smallest-window-contains-characters-string/ 
'''

import sys

def find_smallest_window_containing_string(t):
    p_map = []

    for c in t:
        if c not in p_map:
            p_map.append(c)
    
    count = 0
    start = 0
    start_index = -1
    min_len = sys.maxint
    t_map = {}
    for i in range(len(t)):
        c = t[i]
        try:
            t_map[c] += 1
        except KeyError:
            t_map[c] = 1

        if t_map[c] <= 1:
            count += 1

        if count == len(p_map):
            while t_map[t[start]] > 1:
                t_map[t[start]] -= 1
                start += 1

            curr_len = i - start + 1
            if min_len > curr_len:
                min_len = curr_len
                start_index = start

    return t[start_index:start_index+min_len+1]
            

if __name__ == "__main__":
    #text = 'aabcbcdbca'
    text = 'aaab'
    print "Smallest Window:", find_smallest_window_containing_string(text)
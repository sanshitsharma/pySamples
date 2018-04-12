#!/usr/bin/python

'''
Find the smallest window in a string containing all characters of another string
Given two strings string1 and string2, find the smallest substring in string1 containing all characters of string2 efficiently.
For Example:

Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.

Input :  string = "geeksforgeeks"
         pattern = "ork" 
Output :  Minimum window is "ksfor"

ref: https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
'''

import sys

def smallest_window(text, pat):
    t_map = {}
    p_map = {}

    for c in pat:
        try:
            p_map[c] += 1
        except KeyError as ke:
            p_map[c] = 1

    start = 0
    start_index = -1
    count = 0
    min_window = sys.maxint

    for i in range(len(text)):
        c = text[i]
        #print "i =", i, "char[i]:", text[i]
        # Insert character to hash
        try:
            t_map[c] += 1
        except KeyError as ke:
            t_map[c] = 1

        # Increment the count only if the c is in pattern and number of times c is needed has not been exceeded
        if c in p_map.keys() and t_map[c] <= p_map[c]:
            count += 1

        # At some point when count == len(pat), we start to minimize the window
        if count == len(pat):
            while text[start] not in p_map.keys() or t_map[text[start]] > p_map[text[start]]:
                #print t_map
                if text[start] in p_map.keys() and t_map[text[start]] > p_map[text[start]]:
                    t_map[text[start]] -= 1

                start += 1

            curr_window = i - start + 1

            #print "Min:", min_window, "curr:", curr_window
            if min_window > curr_window:
                min_window = curr_window
                start_index = start
                #print "Found Window:", text[start:i+1], "Updated start:", start

    if start_index == -1:
        print "No such window exists"
        return None

    return text[start_index:start_index+min_window]


if __name__ == "__main__":
    text = 'this is a test string'
    pat = 'tist'

    print smallest_window(text, pat)
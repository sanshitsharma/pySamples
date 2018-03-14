#!/usr/bin/python

'''
Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.

Two strings are called k-anagrams if following two conditions are true.

Both have same number of characters.
Two strings can become anagram by changing at most k characters in a string.

Examples:
Input:  str1 = "anagram" , str2 = "grammar" , k = 3
Output:  Yes
Explanation: We can update maximum 3 values and 
it can be done in changing only 'r' to 'n' 
and 'm' to 'a' in str2.

Input:  str1 = "geeks", str2 = "eggkf", k = 1
Output:  No
Explanation: We can update or modify only 1 
value but there is a need of modifying 2 characters. 
i.e. g and f in str 2.
'''

def are_k_anagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False

    d = {}

    # Parse string 1
    for c in str1:
        if d.has_key(c):
            d[c] = d[c] + 1
        else:
            d[c] = 1

    # Parse string 2
    for c in str2:
        if d.has_key(c):
            d[c] = d[c] - 1
        else:
            d[c] = -1

    #print d
    ops = 0 # Count the number of operation
    char_sum = 0
    for v in d.itervalues():
        if v != 0:
            char_sum = char_sum + v
            ops = ops + abs(v)

    if char_sum == 0 and ops/2 <= k:
        return True

    return False

if __name__ == "__main__":
    print are_k_anagrams('anagram', 'grammar', 3)
    print are_k_anagrams('geeks', 'eggkf', 1)
    print are_k_anagrams('fodr', 'gork', 2)
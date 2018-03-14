#!/usr/bin/python

'''
Given a string of lower and uppercase characters, the task is to find that how many characters are at same position as in English alphabets.
Example:
Input:  ABcED 
Output :  3
First three characters are at same position
as in English alphabets.

Input:  geeksforgeeks 
Output :  1
Only 'f' is at same position as in English
alphabet

Input :  alphabetical 
Output :  3
'''

def find_count(string):
    count = 0
    string = string.lower()
    for i in xrange(0, len(string)):
        if ord(string[i]) - ord('a') == i:
            count = count + 1

    return count

if __name__ == "__main__":
    print 'ABcED -->', find_count('ABcED')
    print 'geeksforgeeks -->', find_count('geeksforgeeks')
    print 'alphabetical -->', find_count('alphabetical')
        
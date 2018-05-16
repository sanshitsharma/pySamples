#!/usr/bin/python

'''
Given a binary string (consists of only 0 and 1). If there is “100” as a sub-string in the string, then we can delete this sub-string.
The task is to find the length of longest sub-string which can be make removed?

Examples:

Input  : str = "1011100000100"
Output : 6
// Sub-strings present in str that can be make removed 
// 101{110000}0{100}. First sub-string 110000-->100-->null,
// length is = 6. Second sub-string 100-->null, length is = 3

Input  : str = "111011"
Output : 0
// There is no sub-string which can be make null

Ref: https://www.geeksforgeeks.org/length-longest-sub-string-can-make-removed/ 
'''

from ds.Stack import Stack

def removeLongestSubstring(s):
    stk = Stack()
    #stk.push(-1)
    maxLen = 0
    currLen = 0

    for i in range(len(s)-1, -1, -1):
        char = s[i]
        if char == '0':
            stk.push(char)
            if currLen > 0:
                currLen = 0
            continue

        # char == '1'
        # pop 2 0's for every 1.
        j = 0
        while not stk.isEmpty and j < 2:
            stk.pop()
            j += 1

        if j == 2:
            currLen += 3
        
        maxLen = max(currLen, maxLen)

    return maxLen

if __name__ == "__main__":
    #s = '1011100000100'
    s = '111011'
    print removeLongestSubstring(s)
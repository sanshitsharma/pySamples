#!/usr/bin/python

"""
Given a string consisting of opening and closing parenthesis, find length of the longest valid parenthesis substring.

Examples:

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()()

Input:  ()(()))))
Output: 6
Explanation:  ()(())
"""

"""
Solution:

Use a stack. Read the string from left to right.

if char is '(': push to stack
if char is ')': Try to pop from stack. 
                If a ')' is found on top, then increament curr_len
                else: compare curr_len to max_len and update

Time Complexity: O(n)
"""

from ds.Stack import Stack

def lvp(s):
    stk = Stack()
    max_len = 0
    curr_len = 0

    for c in s:
        if c == '(':
            stk.push(c)
        else: # c == ')'
            if stk.pop() is None:
                max_len = curr_len if curr_len > max_len else max_len
                curr_len = 0
            else:
                curr_len += 2

    return curr_len if curr_len > max_len else max_len

if __name__ == "__main__":
    string = '()(()))))'
    print "Longest valid parantheses length =", lvp(string)
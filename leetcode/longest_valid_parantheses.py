#!/usr/bin/env python

'''
Problem #32
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

Ref: https://leetcode.com/problems/longest-valid-parentheses/description/ 
'''

from ds.Stack import Stack

def lvp(s):
    if s is None:
        return 0

    stk = Stack()
    max_len = 0
    curr_len = 0

    for c in s:
        print "Evaluating char:", c
        if c == "(":
            stk.push(c)
            continue

        try:
            stk.pop()
            curr_len += 2
            print "TRY BLOCK: curr_len =", curr_len
        except Exception as e:
            max_len = max(max_len, curr_len)
            curr_len = 0
            print "Max Len =", max_len, "Curr Len =", curr_len

    print "Finally Max Len =", max_len, "Curr Len =", curr_len
    return max(max_len, curr_len)

if __name__ == "__main__":
    s = ")())()(())(()"
    #s = "()((((()"
    res = lvp(s) 
    print "Length of longest valid parantheses in", s, " =", res
#!/usr/bin/env python

'''
Given a balanced parentheses string S, compute the score of the string based on the following rule:

Case 1: () has score 1
Case 2: AB has score A + B, where A and B are balanced parentheses strings.
Case 3: (A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50

Ref: https://leetcode.com/problems/score-of-parentheses/description/
'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Initialize an empty stack
        stk = []

        # Check each character in the string
        i = 0
        while i < len(S):
            # If current character is an opening parantheses
            if S[i] == '(':
                # If the next char is a closing parantheses
                if S[i+1] == ')':
                    # If stack is empty or top element is not an integer, just push 1 to the stack
                    if not stk or not isinstance(stk[-1], int):
                        stk.append(1)
                    else: # If the top character is an integer then add 1 because this is a case where we found continuous pairs (Case 2)
                        stk[-1] += 1
                    i += 2 # Increment by two because we already processed the closing parantheses
                else: # If the next char is also an opening parantheses then add it to the stack
                    stk.append('(')
                    i += 1
            else: # S[i] == ')' # If the current char is a closing parantheses
                # Read the top of stack and multiply it by 2 as this is case 3
                temp = 2 * stk.pop()
                stk.pop() # Remove the corresponding opening parantheses
                # Add the count of any solitary pairs encountered before (Case 1's)
                while stk and stk[-1] != '(':
                    temp += stk.pop()
                stk.append(temp)
                i += 1

        # Finally return the top of stack
        return stk.pop()

if __name__ == "__main__":
    tests = ["()", "(())", "()()", "(()(()))", "((()))()()"]
    for test in tests:
        res = "Score of '" + test + "' = " + str(Solution().scoreOfParentheses(test))
        print res
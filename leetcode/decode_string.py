#!/usr/bin/python

'''
Problem #394
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Ref: https://leetcode.com/problems/decode-string/description/
'''

class Solution(object):
    def isEmpty(self, stk):
        return len(stk) == 0

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        k, strStk, numStk = 0, [], []

        for i in range(len(s)):
            if s[i].isdigit():
                k = k*10 + int(s[i])
            elif s[i] == '[':
                strStk.append('[')
                numStk.append(k)
                k = 0
            elif s[i].isalpha():
                strStk.append(s[i])
            else:
                tmp = ''
                while strStk and strStk[-1] != '[':
                    tmp = strStk.pop() + tmp 
                tmp = tmp * numStk.pop()
                strStk.pop()
                strStk.append(tmp)

        print "k =", k, "strStk =", strStk, "numStk =", numStk
        return ''.join(strStk)

if __name__ == "__main__":
    strs = ['3[a]2[bc]', '3[a2[c]]', '2[abc]3[cd]ef', 'd3[a2[bc]]', '11[leetcode]', "3[a]2[b4[F]c]", "st2[r]2[2[y]pq4[2[jk]e1[f]]]xyz"]
    #strs = ["3[a]2[b4[F]c]"]
    for s in strs:
        res = Solution().decodeString(s)
        out = "'" + s + "' --> " + "'" + res + "'"
        print out
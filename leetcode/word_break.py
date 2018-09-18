#!/usr/bin/python

'''
Problem #139:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Ref: https://leetcode.com/problems/word-break/description/
'''
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if not s or not wordDict:
            return False

        canMake = [False] * len(s)
        lastTrueIndx = -1

        if s[0] in wordDict:
            canMake[0] = True
            lastTrueIndx = 0

        for i in range(1, len(s)):
            target = s[:i+1]
            #print "target:", target, "canMake", canMake
            if target in wordDict:
                canMake[i] = True
                continue

            # We need to work backwords from the lastTrueIndx
            for j in range(i-1, -1, -1):
                if canMake[j] == False:
                    continue
                
                subStr = s[j+1:i+1]
                if subStr in wordDict:
                    canMake[i] = True
                    break

        print "canMake:", canMake
        return canMake[len(canMake)-1]

if __name__ == "__main__":
    s = 'catsanddog'
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    '''
    s = 'applepenapple'
    wordDict = ["apple", "pen"]
    '''

    '''
    s = 'leetcode'
    wordDict = ["leet", "code"]

    s = "abcd"
    wordDict = ["a","abc","b","cd"]
    '''

    print Solution().wordBreak(s, wordDict)
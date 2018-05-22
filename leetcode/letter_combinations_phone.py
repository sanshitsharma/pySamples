#!/usr/bin/python

'''
Problem #17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given. Note that 1 & 0 do not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Ref: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''
from datetime import datetime

class Solution(object):
    """
    :type digits: str
    :rtype: List[str]
    """
    def __init__(self):
        self.dMap = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4':'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def _letterCombinations(self, pNum, dIndx, s, results):
        if len(s) == len(pNum):
            results.append(''.join(s))
            return

        for i in  range(len(self.dMap[pNum[dIndx]])):
            s.append(self.dMap[pNum[dIndx]][i])
            self._letterCombinations(pNum, dIndx + 1, s, results)
            s.pop()

    def letterCombinations(self, digits):
        if digits == "":
            return []

        combination = []
        results = []
        self._letterCombinations(digits, 0, combination, results)
        return results

if __name__ == "__main__":
    pNum = '23'
    sol = Solution()
    start_time = datetime.now()
    print sol.letterCombinations(pNum)
    print "Time to complete:", (datetime.now() - start_time).microseconds, "microsecs"
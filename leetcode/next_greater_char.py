#!/usr/bin/python

'''
744. Find Smallest Letter Greater Than Target

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than
the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Ref: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/ 
'''

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if not letters or not target:
            return None

        lo = 0
        hi = len(letters) - 1

        return self.nextGreatestUtil(letters, target, lo, hi)

    def nextGreatestUtil(self, letters, target, lo, hi):
        if lo <= hi:
            mid = (lo+hi)/2
            if letters[mid] == target:
                while mid < len(letters) - 1 and letters[mid+1] == target:
                    mid += 1
                return letters[(mid+1)%len(letters)]
            elif target < letters[mid]:
                if (mid > lo and letters[mid-1] < target) or mid == lo:
                    return letters[mid]
                else:
                    return self.nextGreatestUtil(letters, target, lo, mid-1)
            else:
                if (mid < hi and letters[mid+1] > target) or mid == hi:
                    return letters[(mid+1)%len(letters)]
                else:
                    return self.nextGreatestUtil(letters, target, mid+1, hi)

        return None

if __name__ == "__main__":
    input = [{"letters" : ["c", "f", "j"], "target" : "a"}, {"letters" : ["c", "f", "j"], "target" : "c"}, {"letters" : ["c", "f", "j"], "target" : "d"}, {"letters" : ["c", "f", "j"], "target" : "g"},  {"letters" : ["c", "f", "j"], "target" : "j"},  {"letters" : ["c", "f", "j"], "target" : "k"}, {"letters": ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "target": "e"}]
    for inp in input:
        print "Letters:", inp["letters"], "Target:", inp["target"], "Next Greatest:", Solution().nextGreatestLetter(inp["letters"], inp["target"])
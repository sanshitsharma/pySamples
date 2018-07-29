#!/usr/bin/python

'''
Problem #763
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at
most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.

Ref: https://leetcode.com/problems/partition-labels/description/
'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        # Create a map which tracks the last occurence of the last index of every character
        last = {c : i for i, c in enumerate(S)}

        j = 0
        anchor = 0
        ans = []

        # For every character, if the last occurance of this character is before the
        # current value of j, then we don't do anything
        # else we updated the value of j to the last occurance of the character
        for i, c in enumerate(S):
            j = max(j, last[c])

            # If the current character index is also the furthest we have calculated so far
            # it means that all chaacters from anchor to this spot are in this range, therefore
            # we found a partition
            if i == j:
                ans.append(i - anchor + 1)
                #ans.append(S[anchor:i+1])
                anchor = i + 1

        return ans

if __name__ == "__main__":
    s = 'ababcbacadefegdehijhklij'
    ans = Solution().partitionLabels(s)
    print ans
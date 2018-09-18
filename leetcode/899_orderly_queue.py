#!/usr/bin/python

'''
A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

 

Example 1:

Input: S = "cba", K = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character ("c") to the end, obtaining the string "bac".
In the second move, we move the 1st character ("b") to the end, obtaining the final result "acb".
Example 2:

Input: S = "baaca", K = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character ("b") to the end, obtaining the string "aacab".
In the second move, we move the 3rd character ("c") to the end, obtaining the final result "aaabc".
 

Note:

1 <= K <= S.length <= 1000
S consists of lowercase letters only.

Ref: https://leetcode.com/problems/orderly-queue/description/
'''

class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        # Track all strings that have been seen
        # On every move, move the largest character in the S[0:K] to the end
        # Check if the resulting string is smaller than the current smallest and replace
        currSmallest = S
        seen = set()
        isRepeated = False

        while not isRepeated:
            if S in seen:
                isRepeated = True
                break

            seen.add(S)
            lCI = self.getLargestCharIndx(S[:K])
            print "S =", S, "lCI =", lCI
            S = self.moveLargestToEnd(S, lCI)
            print "After Move:", S
            currSmallest = min(S, currSmallest)

        return currSmallest

    def getLargestCharIndx(self, s):
        largestChar = s[0]
        indx = 0
        for i in range(1, len(s)):
            if largestChar < s[i]:
                largestChar = s[i]
                indx = i

        return indx

    def moveLargestToEnd(self, S, indx):
        s = list(S)
        temp = s[indx]
        i = indx
        while i < len(s) - 1:
            s[i] = s[i+1]
            i += 1
        s[i] = temp

        return ''.join(s)

if __name__ == "__main__":
    S = 'gxzv'
    print Solution().orderlyQueue(S, 4)
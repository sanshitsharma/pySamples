#!/usr/bin/env python

'''
Problem 869: Reordered power of 2

Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit
is not zero. Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:
Input: 1
Output: true

Example 2:
Input: 10
Output: false

Example 3:
Input: 16
Output: true

Example 4:
Input: 24
Output: false

Example 5:
Input: 46
Output: true
 

Note:
1 <= N <= 10^9

Ref: https://leetcode.com/problems/reordered-power-of-2/description/
'''

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # Convert to list in order to generate permutations
        lst = list(str(N))
        start = 0
        found = [False]
        return self._permute(lst, start, found)

    def _permute(self, l, indx, found):
        if indx == len(l) - 1 and l[0] != '0':
            #num = int(''.join(l))
            #print "Got permutation:", l, "num =", num, "ans =", (num & (num-1))
            #return (num & (num-1)) == 0
            return bin(int(''.join(l))).count('1') == 1

        for j in range(indx, len(l)):
            l[indx], l[j] = l[j], l[indx]
            if self._permute(l, indx+1, found):
                found[0] = True
                #print "Found:", found[0]
                break
            l[indx], l[j] = l[j], l[indx]

        return found[0]

if __name__ == "__main__":
    print Solution().reorderedPowerOf2(368407186)
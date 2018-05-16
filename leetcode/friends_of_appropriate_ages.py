#!/usr/bin/python

'''
Problem 825: Friends of appropriate ages

Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

Ref: https://leetcode.com/problems/friends-of-appropriate-ages/description/
'''

from pyCollections import binarySearch, binSearchRecurse

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121

        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA < ageB:
                    continue
                if 0.5*ageA + 7 >= ageB:
                    continue
                if ageA < 100 < ageB:
                    continue
                
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA

        return ans

if __name__ == "__main__":
    #a = [16, 16, 17, 18]
    a = [63,74,40,26,93,1,110,39,65,108,74,110,53,13,92,89,45,63,53,29,28,60,48,45,38,67,20,106,6,23,12,61,65,25,75,73,101,11,39,48,38,1,120,58,62,29,33,21,36,26,59,11,71,106,87,59,46,89,57,29,100,84,108,91,67,32,12,33,94,113,48,28,60,64,14,29,56,13,10,82,2,27,45,53,45,100,73,38,99,18,67,54,44,7,93,79,96,52,70,33]
    a.sort()
    print a
    print Solution().numFriendRequests(a)

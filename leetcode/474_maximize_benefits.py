#!/usr/bin/env python

'''
474. Ones and Zeroes

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings
consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10", "0001", "1", "0"

Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create an array which will keep track of the max benefits at every indx 'i'. 
        # The array is initialized with 0 because we don't know whether the string can
        # be created wihout any prior consumption (from default values of 0's and 1's)
        maxBenefits = [0 for x in strs]

        # Create another array which will track the number of 0's and 1's left after 
        # the string at index 'i' has been created. For now simply initialize the array
        # with starting values of m & n
        rem = [(m,n) for x in strs]

        for i in range(len(strs)):
            # If you can't create the str with the default number of 0's and 1's, then
            # no point in checking ahead
            if not self.canCreate(strs[i], m, n):
                continue

            # First populate the maxBenefits and rem if the string is created from starting
            # values of m & n
            maxBenefits[i] = 1
            costI = self.createCost(strs[i], m, n)
            rem[i] = (m-costI[0], n-costI[1])

            for j in range(i):
                # Check if strs[i] can be created after any of the prev strings from 0..i-1
                # can be created and thereby maximize the benefits
                if maxBenefits[j] > 0 and self.canCreate(strs[i], rem[j][0], rem[j][1]) and maxBenefits[i] < maxBenefits[j] + 1:
                    maxBenefits[i] = maxBenefits[j] + 1
                    rem[i] = (rem[j][0] - costI[0], rem[j][1] - costI[1])

        print "String:", strs
        print "Max benefits:", maxBenefits
        print "Remainder:", rem

        return max(maxBenefits)

    def canCreate(self, string, zeros, ones):
        return string.count('0') <= zeros and string.count('1') <= ones

    def createCost(self, string, zeros, ones):
        #return [zeros - string.count('0'), ones - string.count('1')]
        return [string.count('0'), string.count('1')]

if __name__ == "__main__":
    '''
    A = ['10', '0001', '111001', '1', '0']
    m = 5
    n = 3
    '''

    '''
    A = ["10", "0", "1"]
    m = 1
    n = 1
    '''

    '''
    A = ["10","0001","111001","1","0"]
    m = 4
    n = 3
    '''

    A = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
    m = 9
    n = 80

    print Solution().findMaxForm(A, m, n)
#!/usr/bin/python

'''
Problem #616
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist
in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped
by bold tags are consecutive, you need to combine them.

Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].

Ref: https://leetcode.com/problems/add-bold-tag-in-string/description/
'''

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        if s is None or s == "":
            return ""

        sStrRanges = []
        for val in dict:
            try:
                indx = s.index(val)
                sStrRanges.append([indx, indx+len(val)-1])
            except ValueError as ve:
                print val, "is not a substring of", s

        # Return the string as is, if no words from dict were found to be substring of s
        if len(sStrRanges) == 0:
            return s

        # Sort the ranges in ascending order
        sStrRanges.sort()

        combRanges = [sStrRanges[0]]
        for i in range(1, len(sStrRanges)):
            r = sStrRanges[i]
            l = combRanges[len(combRanges)-1]

            if l[1] >= r[0] or l[1] == r[0]-1:
                combRanges.pop()
                combRanges.append([min(l[0], r[0]), max(l[1], r[1])])
            else:
                combRanges.append(r)


        #print "Combined Ranges:", combRanges

        # Create the results with the bold tags added
        sIndx = 0
        res = []
        for interval in combRanges:
            if interval[0] > sIndx:
                for i in range(sIndx, interval[0]):
                    res.append(s[i])
            
            res.append('<b>')
            for i in range(interval[0], interval[1]+1):
                res.append(s[i])
            res.append('</b>')

            sIndx = interval[1] + 1

        # Add all remaining characters from string
        for i in range(sIndx, len(s)):
            res.append(s[i])

        return ''.join(res)

if __name__ == "__main__":
    s = 'abcxyz123'
    dict = {'abc', '123'}

    #s = "aaabbcc"
    #dict = ["aaa","aab","bc"]
    res = Solution().addBoldTag(s, dict)
    print res
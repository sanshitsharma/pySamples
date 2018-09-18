#!/usr/bin/env python

'''
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index,
otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where
ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return
2147483647.

Example 1:
Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

class ArrReader(object):
    def __init__(self, arr):
        self.__items = list(arr)

    def get(self, k):
        if k > len(self.__items) - 1:
            return 2147483647
        return self.__items[k]

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # First figure out the range of indexes in which the target can exist
        start = 0
        end = 0
        rangeFound = False
        
        if reader.get(start) > target:
            return -1

        while not rangeFound:
            val = reader.get(end)
            if val == target:
                #print "Index =", end
                return end
            elif val > target:
                # If the val is 2147483647 then we exceeded the array bounds. We need to do a partial linear search 
                # starting at end/2 to find the last index
                if val == 2147483647:
                    temp = end/2
                    while reader.get(temp) != 2147483647:
                        temp += 1
                    end = temp - 1
                rangeFound = True
                break
            else:
                start = end
                if end == 0:
                    end += 1
                else:
                    end *= 2
        
        if not rangeFound:
            print "Elem does not exist"
            return -1
        
        #print "Start:", start, "end:", end
        # Now use the start and end range to perform a modified binary search
        return self.searchUtil(reader, start, end, target)

    def searchUtil(self, reader, s, e, target):
        if e < s:
            return -1
        mid = (s + e)/2
        val = reader.get(mid)
        if val == target:
            return mid
        elif val < target:
            return self.searchUtil(reader, mid+1, e, target)
        else:
            return self.searchUtil(reader, s, mid-1, target)

if __name__ == "__main__":
    reader = ArrReader([-1,0,3,5,9,12])
    target = 12
    print Solution().search(reader, target)
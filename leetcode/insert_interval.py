#!/usr/bin/python

'''
Problem #57
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Ref: https://leetcode.com/problems/insert-interval/description/
'''

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[%s, %s]' % (self.start, self.end)

class Solution(object):
    def compare(self, a, b):
        if b.end < a.start:
            # a is bigger
            return 1
        elif b.start > a.end:
            # a is smaller
            return -1
        else:
            return 0
    
    def getOverlappedInterval(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == [] and newInterval == None:
            return []
        
        if intervals == []:
            return [newInterval]

        if newInterval == None:
            return intervals
        
        res = []
        n = newInterval
        l = len(intervals)

        for i in range(l):
            interval = intervals[i]
            comp = self.compare(n ,interval)

            if comp == -1:
                # interval is bigger than n
                res.append(n)
                n = None
                break
            elif comp == 1:
                # n is bigger than interval
                res.append(interval)
            else:
                n = self.getOverlappedInterval(interval, n)

        if n is not None:
            print "n is not none"
            res.append(n)
        elif i != l:
            for j in range(i, l):
                res.append(intervals[j])

        return res

if __name__ == "__main__":
    ###### Corner cases ######
    #intervals = []
    #newInterval = Interval(5,7)

    #intervals = [Interval(5,7)]
    #newInterval = None

    #intervals = []
    #newInterval = None
    ##########################

    ##### Overlap cases ######
    #intervals = [Interval(1, 3), Interval(6, 9)]
    #newInterval = Interval(2, 5)

    intervals = [Interval(1,2), Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
    newInterval = Interval(4,8)
    ##########################

    #### No Overlap cases ####
    #intervals = [Interval(1,5)]
    #newInterval = Interval(0,0)

    #intervals = [Interval(1,5)]
    #newInterval = Interval(6,8)

    #intervals = [Interval(3,5), Interval(12,15)]
    #newInterval = Interval(6,6)
    ##########################

    res = Solution().insert(intervals, newInterval)
    print res
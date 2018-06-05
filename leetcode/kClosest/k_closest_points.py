#!/usr/bin/python

'''
Given millions of points in a file, find the k closest points to origin
'''

import math

class Solution(object):
    def kClosestPoints(self, file, k):
        dists = [(0, '')] * 2 * k
        #print dists

        offset = 0
        hasMoreData = True

        while hasMoreData:
            if offset == 0:
                hasMoreData, offset = self.loadData(file, 0, 2*k, dists, 0, len(dists)-1)
            else:
                hasMoreData, offset = self.loadData(file, offset, k, dists, k, len(dists)-1)

            #print "Dists:", dists, "hasMoreData:", hasMoreData, "offset:", offset

            self.findKthSmallest(dists, k)
            #print "After quickselect:", dists

        return dists[:k]
        '''
        ans = []
        for i in range(k):
            ans.append("(" + dists[i][1] + ")")
        return ans
        '''
        

    def findKthSmallest(self, dists, k):
        #print "find smallest: dists -->", dists, "k:", k 
        return self.quickSelect(dists, 0, len(dists)-1, k-1)

    def quickSelect(self, dists, l, h, k):
        if l > h:
            return

        pivotIndx = self.partition(dists, l, h, k)
        if k == pivotIndx:
            return
        elif k < pivotIndx:
            return self.quickSelect(dists, l, pivotIndx-1, k)
        else:
            return self.quickSelect(dists, pivotIndx+1, h, k)

    def partition(self, arr, l, h, k):
        arr[l], arr[k] = arr[k], arr[l]
        
        #print "partitioning.. l =", l, "h =", h, "k =", k, "arr:", arr
        while l < h:
            while l <= h and arr[l][0] <= arr[k][0]:
                #print "l:", l, "h:", h, "arr[l]:", arr[l][0], "arr[pI]:", arr[pivotIndx][0]
                l += 1

            while h >= l and arr[h][0] >= arr[k][0]:
                #print "h:", h, "l:", l, "arr[h]:", arr[h][0], "arr[pI]:", arr[pivotIndx][0]
                h -= 1

            #print "\tPointers set.. l:", l, "h:", h
            if l < h:
                arr[l], arr[h] = arr[h], arr[l]
                #print "\tTransient: l:", l, "h:", h, "arr:", arr

        arr[k], arr[h] = arr[h], arr[k]
        #print "Post partitioning.. h:", h, "arr:", arr
        return h
        
    def loadData(self, file, offset, k, dists, s, e):
        try:
            f = open(file, 'r')
            f.seek(offset)
            while s <= e:
                point = f.readline().strip('() \n')
                if point == '':
                    break
                x, y = point.split(',')
                dists[s] = (self.getDist(float(x), float(y)), point)
                s += 1

            newOffset = f.tell()
            f.close()

            if s >= e:
                return True, newOffset
            
            return False, newOffset
        except Exception as e:
            raise ValueError("cannot open file:", e)

    def getDist(self, x, y, a=0.00, b=0.00):
        return math.sqrt(pow(x-a, 2)+pow(y-b, 2))


if __name__ == "__main__":
    file = 'data.txt'
    k = 3
    print Solution().kClosestPoints(file, k)
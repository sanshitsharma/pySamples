#!/usr/bin/env python

'''
Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.

Example :

Input :  arr[] = [1, 2, 3, 4, 5, 6, 7]
         d = 2
Output : arr[] = [3, 4, 5, 6, 7, 1, 2] 

Ref: https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/
'''

class Solution(object):
    def rotateArray(self, arr, numElems):
        if numElems < 0:
            print "invalid rotation count"
        
        aLen = len(arr)
        d = numElems%aLen

        if d == 0:
            print "No need to rotate"
            return arr

        # First reverse from index 0..d-1
        l = 0
        r = d-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        # Next reverse from index d..l-1
        l = d
        r = aLen-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        # Lastly, reverse the entire array
        l = 0
        r = aLen-1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        return arr

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    Ar = Solution().rotateArray(A, 1)
    print Ar
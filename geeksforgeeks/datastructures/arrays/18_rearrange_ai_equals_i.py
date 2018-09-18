#!/usr/bin/env python

'''
Rearrange an array such that arr[i] = i
Given an array of elements of length N, ranging from 1 to N. All elements may not be present in the array. If element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

Examples:

Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
              11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
         11, 12, 13, 14, 15, 16, 17, 18, 19]

Ref: https://www.geeksforgeeks.org/rearrange-array-arri/
'''

class Solution(object):
    def rearrange(self, A):
        if not A:
            return None

        for indx in range(len(A)):
            while A[indx] != -1 and A[indx] != indx:
                # Swap 
                tempI = A[indx]
                A[indx], A[tempI] = A[tempI], A[indx]
        return A

if __name__ == "__main__":
    A = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    print Solution().rearrange(A)

    A = [19, 7, 0, 3, 18, 15, 12, 6, 1, 8, 11, 10, 9, 5, 13, 16, 2, 14, 17, 4]
    print Solution().rearrange(A)
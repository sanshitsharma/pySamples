#!/usr/bin/env python

def getMedian(A, B):
    if not A or not B:
        return 0

    if len(A) != len(B):
        print "Does not work for arrays with diff length"
        return None

    if len(A) == 1:
        return float(A[0] + B[0])/2

    return getMedianUtil(A, B, 0, len(A)-1, 0, len(B)-1)

def getMedianUtil(A, B, alo, ahi, blo, bhi):
    if ahi - alo == 1:
        return float(max(A[alo], B[blo]) + min(A[ahi], B[bhi]))/2

    aMI = (alo + ahi)/2
    bMI = (blo + bhi)/2

    if A[aMI] == B[bMI]:
        return A[aMI]
    elif A[aMI] < B[bMI]:
        return getMedianUtil(A, B, aMI, ahi, blo, bMI)
    else:
        return getMedianUtil(A, B, alo, aMI, bMI, bhi)

if __name__ == "__main__":
    A = [1, 12, 15, 26, 38]
    B = [2, 13, 17, 30, 45]

    A = [1]
    B = [2]

    print getMedian(A, B)
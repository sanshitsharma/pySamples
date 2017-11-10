#!/usr/bin/python

def FindLargestSumSubarray(lst):
    nCurSum = 0
    nLargestSum = 0

    startIdx = 0
    endIdx = 0

    for num in lst:
        if nCurSum <= 0:
            nCurSum = num
            startIdx = lst.index(num)
            endIdx = lst.index(num)
        else:
            nCurSum = nCurSum + num
            endIdx = lst.index(num)

        if nCurSum > nLargestSum:
            nLargestSum = nCurSum

    print lst[startIdx:endIdx]
    return nLargestSum

def main():
    #array = [1, -2, 3, 10, -4, 7, 2, -5]
    array = [-1, 2, -3, -10, 4, 7, 2, -5]
    print FindLargestSumSubarray(array)

if __name__ == "__main__":
    main()

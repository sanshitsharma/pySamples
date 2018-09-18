#!/usr/bin/env python

def maxUtilization(cap, fore, back):
    currMaxUtil = 0
    ans = []
    for fItem in fore:
        for bItem in back:
            util = fItem[1] + bItem[1]
            if util <= cap:
                if util == currMaxUtil:
                    ans.append([fItem[0], bItem[0]])
                elif util > currMaxUtil:
                    currMaxUtil = util
                    ans = [[fItem[0], bItem[0]]]

    return ans

def newMax(cap, f, b):
    # First sort all foreground process using utilization as key
    fSorted = sorted(f, key = lambda f: f[1])
    
    # Next sort all background process using utilization as key
    bSorted = sorted(b, key = lambda b: b[1])

    currMaxUtil = 0
    ans = []

    # Start a left pointer at index 0 of foreground sorted
    l = 0

    # Start a right at last element of background sorted
    r = len(bSorted) - 1

    # Move through all the processes
    while l < len(fSorted) and r >= 0:
        util = fSorted[l][1] + bSorted[r][1]
        proc = [fSorted[l][0], bSorted[r][0]]

        if util <= cap:
            if util == currMaxUtil:
                ans.append(proc)
            elif util > currMaxUtil:
                currMaxUtil = util
                ans = [proc] 

            k = r - 1
            while fSorted[l][1] + bSorted[k][1] == currMaxUtil:
                ans.append([fSorted[l][0], bSorted[k][0]])
                k -= 1

            #print ans 
            #r += 1
            l += 1
        else:
            r -= 1

    return ans

if __name__ == "__main__":
    cap = 10
    f = [[1,3], [2,5], [3,7], [4,10]]
    b = [[1,2], [2,3], [3,4],[4,5]]

    #cap = 10
    #f = [[1,1], [2,3], [3,4], [4,7]]
    #b = [[1,2], [2,4], [3,6], [4,8]]
    print newMax(cap, f, b)
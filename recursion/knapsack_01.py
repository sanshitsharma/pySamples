#!/usr/bin/python

'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this
subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don't pick it (0-1 property).

0-1 Knapsack Problem
v = [60, 100, 120]
w = [10, 20, 30]
W = 50

Solution: 220
'''

#count = 0

def solve(v, w, V, W, idx):
    #global count
    #count += 1
    if W == 0 or idx < 0:
        return V

    # If the wait of current item is greater then kanpsack capacity,
    # then this item cannot be included in the solution
    if w[idx] > W:
        return solve(v, w, V, W, idx-1)

    return max(solve(v, w, V + v[idx], W - w[idx], idx - 1), solve(v, w, V, W, idx - 1))

def getMaxValue(v, w, W):
    V = 0
    idx = len(w) - 1

    return solve(v, w, V, W, idx)

if __name__ == "__main__":
    v = [60, 100, 120]
    w = [10, 20, 30]
    W = 50

    res = getMaxValue(v, w, W)
    #print "Call Count =", count
    print res
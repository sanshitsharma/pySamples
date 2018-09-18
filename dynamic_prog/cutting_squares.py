#!/usr/bin/python

import math

def canCut(h, w, edge):
    return (h >= edge and w >= edge)

def squaresUtil(h, w):
    if h <= 0 or w <= 0:
        return

    area = h * w
    pLE = int(math.floor(math.sqrt(area)))
    while not canCut(h, w, pLE):
        pLE -= 1

    count = area/(pLE*pLE)
    squaresUtil.total += count

    print "Cut", count, "squares of edge length =", pLE
    if h == pLE:
        w -= (pLE * count)
    else:
        h -= (pLE * count)

    squaresUtil(h, w)
    return

def minCutSquares(height, width):
    squaresUtil.total = 0
    squaresUtil(height, width)
    return squaresUtil.total

if __name__ == "__main__":
    h = 13
    w = 29

    res = minCutSquares(h, w)
    print "Min squares that can be cut =", res
#!/usr/bin/env python

import numpy as np 

def deletion_dist(A, B):
    nr = len(A) + 1
    nc = len(B) + 1

    DT = np.zeros([nr, nc], dtype=int)

    for r in range(nr):
        for c in range(nc):
            if r == 0:
                DT[r][c] = c
            elif c == 0:
                DT[r][c] = r
            elif A[r-1] == B[c-1]:
                DT[r][c] = DT[r-1][c-1]
            else:
                DT[r][c] = 1 + min(DT[r-1][c], DT[r][c-1])

    #print DT
    return DT[nr-1][nc-1]

if __name__ == "__main__":
    tests = [['boat', 'got'], ['abcd', 'xdyza'], ['geek', 'gesek'], ['abcd', 'xayzd'], ['abc', 'acb']]
    for test in tests:
        print "Deletion distance b/w", test[0], "&", test[1], "=", deletion_dist(test[0], test[1])
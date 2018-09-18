#!/usr/bin/env python

import math 

def nearestXsteakHouses(totalSteakhouses, allocations, numSteakhouses):
    distanceCoordMap = {}

    # Calculate the dist of every steak house from origin
    for coord in allocations:
        d = math.sqrt(coord[0]*coord[0] + coord[1]*coord[1])
        try:
            distanceCoordMap[d].append(coord)
        except:
            distanceCoordMap[d] = [coord]

    dists = distanceCoordMap.keys()
    dists.sort()

    ans = []
    for dist in dists:
        coords = distanceCoordMap[dist]
        if len(ans) < numSteakhouses:
            ans = ans + coords
        else:
            # Select the remaining elements
            ans = ans + coords[:numSteakhouses-len(ans)]

        if len(ans) == numSteakhouses:
            break

    return ans

if __name__ == "__main__":
    t = 3
    a = [[1, 2], [3, 4], [1, -1], [-1, 1]]
    n = 2

    print nearestXsteakHouses(t, a, n)
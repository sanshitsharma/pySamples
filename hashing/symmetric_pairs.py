#/usr/bin/python

"""
Given an array of pairs, find all symmetric pairs in it
Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d. For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.

It may be assumed that first elements of all pairs are distinct.

Example:

Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
Output: Following pairs have symmetric pairs
        (30, 40)
        (5, 10)  
"""

from collections import defaultdict

def find_symmetric_pairs(lst):
    map = defaultdict()
    res = []

    # Init the key, values pairs
    map[0] = []
    map[1] = []

    for pair in reversed(lst):
        if pair[0] in map[1] and pair[1] in map[0]:
            res.append(pair)

        map[0].append(pair[0])
        map[1].append(pair[1])

    return res

if __name__ == "__main__":
    lst = [(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]
    res = find_symmetric_pairs(lst)
    print res
#!/usr/bin/python

'''
Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d
are distinct elements. If there are multiple answers, then print any of them.

Example:

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:   {3, 4, 7, 1, 12, 9};
Output:  (4, 12) and (7, 9)
Explanation: 4+12 = 7+9

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found

Ref: https://www.geeksforgeeks.org/find-four-elements-a-b-c-and-d-in-an-array-such-that-ab-cd/ 
'''

def get_equal_sum_pairs(a):
    sum_map = {}
    res = []
    for i in range(len(a)-1):
        for j in range(i, len(a)):
            s = a[i] + a[j]
            if s in sum_map.keys():
                found_pairs = sum_map[s]
                for pair in found_pairs:
                    res.append((pair, (a[i], a[j])))
                sum_map[s].append((a[i], a[j]))
            else:
                sum_map[s] = [(a[i], a[j])]

    return res

if __name__ == "__main__":
    res = get_equal_sum_pairs([3, 4, 7, 1, 2, 9, 8])
    for pairs in res:
        string = '{' + str(pairs[0]) + ', ' + str(pairs[1]) + '}'
        print string
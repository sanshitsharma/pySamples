#!/usr/bin/python

from collections import OrderedDict

def kth_non_repeating(string, k):
    d = OrderedDict()

    for c in string:
        if not d.has_key(c):
            d[c] = 1
        else:
            d[c] = d[c] + 1

    for key, val in d.iteritems():
        if val == 1:
            k = k - 1

        if k == 0:
            return key

    return None

if __name__ == "__main__":
    print kth_non_repeating('geeksforgeeks', 3)
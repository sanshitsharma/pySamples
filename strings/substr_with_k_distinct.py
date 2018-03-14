#!/usr/bin/python

def add_to_dict(d, k):
    if d.has_key(k):
        d[k] = d[k] + 1
    else:
        d[k] = 1

    return d

def substrs_with_k_distinct(string, k):
    substrs = []
    count = 0
    for i in range(0, len(string)):
        dist_count = 0
        d = {}
        for j in range(i, len(string)):
            if not d.has_key(string[j]):
                dist_count = dist_count + 1
                
            d = add_to_dict(d, string[j])
            substr = string[i: j+1]
            #print "substr:", substr, " dist_count =", dist_count
            if dist_count == k:
                count = count + 1
                substrs.append(substr)

    return substrs

def all_substrings(string):
    return [string[i:j+1] for i in range(len(string)) for j in range(i,len(string))]

if __name__ == "__main__":
    string = 'abcbaa'
    k = 3

    substrs = substrs_with_k_distinct(string, k)
    res = "'" + string + "' has '" + str(len(substrs)) + "' substrings with '" + str(k) + "' distinct characters"
    print res
    print substrs
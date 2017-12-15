#!/usr/bin/python

import sys

def areAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    d = dict()
    for ch in str1:
        try:
            d[ch] += 1
        except:
            d[ch] = 1

    for ch in str2:
        try:
            count = d[ch]
        except:
            print "char", ch, "not found in", str1
            return False
        else:
            d[ch] = count - 1
 
    for key, value in d.iteritems():
        if value != 0:
            res = "char '" + key + "' count doesn't match"
            print res
            return False

    return True

def main():
    print "Welcome to anagram checker"
    if len(sys.argv) != 3:
        print "invalid args"
        sys.exit()

    if areAnagrams(sys.argv[1], sys.argv[2]):
        res = "'" + sys.argv[1] + "' & '" + sys.argv[2] + "' are anagrams"
        print res 

if __name__ == "__main__":
    main()

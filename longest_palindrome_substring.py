#!/usr/bin/python

import argparse

def usage():
	print 'usage: ' + os.path.basename(sys.argv[0]) + ' [-h] -in INSTRING'

def longest_palindrome_substring(str):
    lps = ''
    for indx in range(0, len(str)):
        temp_lps = str[indx]
        left = indx - 1
        right = indx + 1

        while left >= 0 and right <= len(str) - 1:
            if str[left] == str[right]:
                temp_lps = str[left:right+1]
                left -= 1
                right += 1
            elif str[left] == str[indx]:
                temp_lps = str[left:indx+1]
                left -= 1
            elif str[indx] == str[right]:
                temp_lps = str[indx:right+1]
                right += 1
            else:
                break

            if len(temp_lps) > len(lps):
                lps = temp_lps

    return lps

def main():
    print "Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000."
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--instring', nargs=1, help='String in which longest palindrome is to be found', required='true')

    args = parser.parse_args()

    # Parse the input file argument
    if args.instring[0] == "":
        print "error: argument -in/--instring expects a valid string"
        usage()
        sys.exit(1)
    str = args.instring[0]

    lps = longest_palindrome_substring(str)
    print "Longest Palindrome Substring in '" + str + "' --> '" + lps + "'"

if __name__ == "__main__":
    main()
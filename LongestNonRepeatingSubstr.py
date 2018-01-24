#!/usr/bin/python

import argparse

class LongestNonRepeatingSubstr():
    def __init__(self):
        self.__d = {}
        self.__longest_substr = ''

    def find(self, test_str):
        curr_str = ''
        for char in test_str:
            if self.__d.has_key(char):
                if len(curr_str) > len(self.__longest_substr):
                    self.__longest_substr = curr_str                
                self.__d.clear()
                curr_str = ''

            curr_str += char
            self.__d[char] = 1

        return self.__longest_substr

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ts", "--test_str", nargs=1, help="Input string", type=str)

    args = parser.parse_args()
    if args.test_str is not None:
        test = args.test_str[0]
    else:
        test = raw_input('Enter a string to test: ')

    print "Longest non-repeating sub string in '" + test + "': '" + LongestNonRepeatingSubstr().find(test) + "'"

if __name__ == "__main__":
    main()
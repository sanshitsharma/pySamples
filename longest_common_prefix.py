#!/usr/bin/python

def longest_common_prefix(str1, str2):
    prefix = ''

    parse_len = len(str1) if len(str1) < len(str2) else len(str2)
    i = 0

    while i < parse_len:
        if str1[i] != str2[i]:
            break
        prefix += str1[i]
        i += 1
    return prefix

def main():
    print "Given strings, find the longest common prefix"
    print longest_common_prefix('aewfds', 'ae')

if __name__ == "__main__":
    main()

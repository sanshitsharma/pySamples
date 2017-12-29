#!/usr/bin/python

# A number is called ugly if it's only prime factors are 2,3 or 5. Generally 1 is considered an ugly number

import sys

def isUglyNumber(num):
    while num%2 == 0:
        num = num/2

    while num%3 == 0:
        num = num/3

    while num%5 == 0:
        num = num/5

    return num == 1

def main():
    if len(sys.argv) != 2:
        print "invalid input"
        sys.exit()

    try:
        num = int(sys.argv[1])
    except ValueError:
        print "'" + sys.argv[1] + "' is not a numeric string"
        sys.exit()

    print "Is '" + sys.argv[1] + "' an ugly number? " + str(isUglyNumber(num))

if __name__ == "__main__":
    main()

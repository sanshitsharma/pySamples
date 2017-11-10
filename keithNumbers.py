#!/usr/bin/python

import argparse

def sum_and_digits(num):
    digits = []
    nsum = 0

    while num != 0:
        digit = num%10
        digits.append(digit)
        nsum += digit

        num = num/10

    digits.reverse()
    return nsum, digits

def isKeithNumber(num):
    if num < 10:
        return True

    n = len(str(num))

    if n == 1:
        return num

    newNum, digits = sum_and_digits(num)

    while newNum < num:
        newNum = sumDigits(digits)
        if newNum == num:
            return True
        else:
            digits.append(newNum)
            del digits[0]

    return False    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("num", nargs=1, help="Number to test for Keith Numberness", type=int)

    args = parser.parse_args()
 
    print args.num[0], "is a keith number:", isKeithNumber(args.num[0])

if __name__ == "__main__":
    main()

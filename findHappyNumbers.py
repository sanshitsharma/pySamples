#!/usr/bin/python

import argparse

def digitSum( num ):
    sum = 0
    while num != 0:
        digit = num%10
        sum += digit*digit
        num = num/10

    return sum

def happyNumbers( low, high ):
    is_repeated = False
    lst = []

    happyNums = []

    for i in range(low, high+1):
        nextNum = i
        is_repeated = False
        while not is_repeated:
            nextNum = digitSum(nextNum)
            if nextNum == 1:
                is_repeated = True
                happyNums.append(i)
            elif nextNum in lst:
                is_repeated = True
            else:
                lst.append(nextNum)

    return happyNums

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument('-ln', '--lnum', nargs=1, help="From Number", type=int, default='1')
        parser.add_argument('-hn', '--hnum', nargs=1, help="To Number", type=int, default='100')

        args = parser.parse_args()

        if isinstance(args.lnum, list):
            lownum = args.lnum[0]
        else:
            lownum = args.lnum

        if isinstance(args.hnum, list):
            highnum = args.hnum[0]
        else:
            highnum = args.hnum

        print (happyNumbers( lownum, highnum ))

if __name__ == "__main__":
    main()

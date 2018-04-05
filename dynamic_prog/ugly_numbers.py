#!/usr/bin/python

"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... 
shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n'th Ugly number.

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
"""
import sys

def is_ugly_number(num):
    while num%2 == 0:
        num = num/2

    while num%3 == 0:
        num = num/3

    while num%5 == 0:
        num = num/5

    return num == 1

def find_nth_ugly_number(n):
    i = 1
    count = 1

    while n > count:
        i += 1
        if is_ugly_number(i):
            count += 1

    return i

if __name__ == "__main__":
    n = 150
    #print is_ugly_number(n)
    print find_nth_ugly_number(n)
#!/usr/bin/env python

def multiply_3point5(num):
    #return (num << 2) - (num >> 1)
    return (num<<1) + num + (num>>1)

if __name__ == "__main__":
    num = 5
    print num, "x 3.5 =", multiply_3point5(num)
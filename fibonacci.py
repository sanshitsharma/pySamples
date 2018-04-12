#!/usr/bin/python

def fib_recurse(n):
    print "n =", n
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recurse(n-1) + fib_recurse(n-2)

def fib_iterative(n):
    res = [0, 1]
    for i in range(2, n):
        res.append(res[i-1] + res[i-2])

    return res[n-1]


if __name__ == "__main__":
    n = 21
    print fib_recurse(5)
    print fib_iterative(5)
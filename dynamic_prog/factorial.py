#!/usr/bin/python

cache = {}

def fact(n):
    if n < 2:
        cache[n] = 1
        return cache[n]

    if cache.has_key(n-1):
        print "fetched fact(" + str(n-1) + ") from cache"
        cache[n] =  n * cache[n-1]
    else:
        cache[n] = n * fact(n-1)

    return cache[n]

def main():
    T = raw_input()

    nums = []
    for _ in range(0, int(T)):
        n = raw_input()
        print "factorial of '" + n + "' = " + str(fact(int(n)))

if __name__ == "__main__":
    main()
